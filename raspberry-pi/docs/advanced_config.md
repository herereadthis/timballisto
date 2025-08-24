# Advanced Configuration

This section involves manually changing `config` files on the Raspberry Pi. Most of these configurations can be accessed via menus, but sometimes you just want to dive deep. 

Please note: you have to be absolutely sure of what you are doing or you could totally bork your machine.

### Taskbar & Panels

```bash
# Config file for LXPanel
sudo nano /home/pi/.config/lxpanel/LXDE-pi/panels/panel

# Example of temperature plugin
Plugin {
  type=thermal
  Config {
    NormalColor=#00ff00
    Warning1Color=#fff000
    Warning2Color=#ff0000
    AutomaticLevels=1
    Warning1Temp=140
    Warning2Temp=145
    AutomaticSensor=1
  }
}
```

### Raspberry Pi Configuration

```bash
# open config.txt in text editor
sudo nano /boot/config.txt
```

```bash
# Commands

# list all non-zero integer config options
vcgencmd get_config int

# list all non-null string config options
vcgencmd get_config str

# get the clock speed
vcgencmd get_config arm_freq
```

* There is tons of [documentation on raspberrypi.org](https://www.raspberrypi.org/documentation/configuration/config-txt/overclocking.md) on overclocking