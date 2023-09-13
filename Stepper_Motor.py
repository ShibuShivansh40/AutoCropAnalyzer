
 
import RPi.GPIO as GPIO
from time import sleep
# import the library
from RpiMotorLib import RpiMotorLib
    
#define GPIO pins
GPIO_pins = (14, 15, 18) # Microstep Resolution MS1-MS3 -> GPIO Pin
direction= 20       # Direction -> GPIO Pin
step = 21      # Step -> GPIO Pin
 
# Declare an named instance of class pass GPIO pins numbers
mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")


# call the function, pass the arguments
while(True):
    #Colockwise, Steps, Iteration, Speed
    mymotortest.motor_go(False, "Full" , 200, .0004, False, .05)
    mymotortest.motor_go(True, "Full", 200, 0.0004, False, .05)

