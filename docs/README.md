# More Documentation

### Coding and Software

* [Do these things first (v2)](./do_first.md) when you get a Raspberry Pi
* [How to backup your image](./backup.md)
* [Set up Github](./github_setup.md) to get and share code
* [PiHole](./pihole.md) - ad blocking


### Outdated, don&rsquo;t trust the following

* ~[Do these things first (v1, archive)](./archive/do_first_v1.md) when you get a Raspberry Pi~
* [Useful terminal commands](./terminal_commands.md) - including how to turn off a Pi
* [How to schedule tasks](./scheduling.md) when booting up or periodically (cron)
* [Advanced Configuration](./advanced_config.md)
* [Docker](./docker.md) containers for shipping code
* [NodeJS and NPM](./node_js.md) installation and usage
* [Python Virtual Environments](./virtualenv.md) for isolating dependencies

### Sensors and Circuitry

* [GPIO Pinout](./GPIO.md) - diagram of all the pins on the RPi
* [gpiozero](https://github.com/herereadthis/lutra/blob/master/objectives/gpiozero) - basic physical computing
* [How to wire MCP3008](https://github.com/herereadthis/lutra/blob/master/objectives/MCP3008) - analogue-to-digital converter (ACD)
  * [HC-SR04](https://github.com/herereadthis/lutra/blob/master/objectives/hc_sr04) - an ultrasonic distance sensor
* [PIR](https://github.com/herereadthis/lutra/blob/master/objectives/PIR_motion_sensor) - passive infrared motion sensor
* [, I<sup>2</sup>C](./I2C.md) - communication protocol using `SDA` and `SCL` pins
  * [MPU-6050 Gyroscope + Accelerometer](https://github.com/herereadthis/lutra/blob/master/objectives/MPU6050_accelerometer) - 3-axis
  * [LCD Screen](https://github.com/herereadthis/lutra/blob/master/objectives/i2c_lcd) - includes 16x2 and 20x4
* [DS18B20](https://github.com/herereadthis/lutra/blob/master/objectives/DS18B20_thermometer) thermometer sensor
* [ST7735 SPI LCD](./st7735.md), a 1.8" TFT display module
* [MAX98357](./MAX98357.md) class D amplifier
* [Relay Modules](https://github.com/herereadthis/lutra/blob/master/objectives/relay) to control AC powered devices
* [BMP180](https://github.com/herereadthis/lutra/blob/master/objectives/BMP180_barometer) barometer
* [Arduino](https://github.com/herereadthis/lutra/blob/master/objectives/arduino) configuration and usage

### RTL-SDR
* [RTL-SDR](./rtl-sdr/README.md) - Software Defined Radio: Introduction
* [ADS-B](./rtl-sdr/adsb.md) - Aircraft positioning and tracking
* [Antenna Appendix](./rtl-sdr/antennas.md) supplemental info for setting up antennas

###

## Run this first

```bash
# get a bunch of files
python3 download_stuff.py
```
