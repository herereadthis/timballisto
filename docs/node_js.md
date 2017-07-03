# NodeJS and NPM

You can't just install Node like on anything else. Raspberry Pi  uses ARM. Instructions extended from [raspberrypi.stackexchange.com](https://raspberrypi.stackexchange.com/questions/48303/install-nodejs-for-all-raspberry-pi)

```bash
# get CPU info, note the output for "model name" is ARMv7
cat /proc/cpuinfo
```

## Downloading

Latest version is available at [nodejs.org/en/download](https://nodejs.org/en/download/). Under the section "Linux Binaries (ARM)", get the version for `ARMv7`.

```bash
# Latest version as of 2017-07-01 is 6.11.0 - download
cd ~
wget https://nodejs.org/dist/v6.11.0/node-v6.11.0-linux-armv7l.tar.gz

# Open the download
tar -xzf node-v6.11.0-linux-armv7l.tar.gz

# Confirm the download
node-v6.11.0-linux-armv7l/bin/node -v

# Copy the download to /ur/local
cd node-v6.11.0-linux-armv7l/
sudo cp -R * /usr/local/

# Add to PATH
export PATH=$PATH:/usr/local/bin

# Test installation
node -v
npm -v

# Make sure that PATH is in .bashrc or .bash_aliases
PATH=$PATH:/usr/local/bin
```
