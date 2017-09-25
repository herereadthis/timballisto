"""Use a passive infrared motion sensor (PIR) to detect movement."""

from gpiozero import MotionSensor, LED

led = LED(17)
pir = MotionSensor(24)


def main():
    """Demo the PIR motion sensor."""
    try:
        while True:
            pir.wait_for_motion()
            led.on()
            print("You moved")
            pir.wait_for_no_motion()
            led.off()
            print("You stopped")

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
