# https://www.raspberrypi.org/learning/physical-computing-with-python/analogue/

# SPI
# The Serial Peripheral Interface(SPI) is a communication protocol to transfer
# data between micro-computers like the Raspberry Pi and peripheral devices.
# These devices may be either sensors or actuators.
#
# Go into Raspberry Pi Configuration > Interfaces > enable SPI

from gpiozero import MCP3008, PWMLED
import math
from time import sleep

pot1 = MCP3008(0)
pot2 = MCP3008(1)

led = PWMLED(21)

def fader():
    while True:
        pot1_value = round(pot1.value, 2)
        # led.source = pot.values
        led.value = pot1_value
        print(pot1_value)
        sleep(0.1)

def blinker():
    while True:
        pot1_value = round(pot1.value, 2)
        pot2_value = round(pot2.value, 2)
        print(pot1_value, pot2_value)
        led.blink(
            on_time=pot1_value,
            off_time=pot2_value,
            n=1,
            background=False
        )

def pulser():
    while True:
        pot1_value = round(pot1.value, 2)
        pot2_value = round(pot2.value, 2)
        print(pot1_value, pot2_value)
        led.pulse(
            fade_in_time=pot1_value,
            fade_out_time=pot2_value,
            n=1,
            background=False
        )
        
