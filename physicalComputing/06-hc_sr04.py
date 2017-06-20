"""This is a primer on using the HC-SR04 ultrasonic distance sensor."""
# https://www.raspberrypi.org/learning/physical-computing-with-python/distance/
# so this thing is very narrow in measuring something. It pretty much has to be
# in a direct line of sight to work.

from gpiozero import DistanceSensor

"""
Create an instance of DistanceSensor
Echo and trigger correspond to the ones marked on the sensor.
Plug Echo in GPIO #17
Plug Trigger into GPIO #04
"""
ultrasonic = DistanceSensor(
    echo=17,
    trigger=4,
    threshold_distance=0.02,
    max_distance=4
)


def hello():
    """Do something."""
    print('hello')


def bye():
    """Do something."""
    print('bye')


# ultrasonic.when_in_range = hello
# ultrasonic.when_out_of_range = bye

while True:
    print(ultrasonic.distance)
