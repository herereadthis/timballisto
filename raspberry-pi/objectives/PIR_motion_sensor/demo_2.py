"""Use a passive infrared motion sensor (PIR) to detect movement."""

# Alternate GPIOZERO methods

from gpiozero import MotionSensor, LED

led = LED(17)
pir = MotionSensor(24)


def active_sensor():
    """Run when motion detected."""
    led.on
    print('Sensor Activated.')


def inactive_sensor():
    """Run when motion no longer detected."""
    led.off
    print('Sensor going inactive.')


def main():
    """Demo the PIR motion sensor."""
    try:
        pir.when_motion = active_sensor()
        pir.when_no_motion = inactive_sensor()

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
