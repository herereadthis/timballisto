"""Control a button, which can also control an LED."""

# https://learning.raspberrypi.org/en/projects/physical-computing

# Also get button class
from gpiozero import Button, LED
from time import sleep

# attach jumper lead from GPIO pin 17, then to a 330 ohm resistor
# from the 330 ohm resistor to an LED, then back to ground (GND) pin
led = LED(17)
# attach jumper lead from GPIO pin 2, then to a button
# from the button, attach a lead back to ground (GND) pin
button = Button(2)


def main():
    """Demo the Button class."""
    # method that waits for you click press the button
    # note that you can only do this once
    # after you press the button, nothing will happen again.
    button.wait_for_press()
    print('you pushed me')
    led.on()
    sleep(3)
    led.off()

if __name__ == '__main__':
    main()
