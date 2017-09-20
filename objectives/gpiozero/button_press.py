"""Make an LED on only when button is pressed, off when not pressed."""
# https://learning.raspberrypi.org/en/projects/physical-computing

from gpiozero import Button, LED
# https://docs.python.org/3/library/signal.html
# provides signal handlers in Python
from signal import pause

# attach jumper lead from GPIO pin 17, then to a 330 ohm resistor
# from the 330 ohm resistor to an LED, then back to ground (GND) pin
led = LED(17)
# attach jumper lead from GPIO pin 23, then to a button
# from the button, attach a lead back to ground (GND) pin
button = Button(23)


def main():
    """Demo the Button class."""
    # method that waits for you click press the button
    # note that you can only do this once
    # after you press the button, nothing will happen again.
    print('gpiozero demo: Button class with pressed and release()')
    print('Press CTRL+C to quit')
    try:
        # these two methods don't block the flow of the program
        # so they will cycle indefinitely when placed in a loop
        button.when_pressed = led.on
        button.when_released = led.off
        pause()

    except KeyboardInterrupt:
        print('Demo over.')
        pass


if __name__ == '__main__':
    main()
