"""Basic relay test script."""

import time
import RPi.GPIO as GPIO

relay_pin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)
GPIO.output(relay_pin, GPIO.LOW)

time.sleep(0.25)

GPIO.output(relay_pin, GPIO.HIGH)
GPIO.cleanup()
