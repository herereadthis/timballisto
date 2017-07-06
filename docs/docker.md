# Docker on Raspberry Pi

* There's a sample Docker repository at [hereradthis/raspberry-pi-hello-world](https://hub.docker.com/r/herereadthis/raspberry-pi-hello-world/).

### What is Docker?

* Docker packages an application into an isolated “container,” with libaries and settings, but without a full operating system, unlike a virtual machine (VM). Things stay lightweight.
* Docker prevents those “works on my machine” problems when working with application environemnts.
* Portability means the application can be moved from any machine to a VM, server, or cloud.

### Terms


* An **image** is a standalone package of software that includes everything needed to run it (e.g. code, runtime, libraries, env variables, config)
* An **container** is a runtime instance of an image - what the image becomes in memory when it is executed.
* A **service** is a piece of the app that runs an image in a specific way.


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

# The standard documentation says to run this:
docker run hello-world
# but it will fail with this output:
standard_init_linux.go:178: exec user process caused "exec format error"
# The problem is hello-world is an image for Intel x86_64 processors

# Test for Pi ARM 
docker run herereadthis/raspberry-pi-hello-world

```

### Commands

```bash
# Login
docker login

# Check version
docker --version

# list the images you've downloaded or ran
docker images
```