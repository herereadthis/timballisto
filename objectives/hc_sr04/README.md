# HC-SR04 Ultrasonic Distance Sensor

![Raspberry Pi](https://raw.githubusercontent.com/herereadthis/lutra/master/resources/images/hc_sr04_425x250.png)

### Details

* Provides distance readings from `0.02m` to `4m`.
* The 4 connections are `VCC`, `Trigger`, `Echo`, and `GND`
* The output of the HC-SR04 is 5v, but the input pins of the RPi GPIO are 3.3v
* The main problem with this sensor is that it has a very narrow field of vision. You must be in its direct line of site.
* Solve this with a voltage divider circuit.

### Wiring

```
# Voltage divider formula
Vout = Vin X R2/(R1 + R2)
# We can use 330Ω and 470Ω resistors and get sort of close
3.3v = 5v X 470/(330 + 470)
# Another option is 1KΩ and 4KΩ
3.3v = 5v X 1000/(1000 + 2000)

```

* Connect `Vcc` to `5v`
* Connect `GND` to `GND`
* Connect `Trig` to `GPIO04`
* Connect `Echo` to a `330Ω` resistor
* Connect the `330Ω` resistor to `GPIO17`
* Connect the `330Ω` resistor to a `470Ω` resistor
* Connect the `470Ω` resistor to `GND`

### Programming

```python
from gpiozero import DistanceSensor
```

Fortunately `gpiozero` has [written a class to handle the HC-SR04 specifically.](https://gpiozero.readthedocs.io/en/stable/api_input.html#distance-sensor-hc-sr04)