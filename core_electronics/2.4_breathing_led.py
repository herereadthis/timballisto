# 2.4 breath an LED, based on 2.2

# package to control GPIO
import RPi.GPIO as GPIO
# gives delays to create blinking
import time
import math

# good practice to label pin definitions at the top

# pulse width modulation
pwmPin = 18
ledPin = 23
buttonPin = 17

# a constant duty cycle
# a number between 0 and 100% that describes how much power will be supplied
duty = 0

# set up the GPIO

# this means setting the GPIO numbering to those defined by the manufacturer of
# the chip - Broadcom Numbering System
GPIO.setmode(GPIO.BCM)
# tell the pins what we want them to do
GPIO.setup(ledPin, GPIO.OUT)  # output
GPIO.setup(pwmPin, GPIO.OUT)  # output
# activate with an internal pull up resister
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# initialize the PWM channel
# we've setup the PWM as an output, but we've not actually attached it any PWM
# properties yet.
# 200 is the frequency we want the pwm to run at
pwm = GPIO.PWM(pwmPin, 200)

# set the blinking led to off initially
GPIO.output(ledPin, GPIO.LOW)
# start the duty cycle
pwm.start(duty)


def mapFun(x, inLow, inHigh, outLow, outHigh):
    inRange = inHigh - inLow
    outRange = outHigh - outLow
    # normalizing.
    # saying if x = 0, then x is 0% of the inRange
    inScale = (x - inLow) / inRange
    # the output is a percentage of the inRange added to outLow
    return outLow + (inScale * outRange)


x = 0

try:
    while 1:
        # not pressed
        if GPIO.input(buttonPin):
            step = 0.02
        else:
            step = 0.05
        # the sin(x) goes between a range of -1 to 1 (inRange)
        # scale that to 1 to 100 for the duty cycle
        duty = mapFun(math.sin(x), -1, 1, 0, 100)
        x += step
        pwm.ChangeDutyCycle(duty)
        # print(duty)
        time.sleep(0.01)
        if x >= 2 * math.pi:
            x = 0

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    print('Halted Cleanly')
