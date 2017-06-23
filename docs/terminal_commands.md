# Useful Commands in Terminal

## Pi-Specific Stuff

```bash
# Turn off a Raspberry Pi
sudo halt

# Restart a Raspberry Pi
sudo reboot
```

## Moving Around

```bash
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
```

## Networking

```bash
# what is my IP address?
hostname -I

# scan the whole subnet for other devices
nmap -sn 192.168.1.0/24
```