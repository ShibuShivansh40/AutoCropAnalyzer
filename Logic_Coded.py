import RPi.GPIO as GPIO
import time
from time import sleep
from RpiMotorLib import RpiMotorLib

#Setting up the Pin fopr Relay
GPIO.setmode(GPIO.BCM) 
pos2 = 12
pos1 = 6
pos3 = 5
pos4 = 23
pos5 = 24

GPIO.setup(pos1,GPIO.OUT)
GPIO.setup(pos2,GPIO.OUT)
GPIO.setup(pos3,GPIO.OUT)
GPIO.setup(pos4,GPIO.OUT)
GPIO.setup(pos5,GPIO.OUT)

#Functioning of Relay
GPIO.output(pos1, GPIO.LOW)
GPIO.output(pos2, GPIO.LOW)
sleep(1) #Time declared to execute the above command 
GPIO.output(pos1, GPIO.HIGH)
GPIO.output(pos2, GPIO.HIGH)
sleep(30)
#The below is added to switch the relay off
GPIO.output(pos1, GPIO.LOW)
GPIO.output(pos2, GPIO.LOW)
sleep(1)
    
#define GPIO pins
GPIO_pins = (14, 15, 18) # Microstep Resolution MS1-MS3 -> GPIO Pin
direction_tt= 20       # Direction -> GPIO Pin
step_tt= 21# Step -> GPIO Pin
 
direction_sol = 19
step_sol = 26
 
# Declare an named instance of class pass GPIO pins numbers
mymotortest_tt = RpiMotorLib.A4988Nema(direction_tt, step_tt, GPIO_pins, "A4988")
mymotortest_sol = RpiMotorLib.A4988Nema(direction_sol, step_sol, GPIO_pins, "A4988")


t_end = time.time() + 60
# call the function, pass the arguments
while(time.time() < t_end):
    #Colockwise, Steps, Iteration, Speed
    mymotortest_sol.motor_go(False, "Full" , 50, .0015, False, .05)
    mymotortest_sol.motor_go(True, "Full", 50, 0.0015, False, .05)
#code is set with the values of Big Beaker

sleep(1)

GPIO.output(pos3, GPIO.LOW)
sleep(1)
GPIO.output(pos3, GPIO.HIGH)
sleep(60)
GPIO.output(pos3, GPIO.LOW)
sleep(1)

sleep(1)

t_end = time.time() + 60
# call the function, pass the arguments
while(time.time() < t_end):
    #Colockwise, Steps, Iteration, Speed
    mymotortest_sol.motor_go(False, "Full" , 50, .0015, False, .05)
    mymotortest_sol.motor_go(True, "Full", 50, 0.0015, False, .05)

sleep(1)
GPIO.output(pos4, GPIO.LOW)
sleep(1)
GPIO.output(pos4, GPIO.HIGH)
sleep(120)
GPIO.output(pos4, GPIO.LOW)
sleep(1)

sleep(1)

t_end = time.time() + 60
# call the function, pass the arguments
while(time.time() < t_end):
    #Colockwise, Steps, Iteration, Speed
    mymotortest_sol.motor_go(False, "Full" , 50, .0015, False, .05)
    mymotortest_sol.motor_go(True, "Full", 50, 0.0015, False, .05)

#Solution is prepared till this line
    

