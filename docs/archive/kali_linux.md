# Kali Linux

* Get the [Re4son Sticky Fingers Raspberry Pi image](https://whitedome.com.au/re4son/sticky-fingers-kali-pi-pre-installed-image/).
* Get the official [Kali Linux](https://www.offensive-security.com/kali-linux-arm-images/) release

* Login: `root`
* Password `toor`

Get `kalipi-config` at [Re4son](https://github.com/Re4son/RPi-Tweaks/tree/master/kalipi-config), which is basically supposed to be `raspi-config`

```bash
apt install whiptail parted lua5.1 alsa-utils psmisc libraspberrypi0 libraspberrypi-dev libraspberrypi-doc libraspberrypi-bin
wget -O /usr/local/bin/kalipi-config https://raw.githubusercontent.com/Re4son/RPi-Tweaks/master/kalipi-config/kalipi-config
chmod 755 /usr/local/bin/kalipi-config
```

```bash
# change password
passwd root
# kali flavor for sudo raspi-config
kalipi-config
# get the system up to date
apt-get update
apt-get upgrade
apt-get dist-upgrade
```

Bluetooth

```bash
# start bluetooth services
systemctl enable bluetooth
service bluetooth start
systemctl enable hciuart
systemctl start hciuart.service
# begin pairing
bluetoothctl
agent on
default-agent
```

Change the SSH Keys

```bash
cd /etc/ssh/
# see the old keys
ls
# delete all old keys
rm ssh_host_*
# reconfigure the server
dpkg-reconfigure openssh-server
# I have no idea what this is doing but the point is to help auto login at boot
update-rc.d -f ssh remove
update-rc.d -f ssh defaults
# inspect this file
# confirm "PermitRootLogin" is un-tabbed
nano /etc/ssh/sshd_config
# apply changes
sudo service ssh restart
# enable ssh at boot
update-rc.d -f ssh enable 2 3 4 5
```

Enable auto-login

```bash
kalipi-config
# change "Boot Options"
# Choose "Desktop / CLI"
# Choose "Desktop Autologin"
```

Install git

```bash
apt install git
```

Disable onboard wifi

```bash
# the device manager (udev) uses modprobe to load drivers for automatically
# detected hardware
cd /etc/modprobe.d
nano raspi-blacklist.conf

# add the following to the file:

#wifi
blacklist brcmfmac
blacklist brcmutil
```

Put the network card into monitor mode

```bash
# find name of wifi device, which is either wlan0 or wlan1
ifconfig
airmon-ng start wlan0
# see wireless network interface parameters
iwconfig
# test to see if card is capable of packet injection
aireplay-ng --test wlan0mon
```

Search the area around us

```bash
# remember to use airmon-ng to put a network card into monitor mode
airodump-ng wlan0mon
# you will get a bunch of information about all the networks in the area. 
# The key thing to look for is the channel (CH) the network operates on

# search for WEP networks
airodump-ng wlan0mon --encrypt wep
```

### Aircrack-ng

Aircrack-ng is a set of tools to access WiFi network security. It should come pre-installed with Kali Linux

```bash
apt-get install aircrack-ng
```

* `airmon-ng` puts network cards into monitor mode
* `aireplay-ng` is a packet injector
* `airodump-ng` is a packet sniffer. Find info about networks

### Airgeddon

Airgeddon allows you to attack wireless networks, a &ldquo;multi-use bash script for Linux systems to audit wireless networks.&rdquo;

Install airgeddon and essential dependencies

```bash 
apt-get update
git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git
cd airgeddon
sudo bash ./airgeddon.sh
# install lspci, which gets information about PCI buses and what's connected to them
apt-get install pciutils
# install xterm, the terminal emulator for the X Window system
apt-get install xterm
```

Other installs

```bash
# install reaver: brute force attack WPS pins
apt-get install reaver
# install bully: brute force attack WPS pins
apt-get install bully
# install lighttpd, a webserver
apt-get install lighttpd
# install sslstrip, a man-in-the-middle MITM tool
apt-get install sslstrip

# install hashcat, a password recovery utility
git clone https://github.com/hashcat/hashcat
cd hashcat
make
make install

# install mkd4, a tool to exploit common IEEE 802.11 protocol weaknesses
apt-get install pkg-config libnl-3-dev libnl-genl-3-dev libpcap-dev 
git clone https://github.com/aircrack-ng/mdk4
cd mdk4
make
make install
```


Wifi

* The wifi standars are IEEE 802.11 a/b/g/n/ac
* Newer ones are generally better. Newer ones are backwards compatible
  * a: 5GHz, 09-1999
  * b: 2.4GHz, 09-1999
  * g: 2.4GHz, 06-2003
  * n: 2.4/5GGHz, 10-2009
  * ac: 2.4/5GHz, 12-2013
* Security
  * WEP (Wired Equivalent Privacy) The first one, and very easy to crack
  * WPA(1) uses "Temporal Key Integrity Protocol" (TKIP) and is harder to crack
  * WPA2-PSK which is the home implementation of WPA2, more secure. Uses a pre-shared key (PSK)
  * WPA2-AES is the enterprise implementation of WPA2, very difficult to crack. Coupled with a RADIUS server that is used for authentication
* Channels
  * The 802.11  has 14 channels, each with a central frequency
  * For example, channel 1 is centered around 2.412 GHz, channel 2 is centered around 2.417 GHz
  * US can use channels 1&ndash;11, Europe can use channels 1&ndash;13
    * This means a device on channel 12 would be invisble to US scanners
  * Typically a device will use only a few channels, such as 1, 6, and 11 to avoid overlap


### Evil Twin Attack

What if you don't know the password to the the network?
* The evil twin attack is a social engineering attack, as it requires tricking the user into giving up information.
* Interrupt the user's connection to the access point, and capture the password exchange between the two
* Kick a user off the network
* Offer up a fake access point with the same name but a different authentication
* The user tries to connect to the fake access point
* The fake access point prompts for the real network password, which the user enters
* The fake access point checks the entered password against the password exchange hash, and if it is good, allow the user to connect to the real access point

```bash
# these should already be part of kali linux
# install macchanger, which allows you to change your mac address
apt-get install macchanger
# install aircrack-ng, which is a set of tools to access WiFi network security
apt-get install aircrack-ng
```

## Sources

* [Build a Beginner Hacking Kit with the Raspberry Pi 3 Model B+](https://null-byte.wonderhowto.com/how-to/build-beginner-hacking-kit-with-raspberry-pi-3-model-b-0184144/) (Null Byte)
* [How to Disable Onboard WiFi for Raspberry Pi 3](https://dephace.com/how-to-disable-onboard-wifi-for-raspberry-pi-3/) (Dephace)