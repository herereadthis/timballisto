# Pi NAS

* Use Open Media Vault. Download page [here](https://sourceforge.net/projects/openmediavault/files/Raspberry%20Pi%20images/).
* OpenMediaVault says not to decompress but to use [Etcher](https://www.balena.io/etcher/).
* Once it&rsquo;s flashed, start up the Raspberry Pi.
* Find its IP address
  ```bash
  ping raspberrypi.local
  ```
* Open the IP address in a browser. The default user is `admin` and the default password is `openmediavault`.
* Edit &ldquo;System&rdquo;
  *  &ldquo;General Settings&rdquo; > "Web Administrator Password" - change the default password
  * "Date &amp; Time" - change the time zone
  * "Network" > "General" - change the hostname
* Edit "Storage"
  * It turns out OMV is terrible at wiping and formatting drives, especially if you are re-using drives that originally being used for Mac or Windows. See Addendum for alternatives.
* "File System"
  * Mount the drive you've added.
* "Access Rights Management"
  * "Users"
    * Create a guest user, who will only get to read files
    * Create an admin user (not OMV system admin with which you log in) who will be able to read and write
  * "Shared Folders"
    * Create directories pointing to drives. Once those are created, add users to those drives using "Privileges." The guest user only gets to read, the admin user gets to read and write
* "Services"
  * "SMB/CIFS" > "General Settings" - Toggle to enable



## Addendum

### Formatting a drive

* It&rsquo;s much easier to wipe and format a drive using Raspbian terminal. Plug your drive in and find it.
  ```bash
  lsblk
  ```
* You are going to see a drive like `/dev/sda` and it may have children such as `/dev/sda1` or whatever. Unmount all of those.
  ```bash
  umount /dev/sdb1
  ```
* Prepare the drive with `fdisk`
  ```bash
  sudo fdisk /dev/sda
  # commands:
  # press d to wipe the system
  # press p to partition. Stick with defaults (press return multiple times)
  ```
* Create the correct file system for Linux
  ```bash
  sudo mkfs.ext4 /dev/sda
  ```

<!--
* ssh into it
  ```bash
  ssh pi@191.168.1.###
  ```
* Change default password
  ```bash
  passwd
  ```
-->
