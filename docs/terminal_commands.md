# Useful Commands in Terminal

## Pi-Specific Stuff

### On/Off

```bash
# Turn off a Raspberry Pi
sudo halt

# Restart a Raspberry Pi
sudo reboot
```

### Services

```bash
# See bluetooth status
sudo systemctl status bluetooth

# Stop bluetooth service
sudo systemctl stop bluetooth

# Start bluetooth service
sudo systemctl start bluetooth
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
pep8 --first PATH/TO/file.py
# lint a file, very detailed
pep8 --show-source --show-pep8 PATH/TO/file.py
```

## Networking

```bash
# what is my IP address?
hostname -I

# scan the whole subnet for other devices
nmap -sn 192.168.1.0/24

# Find the IP address of your DNS
cat /etc/resolv.conf
```