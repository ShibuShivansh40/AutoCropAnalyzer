import RPi.GPIO as GPIO
from time import sleep
# import the library
from RpiMotorLib import RpiMotorLib
    

#Setting up the Pin fopr Relay
GPIO.setmode(GPIO.BCM) 
positive1 = 11
GPIO.setup(positive1,GPIO.OUT)



#define GPIO pins
GPIO_pins = (14, 15, 18) # Microstep Resolution MS1-MS3 -> GPIO Pin
direction= 20       # Direction -> GPIO Pin
step = 21      # Step -> GPIO Pin
 
# Declare an named instance of class pass GPIO pins numbers
mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")


# call the function, pass the arguments
while(True):
    #Functioning of Relay
    GPIO.output(positive1, GPIO.LOW)  
    sleep(1) #Time declared to execute the above command 
    GPIO.output(positive1, GPIO.HIGH) 
    sleep(5)
    #The below is added to switch the relay off
    GPIO.output(positive1, GPIO.LOW)  
    sleep(1)
    
    #Colockwise, Steps, Iteration, Speed
    mymotortest.motor_go(False, "Full" , 2000, .0004, False, .05)
    mymotortest.motor_go(True, "Full", 2000, 0.0004, False, .05)
