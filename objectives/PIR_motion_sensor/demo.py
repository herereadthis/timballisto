"""Use a passive infrared motion sensor (PIR) to detect movement."""

from gpiozero import MotionSensor

pir = MotionSensor(24)


def main():
    """Demo the PIR motion sensor."""
    try:
        while True:
            pir.wait_for_motion()
            print("You moved")
            pir.wait_for_no_motion()
            print("You stopped")

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
