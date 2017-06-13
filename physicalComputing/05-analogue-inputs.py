# https://www.raspberrypi.org/learning/physical-computing-with-python/analogue/

# SPI
# The Serial Peripheral Interface(SPI) is a communication protocol to transfer
# data between micro-computers like the Raspberry Pi and peripheral devices.
# These devices may be either sensors or actuators.
#
# Go into Raspberry Pi Configuration > Interfaces > enable SPI



from gpiozero import MCP3008
import math
from time import sleep

pot = MCP3008(0)

while True:
    pot_value = round(pot.value * 100)
    print(pot_value)
    sleep(0.1)
