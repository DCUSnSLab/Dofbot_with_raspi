#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
# GPIO.setmode(GPIO.BOARD)
# tmp = "0"
for i in [12, 13, 18, 19]:
    GPIO.setup(i, GPIO.OUT)
    # GPIO.output(i, GPIO.HIGH)
    pwm = GPIO.PWM(i, 100)
    pwm.start(100)
    print("> GPIO {0} : PWM".format(i))
    # tmp = str(input(">> PASS ?"))
    time.sleep(5)
    pwm.stop()
    # GPIO.output(i, GPIO.LOW)
GPIO.cleanup()
