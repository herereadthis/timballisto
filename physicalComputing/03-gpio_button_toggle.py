# https://learning.raspberrypi.org/en/projects/physical-computing

from gpiozero import Button, LED
from time import sleep

led = LED(17)
button = Button(2)

# This while loop is always true, so it's always waiting for a press
while True:
    button.wait_for_press()
    # toggle method alternates between ON and OFF
    led.toggle()

