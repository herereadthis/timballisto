# Do These Things When You Get a Raspberry Pi (v2)

## Get Raspbian

* Obviously, download the Raspbian image. There are three versions (go with the desktop version):
  * Full, (with recommended software): [downloads.raspberrypi.org/raspbian_full_latest](https://downloads.raspberrypi.org/raspbian_full_latest)
  * Desktop version: [downloads.raspberrypi.org/raspbian_latest](https://downloads.raspberrypi.org/raspbian_latest)
  * Lightweight and minimal: [downloads.raspberrypi.org/raspbian_lite_latest](https://downloads.raspberrypi.org/raspbian_lite_latest)
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

## Sources

* [Installing operating system images on Mac OS](https://www.raspberrypi.org/documentation/installation/installing-images/mac.md)
