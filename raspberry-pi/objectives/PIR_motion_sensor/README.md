# PIR - Pyroelectric ("Passive") InfraRed Sensor

![PIR](https://raw.githubusercontent.com/herereadthis/lutra/master/resources/images/pir_350x320.png)

* There are many different models, the recommended one is HC-SR01
* PIR sensors allow motion detection by detecting changes in infrared radiation.
* After plugging it in, wait for about a minute for it to stabilize.
* The three connectors on the PIR are:
  * `Vcc`, which connects to `5V`
  * `Out`, which connects to a `GPIO` pin
  * `GND`, which connects to `GND`

* Position the sensor so the bulb is facing you, and the the potentiometers are on top.
  * The left controls <strong>sensitivity</strong>, turning clockwise increases sensing distance to 7 meters, fully counterclockwise decreases to 3 meters.
  * The right controls <strong>delay</strong> or timeout, turning fully counter-clockwise means it's on for 5 seconds when it detects motion. Turning it fully clockwise turns it on for 3000 seconds.
* There is also a jumper for <strong>L</strong> and <strong>H</strong>
  * <strong>L</strong> (non-retriggering mode) - turns on and off while motion is detected
  * <strong>H</strong> (retriggering mode) - stays on while motion is detected