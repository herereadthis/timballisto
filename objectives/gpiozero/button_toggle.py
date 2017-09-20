"""The most basic LED toggle script."""

# https://learning.raspberrypi.org/en/projects/physical-computing

from gpiozero import Button, LED

led = LED(17)
button = Button(2)


def main():
    """Demo the toggle method."""
    # This while loop is always true, so it's always waiting for a press
    while True:
        button.wait_for_press()
        # toggle method alternates between ON and OFF
        led.toggle()

if __name__ == '__main__':
    main()
