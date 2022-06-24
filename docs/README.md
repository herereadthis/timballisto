# More Documentation

### Tutorials

* [Raspberry Pi USB Boot](https://raspberrystreet.com/learn/how-to-boot-raspberrypi-from-usb-ssd)

### Coding and Software

* [Useful terminal commands](./terminal_commands.md) - including how to turn off a Pi
* [Set up Github](./github_setup.md) to get and share code
* [How to backup your image](./backup.md)
* [ZShell](zsh.md), zsh, aliases
* [How to schedule tasks](./scheduling.md) when booting up or periodically (cron)
<!-- todo: crontab https://crontab.guru/#0-59/5_*_*_*_* -->

### Useful things to install

```
# emacs
# shortcuts: https://www.gnu.org/software/emacs/refcards/pdf/refcard.pdf
sudo apt install emacs
# quit: C-x, C-c
# Open file: C-x, C-f
# Save: C-x, C-s
# Undo: C-x, u

# docker: see https://docs.docker.com/engine/install/debian/
curl -fsSL https://get.docker.com -o get-docker.sh
# dry run
DRY_RUN=1 sh ./get-docker.sh
# install for real
sudo sh get-docker.sh
```

### RTL-SDR
* [RTL-SDR](./rtl-sdr/README.md) - Software Defined Radio: Introduction
* [ADS-B](./rtl-sdr/ads-b.md) - Aircraft positioning and tracking
* [NOAA Satellites](./rtl-sdr/ads-b.md) - tracking and building
* [Antenna Appendix](./rtl-sdr/antennas.md) supplemental info for setting up antennas

### Sensors and Circuitry

* [GPIO Pinout](./GPIO.md) - diagram of all the pins on the RPi


### Outdated, don&rsquo;t trust the following

* ~[Do these things first (v1, archive)](./archive/do_first_v1.md) when you get a Raspberry Pi~
* ~[Do these things first (v2)](./archives/do_first.md) when you get a Raspberry Pi~
* ~[Do these things next](./archives/do_next.md) to improve usability~
* [Pi NAS](./pi-nas.md) - Network Attached Storage
* [Pi-hole](./pi-hole.md) - ad blocking
* [Advanced Configuration](./advanced_config.md)
* [Docker](./docker.md) containers for shipping code
* [NodeJS and NPM](./node_js.md) installation and usage
* [Python Virtual Environments](./virtualenv.md) for isolating dependencies

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


###

## Run this first

```bash
# get a bunch of files
python3 download_stuff.py
```
