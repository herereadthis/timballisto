# Kali Linux

Get the [Re4son Sticky Fingers Raspberry Pi image](https://whitedome.com.au/re4son/sticky-fingers-kali-pi-pre-installed-image/).

* Login: `root`
* Password `toor`

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


## Sources

* [Build a Beginner Hacking Kit with the Raspberry Pi 3 Model B+](https://null-byte.wonderhowto.com/how-to/build-beginner-hacking-kit-with-raspberry-pi-3-model-b-0184144/) (Null Byte)
* [How to Disable Onboard WiFi for Raspberry Pi 3](https://dephace.com/how-to-disable-onboard-wifi-for-raspberry-pi-3/) (Dephace)