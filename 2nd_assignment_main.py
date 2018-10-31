#########################################################################
# Date: 2018/10/02
# file name: 2nd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time
import pid


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)



    def drive_parking(self):
        self.car.drive_parking()


    # =======================================================================
    # 2ND_ASSIGNMENT_CODE
    # Complete the code to perform Second Assignment
    # =======================================================================
    def car_startup(self):
        # implement the assignment code here

        while(True):
            l=self.car.line_detector.read_digital()
            time.sleep(0.01)

            self.car.steering.turn(90-30*l[0]-10*l[1]+10*l[3]+30*l[4])
            if l==[1,1,1,1,1]:
                self.car.accelerator.stop()


if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
