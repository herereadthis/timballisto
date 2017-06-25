# Useful Commands in Terminal

## Pi-Specific Stuff

```bash
# Turn off a Raspberry Pi
sudo halt

# Restart a Raspberry Pi
sudo reboot
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
```