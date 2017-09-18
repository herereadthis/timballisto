# Do These Things When You Get a Raspberry Pi

## Quick version

The Lutra repo has a bunch of setup scripts! [Setup Github](https://github.com/herereadthis/lutra/blob/master/docs/github_setup.md) if you haven't already.

```bash
# Recommended: all repositories should go into a repos directory at home
mkdir -p ~/repos;cd repos
git clone git@github.com:herereadthis/lutra.git
cd lutra/resources
./complete_install.sh

# instead of complete install, you can pick and choose

# recommended start from scratch
./rpi_setup.sh

# setup RTL-SDR
./rtlsdr_setup.sh

# install recommended Git Repos
./repo_setup.sh                        
```

## Set Preferences

* Go to Main Menu > Preferences > Raspberry Pi Configuration
* Go to Localisation, then change Locale, Timezone, Keyboard, and WiFi Country

## Change the default password
```bash
# The default user on a Rapberry Pi is pi, password: raspberry
# Change the sudoer password
passwd
```

### Enable Kernal Modules at boot

```bash

# If you want to load kernal drivers at boot run complete_instal or rpi_setup
# otherwise,
cd lutra/resources
cp ./modules /etc/modules
```

### Interfaces

* Go to Menu > Preferences > Raspberry Pi Configuration > Interfaces.
* Enable Camera, SSH, VNC, SPI, I<sup>2</sup>C, Serial, and 1-Wire.


## Install these

### Pip is messed up

Currently, Rasbian Jessie comes with two versions of Python, `2.7` and `3.4`. When you run `pip install <packagename>`, it will default all installations to `/usr/local/lib/python2.7/dist-packages`. We don't want this because you're going to get `ImportError: No module named 'packagename'` for just about anything you install. By properly installing Pip, all future installs will instead go to `3.4`. I suppose you can mess with `PATH` or always specify `python3.4 -m pip install <packagename>` but that gets old.

```bash
# This solved a lot of problems for me. 
# I recommend it; you don't have to if you're not comfortable
sudo pip uninstall pip
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
rm get-pip.py
```

### Highly recommended

```bash
# Network Mapper tool for network discovery
sudo apt-get install -y nmap

# xclip allows you to copy + paste from command line
sudo apt-get install -y xclip

# Python linter to check if files are written correctly
sudo pip3 install -U flake8

# Command line interface for testing internet bandwidth
sudo pip3 install -U speedtest-cli

# Manage virtual environments to isolate Python projects from one another
sudo pip3 install -U virtualenv virtualenvwrapper

# All the above, condensed
sudo apt-get install xclip nmap
sudo pip3 install speedtest-cli flake8 virtualenv virtualenvwrapper
```

### Good to have

```bash
# The Arduino IDE and microcontroller manager
sudo apt-get install -y arduino

# Libudev provides API to instrospect and enumerate devices
sudo apt-get install -y libudev-dev

# Matplotlib is a Python 2D plotting library: https://matplotlib.org/
sudo apt-get install -y python3-matplotlib

# Requests is an elegant and simple HTTP library for Python
# http://docs.python-requests.org/en/master/
sudo apt-get install -y python3-requests

# Thermometer driver using 1-wire communication
sudo apt-get install -y python3-w1thermsensor

# X Windows screensaver application
# the option will show up under "Preferences" from the Desktop menu.
sudo apt-get install -y xscreensaver

# Super simple Google Spreadsheets Python API
sudo pip3 install -U gspread

# Python library for accessing resources protected by OAuth 2.0
sudo pip3 install -U oauth2client

# A packet manipulation program & library, e.g., sniff for stuff on your wifi
sudo pip install -U scapy

# SMS communication
sudo pip3 install -U twilio

# Utility for interacting with PyPi: Python Package Index
sudo pip3 install -U twine

# All the above, condensed
sudo apt-get install arduino libudev-dev python3-matplotlib  python3-requests python3-w1thermsensor xscreensaver
sudo pip install gspread oauth2client scapy twilio twine
```

## Updating

```bash
# download the package lists from repositories and "updates" them to get
# information on the newest versions
sudo apt-get update

# upgrade your packages
sudo apt-get upgrade

# upgrade your distribution
sudo apt-get dist-upgrade
```

## Bash Aliases

(No need to do this if you've run the `rpi_setup.sh` script) [Copy the bash script from this repo's resources directory](https://github.com/herereadthis/lutra/blob/master/resources/.bash_aliases)

```bash
cd ~
# paste into this new file, so you don't have to mess with .bashrc
touch .bash_aliases

# relaunch bash
exec bash
```

## Networking

### Hostnames

You will probably end up having multiple Pis on your network, so you should give each a unique name. The name can only use letters `a-zA-Z`, numbers `0-9`, and dash `-`

```bash
sudo nano /etc/hosts
# Find the line that says this:
127.0.1.1       raspberrypi
# And replace with this:
127.0.1.1       mynewhostname

sudo nano /etc/hostname
# This file is only 1 line.
# Replace 'raspberrypi' with new hostname

# Reboot the pi and test the new hostname
# You'll also notice the prompt in terminal has changed.
hostname

```

### Virtual Network Computing

[VNC Conect from RealVNC is included with Raspbian](https://www.raspberrypi.org/documentation/remote-access/vnc/README.md). The packages are `realvnc-vnc-server` and `realvnc-vnc-viewer` In Menu > Preferences > RPi Config > Interfaces, enable VNC.

```bash
# what is my IP address?
hostname -I

# scan the whole subnet for other devices
nmap -sn 192.168.1.0/24
```

* Direct connection: Download VNC Viewer onto your computer, and look for the IP address of the Raspberry Pi. Username/password is pi/raspberry as default.
* Cloud Connection: 
  * [Register an account with RealVNC](https://www.realvnc.com/raspberrypi/#sign-up).
  * Enable VNC server at Menu > Preferences > Raspberry Pi Configuration > Interfaces.
  * Then go to VNC Server on Raspberry Pi (top right corner) and sign in, 
  * Go to another computer, [install VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/), and sign in.
* Virtual Desktop: In RPi terminal run ```vncserver``` and it will generate an IP address. Use that address in VNC viewer. Run ```vncserver -kill :<display-number>``` to kill.


## Scheduling

[Read the docs on scheduling](https://github.com/herereadthis/lutra/blob/master/docs/scheduling.md) for a more detailed explanation.

```bash
# open cron jobs
crontab -e

# paste the following, which will:
# update all packages every Monday at 3AM
0 3 * * 1 sudo apt-get update && sudo apt-get -y upgrade
```

## Dropbox

* The official Dropbox client supports only x86 computers; RPi is ARM. 
* [Guides exist](https://www.hackster.io/dmitry21/run-dropbox-on-raspberry-pi-5449b4) to launch a guest x86 system with the [32-bit Debian](https://www.dropbox.com/install), but doing so seems lame. 
* Instead, go get [Dropbox API keys](https://www.dropbox.com/developers/apps/create), create an app, and "generate" an access token.
* Then do the following:

```bash
# Install Dropox Uploader, a bash script
cd /PATH/TO/REPOS
git clone https://github.com/andreafabrizi/Dropbox-Uploader.git
cd Dropbox-Uploader/

# give exec permission
chmod +x dropbox_uploader.sh
./dropbox_uploader.sh

# First run-through will ask for configuration. Use the access token generated from the API app.
# Config will be stored at ~/.dropbox_uploader
# Usage / Flags: -s is skip existing file, default is overwite

# upload a file from a directory to remote dropbox
./dropbox_uploader.sh upload /PATH/TO/local_file /REMOTE/PATH
./dropbox_uploader.sh upload /PATH/* /

# download
./dropbox_uploader.sh download /PATH/TO/remote_file

# Other commands: delete copy, mkdir, space, list
```

## Static IP Address

* Get your Pi to [boot up with the same IP address each time](https://www.raspberrypi.org/learning/networking-lessons/rpi-static-ip-address/], which could be useful for making a self-contained netwrk or building a standalone project.
* You will will be editing your DHCP configuration. DHCP stands for Dynamic Host Configuration Protocol

```bash
# Every network has its own configuration; see how yours is numbered
ifconfig wlan0
# Look at "inet addr" For example, mine is 192.168.1.15
# Note the first three number sets. The last is the one we want to control
# this command also gets your IP
hostname -I

# Find the IP address of your router, with the first 3 number sets from above
# like so: ###.###.#.0/24
nmap -sn 192.168.1.1/24
# My router (same for you if you have Verizon FiOS) is 192.168.1.1

# Find the IP address of your DNS
cat /etc/resolv.conf

# Edit dhcpcd, which is the DHCP client daemon.
# It gets the host info (IP, netast, broadcast address, etc) fro a DHCP server 
# and configures the network machine on which is running.
sudo nano /etc/dhcpcd.conf

# paste the following at the bottom of the configuration file.

# interface is network interface, wired = eth0, wireless = wlan0
# static ip_address is what the static IP for the RPi will be.
# I want 18 for ethernet, 19 for wifi
# static routers is the router's IP address, determined previously
# static domain_name_servers is the DNS, determined previously

interface eth0

static ip_address=192.168.1.18/24
static routers=192.168.1.1
static domain_name_servers=192.168.1.1

interface wlan0

static ip_address=192.168.1.19/24
static routers=192.168.1.1
static domain_name_servers=192.168.1.1

# After saving, reboot and then confirm changes happened
ifconfig
ping www.raspberrypi.org
```
