# DS18B20 Thermometer Sensor

The DS18B20 sensor comes in several flavors.

* The integrated circuit is as follows (front is the flat side with text):
  * 1 (left) is `GND`
  * 2 (middle) is `DQ` for data
  * 3 (right) is `VDD` for power
* The waterproof wire is color-coded:
  * red is power
  * yellow is data
  * black is ground

## Connection

* Connect black (ground) to `GND` (recommend #09)
* Connect red (power) to `3V3` (recommend #01)
* Connect yellow (data) to `GPIO4` (#07)
* Connect a 4.7K-Ω resitor in parallel between power and data

## Configuration

```bash
# must load the w1 kernal
sudo nano /boot/config.txt

# paste the following

# 1-Wire Communication e.g., thermometer
dtoverlay=w1-gpio,gpiopin=4
```