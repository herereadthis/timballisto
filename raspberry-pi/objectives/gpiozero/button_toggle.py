"""The most basic LED toggle script."""
# https://learning.raspberrypi.org/en/projects/physical-computing

from gpiozero import Button, LED

# attach jumper lead from GPIO pin 17, then to a 330 ohm resistor
# from the 330 ohm resistor to an LED, then back to ground (GND) pin
led = LED(17)
# attach jumper lead from GPIO pin 23, then to a button
# from the button, attach a lead back to ground (GND) pin
button = Button(23)


def main():
    """Demo the toggle method."""
    print('gpiozero demo: Button class with toggle()')
    print('Press CTRL+C to quit')
    try:
        # This while loop is always true, so it's always waiting for a press
        while True:
            button.wait_for_press()
            # toggle method alternates between ON and OFF
            led.toggle()

    except KeyboardInterrupt:
        print('Demo over.')
        pass


if __name__ == '__main__':
    main()
