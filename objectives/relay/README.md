# Relay Modules

Relay modules allow controlling of AC devices. Changing the 3.3 V input voltage from `HIGH` to `LOW` will trip a relay, allowing controlling of things that are using AC power, or other sources of DC power.

* Connect `DC IN` to `5V`
* Connect `DC OUT` to `GND`
* Connect `VCC` to a standard GPIO pin, such as `GPIO17` or `GPIO23`

Some relays will have a high/low trigger jumper.

* High trigger means you must turn ON the input to turn on the relay.
* Low trigger means you must turn OFF the input to turn on the relay