"""Control the lighting of an LED using the GPIO pins."""

# https://learning.raspberrypi.org/en/projects/physical-computing

# GPIO zero is a Python library which provides a interface to GPIO components
# Use to get LED class
from gpiozero import PWMLED
from time import sleep

# attach jumper lead from GPIO pin 17, then to a 330 ohm resistor
# from the 330 ohm resistor to an LED, then back to ground (GND) pin
led = PWMLED(17)

# Polarity:
# Anode (positive) - long side with rounded edge
# Cathode (negative) - short side with flat edge


def main():
    """Demo the PWMLED class."""
    print('gpiozero demo: PWMLED class')
    num_pulses = 5
    num_blinks = 5
    print('Pulse %s times' & (num_pulses))
    led.pulse(fade_in_time=2, fade_out_time=2, n=num_pulses, background=False)
    print('End pulsing.')
    sleep(2)
    print('Blink %s times' & (num_pulses))
    led.blink(
        on_time=1.5,
        off_time=1.5,
        fade_in_time=0.5,
        fade_out_time=0.5,
        n=num_blinks,
        background=False
    )
    print('End blinking.')


if __name__ == '__main__':
    main()
