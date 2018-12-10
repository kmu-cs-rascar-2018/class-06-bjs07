#########################################################################
# Date: 2018/10/02
# file name: 2nd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import RPi.GPIO as GPIO
import time
# Raspberry Pi 3번 핀을 버튼 입력으로 사용합니다.
button_pin = 19
led_pinR = 37

# Raspberry Pi 보드의 핀 순서를 사용합니다.
GPIO.setmode(GPIO.BOARD)

# button_pin을 GPIO 입력으로 설정합니다.
GPIO.setup(button_pin, GPIO.IN)
GPIO.setup(led_pinR, GPIO.OUT)
pwm = GPIO.PWM(led_pinR, 100)

class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)
        self.l = [0,0,0,0,0]

    def drive_parking(self):
        self.car.drive_parking()
    # =======================================================================
    # 2ND_ASSIGNMENT_CODE
    # Complete the code to perform Second Assignment
    # =======================================================================
    def car_startup(self):
        # implement the assignment code here
       cnt=0

       while(True):
           button_input=GPIO.input(button_pin)
           if (button_input==0):
               GPIO.output(led_pinR,True)
               print("Start")
               break

       while (cnt != 2):
            # for turn in range(2):
            #print(cnt)

            self.l = self.car.line_detector.read_digital()
            distance = self.car.distance_detector.get_distance()
            time.sleep(0.01)
            self.car.accelerator.go_forward(30)
            if self.l != [0, 0, 0, 0, 0]:
                l = self.l
                self.car.steering.turn(90 - 30 * l[0] - 10 * l[1] + 10 * l[3] + 30 * l[4])
            else:
                self.car.accelerator.go_backward(30)
                self.car.steering.turn(90 + 30 * l[0] + 10 * l[1] - 10 * l[3] - 30 * l[4])

            if l == [1, 1, 1, 1, 1]:

                while (True):
                    l = self.car.line_detector.read_digital()
                    self.car.steering.turn(90 - 30 * l[0] - 10 * l[1] + 10 * l[3] + 30 * l[4])
                    if l != [1, 1, 1, 1, 1]:
                        cnt += 1
                        break
            if (cnt==1 and l==[1,1,1,1,1]):
                self.car.steering.turn_right(90+40)
                self.car.accelerator.go_forward(30)
                time.sleep(1)
                self.car.steering.turn_left(20)
                self.car.accelerator.go_backward(30)
                time.sleep(1.5)
                GPIO.output(led_pinR, False)
                self.car.drive_parking()

            print(l)

            if distance < 25 and distance != -1:

                while (True):
                    l = self.car.line_detector.read_digital()
                    # print(distance)
                    # print("in")
                    # if l[4] ==0:
                    self.car.steering.turn_left(40)

                    if l[0] == 1 and l[1] == 1:
                        print(l)
                        # print("out1")
                        break

                while (True):
                    l = self.car.line_detector.read_digital()
                    time.sleep(0.001)

                    # if l[0] ==1 or l[1]==1 :

                    # self.car.steering.center_alignment()
                    # self.car.accelerator.go_forward(30)
                    # 직선주행
                    self.car.steering.turn_right(90 + 80)
                    # print("go")

                    self.car.accelerator.go_forward(30)
                    if l == [0, 0, 0, 0, 0]:
                        # print("out2")
                        break

                while (True):
                    l = self.car.line_detector.read_digital()
                    time.sleep(0.001)
                    # print("go3")
                    # if l[2]==0 or l[1]==0 or l[0] ==0:
                    # print(l)
                    self.car.steering.turn_right(90 + 20)
                    if l[3] == 1 or l[4] == 1:
                        print("out3")

                        break
       self.car.drive_parking()


if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
