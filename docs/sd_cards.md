# SD CARDS

## Flash Raspbian

These instructions are based on using Mac OSX

```bash
# install wget if necessary
brew install wget
# download and unzip
wget https://downloads.raspberrypi.org/raspbian_latest

# identify disks
# Find something like dev/disk2 or dev/disk3 - the size will your card
diskutil list

# unmount the SD card
diskutil unmountDisk /dev/disk<# from above>
# e.g., diskutil unmountDisk /dev/disk2

# copy Rasbian image to card
sudo dd bs=1m if=PATH/TO/image.img of=/dev/rdisk<# from above> conv=sync
# example:
sudo dd bs=1m if=2017-08-16-raspbian-stretch.img of=/dev/rdisk2 conv=sync
```

## How to back up and restore a Raspberry Pi SD Card

[(Complete tutorial found on thepihut.com)](https://thepihut.com/blogs/raspberry-pi-tutorials/17789160-backing-up-and-restoring-your-raspberry-pis-sd-card)

## Using OSX

```bash
# Insert SD card into mac. Locate the card:
diskutil list

# Find the SD card by looking for a disk of the right size and name.
# Create a disk image
# This will take a while and will give no progress indication
sudo dd if=PATH_TO_SD_CARD of=~/RaspberryPiBackup.dmg

# When making backup With new card or original card, unmount first
diskutil unmountDisk /dev/disk1

# write the image
sudo dd if=~/RaspberryPiBackup.dmg of=PATH_TO_SD_CARD
```