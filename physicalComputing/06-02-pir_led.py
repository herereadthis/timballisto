"""Connect a PIR sensor to an LED."""
# https://diyhacking.com/raspberry-pi-gpio-control/

import RPi.GPIO as GPIO
import time

# GPIO pin for light
ledPin = 4
# GPIO pin for sensor
pirPin = 17

# the chip - Broadcom Numbering System
GPIO.setmode(GPIO.BCM)

# no need to disble warnings for now
# GPIO.setwarnings(False)

GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(pirPin, GPIO.IN)


def led_test():
    """Test to make sure the LED is working."""
    try:
        while True:
            # Outputs digital HIGH signal (5V) on GPIO Pin 3
            GPIO.output(ledPin, 1)
            # Time delay
            time.sleep(0.25)

            # Outputs digital LOW signal (0V) on GPIO Pin 3
            GPIO.output(ledPin, 0)
            # Time delay
            time.sleep(0.25)

    # this is how we quit the script
    except KeyboardInterrupt:
        # reset all the GPIO to a safe place so we can use pi for something
        # else - clean up
        GPIO.cleanup()


def pir_led():
    """trigger the led with the pir sensor."""
    try:
        while True:
            i = GPIO.input(pirPin)

            if i == 0:
                print("nNo intruders",i)
                GPIO.output(ledPin, 0)
                time.sleep(0.1)
            elif i == 1:
                print("intruder detected",i)
                GPIO.output(ledPin, 1)
                time.sleep(0.1)
                
    except KeyboardInterrupt:
        GPIO.cleanup()

