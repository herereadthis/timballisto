"""Connect a PIR sensor to an LED."""
# https://diyhacking.com/raspberry-pi-gpio-control/

import RPi.GPIO as GPIO
import time

# Define pin 3 as an output pin
ledPin = 3

# the chip - Broadcom Numbering System
GPIO.setmode(GPIO.BCM)

# GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)

try:
    while True:
        # Outputs digital HIGH signal (5V) on GPIO Pin 3
        GPIO.output(ledPin, 1)
        # Time delay of 1 second
        time.sleep(1)

        # Outputs digital LOW signal (0V) on GPIO Pin 3
        GPIO.output(ledPin, 0)
        # Time delay of 1 second
        time.sleep(1)

# this is how we quit the script
except KeyboardInterrupt:
    # reset all the GPIO to a safe place so we can use pi for something else
    # clean up
    GPIO.cleanup()
