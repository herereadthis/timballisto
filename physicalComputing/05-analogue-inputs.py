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

# How to wire an MCP3008 Analogue-to-Digital Converter (ADC)
# The side with the notch is 0, the other side is 8.
# if the notch is facing to your left, connect wires from the raspberry pi from
# the side that is to the top of the notch (start from top left is pin 16, top
# right is 09)
#
# pin 16 goes to 3V
# pin 15 goes to 3V
# pin 14 goes to GND (or pin #17)
# pin 13 goes to SPI SCLK GP11
# pin 12 goes to SPI MISO GP09
# pin 11 goes to SPI MOSI GP10
# pin 10 goes to SPI CE0 GP08
# pin 09 goes to GND (or pin #20)

# when connecting potentiometers, middle pin goes to analogue side of MCP3008
# top or bottom go to 3V or GND. If you switch which goes to 3v and which goes
# to GND, then the dial is reversed, no worries.

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
        
