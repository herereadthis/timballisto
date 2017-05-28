# LUTRA!

![Raspberry Pi](https://raw.githubusercontent.com/herereadthis/lutra/master/resources/images/raspberry_pi_64x64.png)

This repo is for me to keep track of whatever I'm doing with my Raspberry Pi.

### How to turn on/off the pi

```bash
sudo halt
sudo reboot
```

### Install these

```bash
# xclip allows you to copy + paste from command line
sudo apt-get install xclip 
# X Windows screensaver application
# the option will show up under "Preferences" from the Desktop menu.
sudo apt-get install xscreensaver
# Network Mapper tool for network discovery
sudo apt-get install nmap
# Requests is an elegant and simple HTTP library for Python
# http://docs.python-requests.org/en/master/
sudo apt-get install python3-requests
```

### Updating

```bash
# download the package lists from repositories and "updates" them to get
# information on the newest versions
sudo apt-get update
# upgrade your packages
sudo apt-get upgrade
# upgrade your distribution
sudo apt-get dist-upgrade
```

### Set up Github

```bash
git config --global user.name "herereadthis"
git config --global user.email "herereadthis@email.com"
```

### Generate Github SSH keys

```bash
# generate keys
cd ~
mkdir .ssh
cd .ssh
ssh-keygen -t rsa -b 4096 -C "herereadthos@email.com"
# you will be prompted to create a file; the id_rsa default is fine
# you will also be prompted to create a passphrase; create it
# start the ssh-agent
eval "$(ssh-agent -s)"
# add SSH private key to the ssh-agent
ssh-add id_rsa
#copy the SSH key
xclip -sel clip < id_rsa.pub
```

Log in to your github page, then go to [/settings/keys](https://github.com/settings/keys), and select "New SSH key." Paste your key there and save.

```bash
# test your connection
ssh -T git@github.com
# verify by typing yes
```

### Virtual Network computing

[VNC Conect from RealVNC is included with Raspbian](https://www.raspberrypi.org/documentation/remote-access/vnc/README.md). The packages are `realvnc-vnc-server` and `realvnc-vnc-viewer` In Menu > Preferences > RPi Config > Interfaces, enable VNC.

```bash
# what is my IP address?
hostname -I
# scan the whole subnet for other devices
nmap -sn 192.168.1.0/24
```

* Direct connection: Download VNC Viewer onto your computer, and look for the IP address of the Raspberry Pi. Username/password is pi/raspberry as default.
* Cloud Connection: [Register an account with RealVNC](https://www.realvnc.com/raspberrypi/#sign-up). Then go to VNC Server on Raspberry Pi (top right corner), and sign into VNC Viewer on your other machine.
* Virtual Desktop: In RPi terminal run ```vncserver``` and it will generate an IP address. Use that address in VNC viewer. Run ```vncserver -kill :<display-number>``` to kill.

### Bash Aliases

[Copy the bash script from this repo's resources directory](https://github.com/herereadthis/lutra/blob/master/resources/.bash_aliases)

```bash
cd ~
# paste into this new file, so you don't have to mess with .bashrc
touch .bash_aliases
# relaunch bash
exec bash
```
 
