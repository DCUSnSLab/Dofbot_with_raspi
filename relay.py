#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

# J1 : GP23(16)
# J2 : GP11(23)
# J3 : GP9(21)
# J4 : GP10(19)
# J5 : GP25(22)
# J6 : GP2(3)

relay = 10
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay, GPIO.OUT)

GPIO.output(relay, False)

try:
    while True:
        GPIO.output(relay, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(relay, GPIO.LOW)
        time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()

