# gpiozero - GPIO Interface

Getting started with physical computing is easier with [this library](https://gpiozero.readthedocs.io/en/stable/).

These demo files build on top of each other. Follow in order.

1. [LED](https://github.com/herereadthis/lutra/tree/master/objectives/gpiozero/led.py) - `LED` class that turns a light on and off.
  * Anode (positive) - long wire with rounded edge
  * Cathode (negative) - short wire with flat edge
2. [PWMLED](https://github.com/herereadthis/lutra/tree/master/objectives/gpiozero/pwm_led.py) - light with variable brightness.
3. [Button](https://github.com/herereadthis/lutra/tree/master/objectives/gpiozero/button.py) - introduces `Button` class to trigger light using `wait_for_press()` method.
4. [Button & toggle](https://github.com/herereadthis/lutra/tree/master/objectives/gpiozero/button_toggle.py) - use `toggle()` method to trigger light.
5. [Button when pressed](https://github.com/herereadthis/lutra/tree/master/objectives/gpiozero/button_press.py) - use `when_pressed()` and `when_released()` methods.