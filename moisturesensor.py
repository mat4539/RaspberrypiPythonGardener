#!/usr/bin/python
import RPi.GPIO as GPIO
import time
 
#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
# GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change


def check_water():
 return GPIO.input(channel)