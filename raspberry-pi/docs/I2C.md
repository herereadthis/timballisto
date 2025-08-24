# I<sup>2</sup>C Tutorial

* I<sup>2</sup>C (a.k.a. I2C, IIC) is a communication protocol that runs over a two wire bus. 
* Connect to the Raspberry Pi `GPIO` pins: `SDA` (serial data) and `SCL` (serial clock).

## Installations

If you run `lutra/resources/rpi_setup.sh`, you should be all set for installationsm.

```bash
#  I2C tools for Linux: a bus probing tool, a chip dumper, register-level access helpers, EEPROM decoding scripts, and more.
# https://packages.debian.org/jessie/i2c-tools
# This should already be installed
sudo apt-get install i2c-tools

# confirm i2c-tools installation
man i2cset
man i2cget
man i2cdump

# I2C programming library development files
# https://packages.debian.org/jessie/libi2c-dev
sudo apt-get install libi2c-dev

# allows SMBus access through the I2C /dev interface on Linux hosts
# https://packages.debian.org/jessie/python-simbus
# This should already be installed
sudo apt-get install python-simbus

# all together
sudo apt-get install i2c-tools libi2c-dev python-simbus
```

## Configuration

```bash
# You will have to modify /etc/modules, which will load drivers for the kernal
# sudo nano /etc/modules
# make sure these two are enabled and included
i2c-dev
i2c-bcm2708
```

* You can also paste from this provided [modules](https://github.com/herereadthis/lutra/blob/master/resources/modules) file.

```bash
# Make sure the I2C Interface is on at boot
# sudo nano /boot/config.txt
# find this line and make sure it says "on" instead of "off"
dtparam=i2c_arm=on
```

* Alternate: go to Menu > Preferences > Raspberry Pi Configuration > Interfaces and select "Enable" for I2C.

```bash
# Comment out drivers from blacklist
sudo nano /etc/modprobe.d/raspi-blacklist.conf
# make sure this line (if it exists) is not blacklisted
# blacklist i2c-bcm2708
```

## Testing

Plug in an I<sup>2</sup>C device to confirm it's working. The whole point of using this interface that it's simple stupid.

* Connect `Vcc` to `5v` (#02)
* Connect `GND` to `GND` (#06)
* Connect `SDA` to `SDA` (#03)
* Connect `SCL` to `SCL` (#05)
* Refer to [GPIO Pinout](https://github.com/herereadthis/lutra/blob/master/docs/GPIO.md) doc for assistance.

```bash
# One of these commands will work. On my RPi3, the first command worked
sudo i2cdetect -y 1
# If that fails, try this one:
sudo i2cdetect -y 0
```

If successful, you should see an output like this:

```
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 3f 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- -- 
```

My device is connected to the I<sup>2</sup>C bus, using the address of `0x3f`.

## Acknowledgements

Enabling I<sup>2</sup>C on a Raspberry Pi 3 turned out to be more difficult than imagined. The reason is documentation exists for various combinations of RPi3 or RPi2, with installations of Raspbian Jessie or Wheezy. However, these links provided a good start:

* Ozzmaker | [How to Enable i2c on the Raspberry Pi](http://ozzmaker.com/i2c/)
* osoyoo.com | [Drive i2c LCD Screen with Raspberry Pi](http://osoyoo.com/2016/06/01/drive-i2c-lcd-screen-with-raspberry-pi/)
* TheRaspberryPiGuy | [Raspberry Pi - Mini LCD Display Tutorial](https://www.youtube.com/watch?v=fR5XhHYzUK0)
