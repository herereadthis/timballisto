# Docker on Raspberry Pi

### What is Docker?

* Docker packages an application into an isolated “container,” with libaries and settings, but without a full operating system, unlike a virtual machine (VM). Things stay lightweight.
* Docker prevents those “works on my machine” problems when working with application environemnts.
* Portability means the application can be moved from any machine to a VM, server, or cloud.

### Terms


* An **image** is a standalone package of software that includes everything needed to run it (e.g. code, runtime, libraries, env variables, config)
* An **container** is a runtime instance of an image - what the image becomes in memory when it is executed. 


### Installation

```bash
# this will copy relevant Docker binaries into /usr/bin/
curl -sSL get.docker.com | sh

# Set Docker to auto-start
sudo systemctl enable docker

# Or start the Docker daeon with
sudo systemctl start docker

# Enable Docker client to be used by root user
sudo usermod -aG docker pi
```