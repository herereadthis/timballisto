# PIR - Pyroelectric ("Passive") InfraRed Sensor

![PIR](https://raw.githubusercontent.com/herereadthis/lutra/master/resources/images/pir_350x320.png)

* PIR sensors allow motion detection by detecting changes in infrared radiation.
* The three connectors on the PIR are:
  * `Vcc`, which connects to `5V`
  * `Out`, which connects to a `GPIO` pin
  * `GND`, which connects to `GND`
* When looking at the side with all the guts, you will see two potentiometers
  * The left controls timeout, turning fully counter-clockwise means it's on for 2.5 seconds when it detects motion. Turning it fully clockwise turns it on for 250 seconds.
  * The right controls sensitivity,