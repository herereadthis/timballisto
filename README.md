# LUTRA!

This repo is for me to keep track of whatever I'm doing with my Raspberry Pi.

How to turn on/off the pi

```bash
sudo halt
sudo reboot
```

Install these


```bash
xclip allows you to copy + paste from command line
sudo apt-get install xclip 
```

### Updating

```
# download the package lists from repositories and "updates" them to get
# information on the newest versions
sudo apt-get update
# upgrade your packages
sudo apt-get upgrade
# upgrade your distribution
sudo apt-get dist-upgrade
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

 
