# Useful Commands in Terminal

## Pi-Specific Stuff

### On/Off

```bash
# Turn off a Raspberry Pi
sudo halt

# Restart a Raspberry Pi
sudo reboot

# Get GPIO Information
python3
import RPi.GPIO as GPIO
print(GPIO.RPI_INFO)
```

### Services

```bash
# See bluetooth status
sudo systemctl status bluetooth

# Stop bluetooth service
sudo systemctl stop bluetooth

# Start bluetooth service
sudo systemctl start bluetooth

# Screenshots
# To take a screenshot, set the command on a delay and then select your window
# -u means active window, -d means delay, -e is exec
# screenshot will be saved to current pwd in 3s. Alt+Tab to target window.
scrot -u -d 3
# screenshot will be saved to desktop
scrot -u -d 3 -e 'mv $f ~/Desktop'
```

### Monitoring

```bash
# See CPU usage
top

# Details about the processor
cat /proc/cpuinfo

# see disk usage of a particular directory
cd PATH/TO/DIRECTORY
du -hs

# How much space is on the drive?
df -h

# See memory (RAM) usage
free -h
# Expressed in MB
free -m
# Very detailed
cat /proc/meminfo

# different ways to get uptime
uptime
cat /proc/uptime
w

# View the Pi's current frequency (clock speed) in MHz
echo $(($(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq)/1000))

# View core temperature in Celsius
echo $(($(cat /sys/class/thermal/thermal_zone0/temp)/1000))
```

## Bash

```bash
# Get the manual for commands
man

# example: the manual for the date command
man date
```

## Moving Around

```bash
# Where am I now? (Print Working Directory)
pwd

# open the current directory from inside terminal
xdg-open .

# open a file with the default text editor
xdg-open filename.md
```

## Python Stuff

```bash
# list all packages
pip freeze

# method 2, will show you a whole lot more
python3 # open python shell
help('modules')

# lint a file
flake8 path/to/file.py
# lint files in a directory
flake8 .
```

## Networking

```bash
# what is my IP address?
hostname -I

I am on WiFi, how else can I get my IP?
hostname -I | awk '{print $1}'

# scan the whole subnet for other devices
nmap -sn 192.168.1.0/24

# Find the IP address of your DNS
cat /etc/resolv.conf
```