# SD CARDS

## Flash Raspbian

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