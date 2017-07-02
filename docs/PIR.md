# PIR - Pyroelectric ("Passive") InfraRed Sensor

![PIR](https://raw.githubusercontent.com/herereadthis/lutra/master/resources/images/pir_350x320.png)

* There are many different models, the recommended one is HC-SR01
* PIR sensors allow motion detection by detecting changes in infrared radiation.
* After plugging it in, wait for about a minute for it to stabilize.
* The three connectors on the PIR are:
  * `Vcc`, which connects to `5V`
  * `Out`, which connects to a `GPIO` pin
  * `GND`, which connects to `GND`
* When looking at the side with all the guts, you will see two potentiometers
  * The left controls timeout, turning fully counter-clockwise means it's on for 5 seconds when it detects motion. Turning it fully clockwise turns it on for 3000 seconds.
  * The right controls sensitivity, turning clockwise increases sensing distance to 7 meters, fully counterclockwise decreases to 3 meters.