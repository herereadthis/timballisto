# Do These Things When You Get a Raspberry Pi (v2)

## Get Raspbian

* Option 1: download the Raspbian image. There are three versions (go with the desktop version):
  * Full, (with recommended software): [downloads.raspberrypi.org/raspbian_full_latest](https://downloads.raspberrypi.org/raspbian_full_latest)
  * Desktop version: [downloads.raspberrypi.org/raspbian_latest](https://downloads.raspberrypi.org/raspbian_latest)
  * Lightweight and minimal: [downloads.raspberrypi.org/raspbian_lite_latest](https://downloads.raspberrypi.org/raspbian_lite_latest)
* Option 2: Terminal
  ```bash
  # install wget if necessary
  brew install wget
  # download and unzip
  wget -S https://downloads.raspberrypi.org/raspbian_latest -O raspbian.zip
  ```
* Unzip the download and go to where you downloaded it.
  ```bash
  cd /PATH/TO/RASPBIAN_IMG
  ```

### Flashing ([Mac Installation](https://www.raspberrypi.org/documentation/installation/installing-images/mac.md))

* Find your micro SD card\
  ```bash
  diskutil list
  ```
* Find the one that matches the size of your card. For the purposes of this guide, let&rsquo;s say it&rsquo;s called `disk2`.
* Wipe the card, just to be sure. Then, unmount it.
  ```bash
  # "disk2" is for demo. Be sure sure you name the disk correctly!
  # "RPI01" is what the disk will be named, for demo. Name it whatever.
  sudo diskutil eraseDisk FAT32 RPI01 MBRFormat /dev/disk2
  # Unmount it.
  diskutil unmountDisk /dev/disk2
  ```
* Copy the image to the card.
  ```bash
  # "2018-11-13-raspbian-stretch.img" is for demo. Replace with your image name!
  # Press Ctrl+T to see progress
  sudo dd bs=1m if=2018-11-13-raspbian-stretch.img of=/dev/disk2 conv=sync
  # If it fails with "dd: invalid number '1m'", replace bs=1m with bs=1M
  ```

### Enable SSH and Wifi Boot

* If you want to run the Raspberry Pi without a keyboard or monitor, first enable SSH
  ```bash
  cd /Volumes/boot
  # Create empty SSH file
  touch ssh
  ```
* Ethernet is best, but if you want to run the RPI on Wifi, create this file
  ```bash
  cd /Volumes/boot
  touch wpa_supplicant.conf
  # Edit the file
  nano wpa_supplicant.conf
  ```
* You want to copy the contents of the following into this file. Change your Wifi name and password accordingly. [Country Codes](https://www.raspberrypi-spy.co.uk/2017/04/manually-setting-up-pi-wifi-using-wpa_supplicant-conf/) are from [ISO/IEC alpha2 code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements)
  ```bash
  country=US
  ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
  update_config=1

  network={
      ssid="MY_WIFI_NAME"
      psk="MY_WIFI_PASSWORD"
      scan_ssid=1
      key_mgmt=WPA-PSK
  }
  ```

## Initial Setup

### Headless Entry, New user!

* Okay plug in the Raspberry Pi and wait a few seconds. Find its IP address:
  ```bash
  ping raspberrypi.local
  ```
* SSH into it for the first time. The default user is `pi`, the default password is `raspberry`
  ```
  ssh pi@raspberrypi.local
  # alternatively, use its IP address
  ssp pi@192.168.1.###
  ```
* You will probably have many Pis, so it will be easier for them to all have the same user.
* However, change the default password for each one
  ```bash
  passwd
  ```

### Github

* Run through the [Github instructions](./github_setup.md) to clone Lutra and come back here.

## Networking

### Hostname

* With many Pis in your network, it&rsquo;s best to give each a unique name


## Sources

* [Installing operating system images on Mac OS](https://www.raspberrypi.org/documentation/installation/installing-images/mac.md)
* [Raspbian Stretch Headless Setup Procedure](https://www.raspberrypi.org/forums/viewtopic.php?t=191252)
* [Setup WiFi on a Pi Manually using wpa_supplicant.conf](https://www.raspberrypi-spy.co.uk/2017/04/manually-setting-up-pi-wifi-using-wpa_supplicant-conf/)
* [Officially assigned code elements](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) (Wikipedia)
* [Connect from a Mac
](https://www.dexterindustries.com/getting-started/using-the-pi/connect-to-your-raspberry-pi-from-a-mac/)
