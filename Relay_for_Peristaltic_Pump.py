import RPi.GPIO as GPIO
from time import sleep

#Setting up the Pin fopr Relay
GPIO.setmode(GPIO.BCM) 
positive1 = 21
GPIO.setup(positive1,GPIO.OUT)

#Functioning of Relay
GPIO.output(positive1, GPIO.LOW)  
sleep(10) #Time declared to execute the above command 
GPIO.output(positive1, GPIO.HIGH) 
sleep(10)
#The below is added to switch the relay off
GPIO.output(positive1, GPIO.LOW)  
sleep(1)


"""
Description about the pins on which excution is done
1. Negative Pin is added to the Ground.
2. Positive Pin is added to the GPiO Pin Number 21.
"""
