# How to back up and restore a Raspberry Pi SD Card

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

# eject
sudo diskutil eject /dev/rdisk3
```

## Sources

* [How to Backup your Raspberry Pi SD Card](https://pimylifeup.com/backup-raspberry-pi/)
* [Backing up and Restoring your Raspberry Pi's SD Card](https://thepihut.com/blogs/raspberry-pi-tutorials/17789160-backing-up-and-restoring-your-raspberry-pis-sd-card)
