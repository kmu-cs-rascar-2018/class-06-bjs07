
#########################################################################
# Date: 2018/10/02
# file name: 3nd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)
        self.l = [0,0,0,0,0]
        self.error = 0
        self.P = 0
        self.I = 0
        self.D = 0

        self.Kp = 0.5
        self.Ki = 0.5
        self.Kd = 0.5
        self.PID_value = 0
        self.previous_error = 0

    def drive_parking(self):
        self.car.drive_parking()

    def error_f(self):


        if self.l[0] == 1 and self.l[1] == 1 and self.l[2] == 1 and self.l[4] == 1 and self.l[4] == 0:
            self.error = 4
        elif ((self.l[0] == 1) and (self.l[1] == 1) and (self.l[2] == 1) and(self.l[4] == 0)and(self.l[4] == 0)):
            self.error = 3
        elif ((self.l[0] == 1) and (self.l[1] == 1) and (self.l[2] == 1) and (self.l[4] == 0) and (self.l[4] == 1)):
            self.error = 2
        elif ((self.l[0] == 1) and(self.l[1] == 1) and (self.l[2] == 0) and (self.l[4] == 0) and (self.l[4] == 1)):
            self.error = 1

        elif ((self.l[0] == 1)and(self.l[1] == 1) and (self.l[2] == 0) and (self.l[4] == 1) and (self.l[4] == 1)):
            self.error = 0
        elif ((self.l[0] == 1) and (self.l[1] == 0) and (self.l[2] == 0) and (self.l[4] == 1) and(self.l[4] == 1)):
            self.error = -1

        elif ((self.l[0] == 1) and (self.l[1] == 0) and (self.l[2] == 1) and (self.l[4] == 1) and (self.l[4] == 1)):
            self.error = -2
        elif ((self.l[0] == 0) and (self.l[1] == 0) and (self.l[2] == 1) and (self.l[4] == 1) and (self.l[4] == 1)):
            self.error = -3
        elif ((self.l[0] == 0) and (self.l[1] == 1) and (self.l[2] == 1) and (self.l[4] == 1) and (self.l[4] == 1)):
            self.error = -4



    def calc_pid(self):
        self.P = self.error
        self.I = self.I + self.error
        self.D = self.error-self.previous_error
        self.PID_value = (self.Kp * self.P) + (self.Ki * self.I) + (self.Kd * self.D)
        self.previous_error = self.error



    # =======================================================================
    # 2ND_ASSIGNMENT_CODE
    # Complete the code to perform Second Assignment
    # =======================================================================
    def car_startup(self):
        # implement the assignment code here
        #start_time=time.time()
        cnt=0

        while(True):
            #for turn in range(2):

                l=self.car.line_detector.read_digital()
                distance=self.car.distance_detector.get_distance()
                time.sleep(0.01)
                #print(l)
                print(self.car.distance_detector.get_distance())
                self.car.accelerator.go_forward(20)

                self.car.steering.turn(90 - 30 * l[0] - 10 * l[1] + 10 * l[3] + 30 * l[4])
                time.sleep(0.01)
                if l==[0,0,0,0,0]:
                    #self.car.steering.turn(90+ 30 * l[0] -+ 10 * l[1] - 10 * l[3] - 30 * l[4])
                    self.car.steering.center_alignment()
                    self.car.accelerator.go_backward(20)
                    time.sleep(0.1)
                if l==[1,1,1,1,1] and cnt ==1:
                    self.car.drive_parking()
                if l==[1,1,1,1,1] and cnt==0:
                    print("cnt plus")
                    cnt+=1
                if distance< 25 and distance!= -1:

                    while(True):
                        l = self.car.line_detector.read_digital()
                        print(distance)
                        print("in")
                        #if l[4] ==0:
                        self.car.steering.turn_left(40)


                        if l[0] ==1 and l[1]==1:
                            print(l)
                            print("out1")
                            break

                    while(True):
                        l = self.car.line_detector.read_digital()
                        time.sleep(0.01)

                        #if l[0] ==1 or l[1]==1 :

                            #self.car.steering.center_alignment()
                            #self.car.accelerator.go_forward(30)
                            #직선주행
                        self.car.steering.turn_right(90 + 80)
                        print("go")

                        self.car.accelerator.go_forward(20)
                        if l==[0,0,0,0,0]:
                            print("out2")
                            break


                    while(True):
                        l = self.car.line_detector.read_digital()
                        time.sleep(0.01)
                        print("go3")
                        #if l[2]==0 or l[1]==0 or l[0] ==0:
                        print(l)
                        self.car.steering.turn_right(90+20)
                        if l[3] ==1 or l[4]==1:
                            print("out3")

                            break



                        #if 0 in l
                        #self.car.steering.turn_right(90+30)
                        #time.sleep(1.4)


                        #break
                        #self.car.steering.turn_right(90+30)
                        #time.sleep(0.5)


if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
