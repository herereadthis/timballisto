# Advanced Configuration

This section involves manually changing `config` files on the Raspberry Pi. Most of these configurations can be accessed via menus, but sometimes you just want to dive deep. 

Please note: you have to be absolutely sure of what you are doing or you could totally bork your machine.

### Taskbar & Panels

```bash
# Config file for LXPanel
sudo nano /home/pi/.config/lxpanel/LXDE-pi/panels/panel
```

### Raspberry Pi Configuration

```bash
# open config.txt in text editor
xdg-open /boot/config.txt
# or
sudo nano /boot/config.txt

# you can overclock the ARM if you change arm_freq
arm_freq=1200

# list all non-zero integer config options
vcgencmd get_config int

# list all non-null string config options
vcgencmd get_config str

# get the clock speed
vcgencmd get_config arm_freq
```

* There is tons of [documentation on raspberrypi.org](https://www.raspberrypi.org/documentation/configuration/config-txt/overclocking.md) on overclocking