"""Basic relay test script."""

from gpiozero import DigitalOutputDevice
import time

# Some relays will have a jumper for high/low trigger.
# Basically, high trigger means you must turn the input on to turn on the relay.
# Low trigger means you must turn the input off to turn on the relay


def main():
    """Run a loop."""
    # Wire DC IN to 5V
    # Wire DC OUT to GND
    # Wire VCC to GPIO 23

    output_pin = 23
    relay = DigitalOutputDevice(output_pin)
    
    try:
        while True:
            relay.on()
            time.sleep(0.5)
            relay.off()
            time.sleep(0.5)

    except KeyboardInterrupt:
        pass
    finally:
        relay.close()


if __name__ == '__main__':
    main()
