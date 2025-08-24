"""Control the lighting of an LED using the GPIO pins."""

# https://learning.raspberrypi.org/en/projects/physical-computing

# GPIO zero is a Python library which provides a interface to GPIO components
# Use to get LED class
from gpiozero import LED
from time import sleep

# attach jumper lead from GPIO pin 17, then to a 330 ohm resistor
# from the 330 ohm resistor to an LED, then back to ground (GND) pin
led = LED(17)

# Polarity:
# Anode (positive) - long side with rounded edge
# Cathode (negative) - short side with flat edge


def main():
    """Demo the LED class."""
    print('gpiozero demo: LED class')
    print('Press CTRL+C to quit')
    try:
        while True:
            # on() turns the LED on
            led.on()
            # sleep is do nothing for # seconds
            sleep(0.2)
            # off() turns the LED off
            led.off()
            sleep(0.2)

    except KeyboardInterrupt:
        print('Demo over.')
        pass


if __name__ == '__main__':
    main()
