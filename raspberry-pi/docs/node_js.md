# NodeJS and NPM

You can't just install Node like on anything else. Raspberry Pi  uses ARM. Instructions extended from [raspberrypi.stackexchange.com](https://raspberrypi.stackexchange.com/questions/48303/install-nodejs-for-all-raspberry-pi)

```bash
# get CPU info, note the output for "model name" is ARMv7
cat /proc/cpuinfo
```

## Downloading

Latest version is available at [nodejs.org/en/download](https://nodejs.org/en/download/). Under the section "Linux Binaries (ARM)", get the version for `ARMv7`.

All of the following is part of the [node_install.sh](https://github.com/herereadthis/lutra/blob/master/resources/install_scripts/node_install.sh) script.

```bash
cd lutra/resources
./node_install.sh
```

```bash
# Latest version as of 2017-09-21 is 6.11.3 - download
cd ~
wget https://nodejs.org/dist/v6.11.3/node-v6.11.3-linux-armv7l.tar.xz

# Extract the download
tar xf node-v6.11.3-linux-armv7l.tar.xz

# Confirm the download
node-v6.11.3-linux-armv7l/bin/node -v

# Copy the download to /ur/local
cd node-v6.11.3-linux-armv7l/
sudo cp -R * /usr/local/

# Clean up
cd ~
rm -rf node-v6.11.0*

# Add to PATH
export PATH=$PATH:/usr/local/bin

# Test installation
node -v
npm -v

# Make sure that PATH is in .bashrc or .bash_aliases
PATH=$PATH:/usr/local/bin

# start node REPL
node

# Test by getting the date
new Date()
```
