# makes an LED on only when button is pressed, off when not pressed

# https://learning.raspberrypi.org/en/projects/physical-computing

from gpiozero import Button, LED
# https://docs.python.org/3/library/signal.html
# provides signal handlers in Python
from signal import pause

led = LED(17)
button = Button(2)

# these two methods don't block the flow of the program
# so they will cycle indefinitely when placed in a loop
button.when_pressed = led.on
button.when_released = led.off

pause()
