# 2.2 connecting to the outside world with gpio

# package to control GPIO
import RPi.GPIO as GPIO
# gives delays to create blinking
import time

# good practice to label pin definitions at the top

# pulse width modulation
pwmPin = 18
ledPin = 23
buttonPin = 17

# a constant duty cycle
# a number between 0 and 100% that describes how much power will be supplied
duty = 75

# set up the GPIO

# this means setting the GPIO numbering to those defined by the manufacturer of
# the chip - Broadcom Numbering System
GPIO.setmode(GPIO.BCM)
# tell the pins what we want them to do
GPIO.setup(ledPin, GPIO.OUT) # output
GPIO.setup(pwmPin, GPIO.OUT) # output
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

# since the pins are left in the state of what it was before, we should try
try:
    # we want to set up an infinite loop with the actually functionality
    # this is always true
    while 1:
        # if button not pressed
        if GPIO.input(buttonPin):
            pwm.ChangeDutyCycle(duty)
            GPIO.output(ledPin, GPIO.LOW)
        # else if button pressed
        else:
            pwm.ChangeDutyCycle(duty)
            GPIO.output(ledPin, GPIO.HIGH)
            # delay
            time.sleep(0.5)
            # opposite of what it was before
            pwm.ChangeDutyCycle(100 - duty)
            GPIO.output(ledPin, GPIO.LOW)
            # delay
            time.sleep(0.5)
# this is how we quit the script
except KeyboardInterrupt:
    # reset all the GPIO to a safe place so we can use pi for something else
    # cut the pwm channel
    pwm.stop()
    # clean up
    GPIO.cleanup()









GPIO.cleanup()
