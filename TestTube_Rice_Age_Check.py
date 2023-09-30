#Here, we will test the Rice present in Test Tube
import RPi.GPIO as GPIO
import time
from time import sleep
from RpiMotorLib import RpiMotorLib

#Setting up the Pin fopr Relay
GPIO.setmode(GPIO.BCM) 

pos5 = 24
GPIO.setup(pos5,GPIO.OUT)

#define GPIO pins
GPIO_pins = (14, 15, 18) # Microstep Resolution MS1-MS3 -> GPIO Pin
direction_tt= 20       # Direction -> GPIO Pin
step_tt= 21# Step -> GPIO Pin
 
direction_sol = 19
step_sol = 26
 
# Declare an named instance of class pass GPIO pins numbers
mymotortest_tt = RpiMotorLib.A4988Nema(direction_tt, step_tt, GPIO_pins, "A4988")
#30 sec 25 ml
# Time to pump out 10ml = 25/30*10

sleep(1)
GPIO.output(pos5, GPIO.LOW)
sleep(1)
GPIO.output(pos5, GPIO.HIGH)
#sleep(25/30*10)
sleep(8.3)
GPIO.output(pos5, GPIO.LOW)
sleep(1)

sleep(1)

t_end = time.time() + 60
# call the function, pass the arguments
while(time.time() < t_end):
    #Colockwise, Steps, Iteration, Speed
    mymotortest_tt.motor_go(False, "Full" , 50, .0015, False, .05)
    mymotortest_tt.motor_go(True, "Full", 50, 0.0015, False, .05)