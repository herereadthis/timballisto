# Do these things next

The following stuff is not too important, but is worthwhile doing in order to improve usability for the Raspberry Pi.

## Set up remote access with VNC

Access the Raspberry Pi as a remote desktop, so you won&rsquo;t have to connect a monitor to it.

```bash
# install VNC
sudo apt-get install realvnc-vnc-server realvnc-vnc-viewer
# enable VNC by going into configuration > Interfaces
sudo raspi-config
# remember the IP address
hostname -i
```

* On your master computer, create a VNC account and [download VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/).
* Then in the VNC viewer type in the IP address you got earlier.
* When it prompst for username and password, it is the one to sign into the Raspberry Pi (If you haven&rsquo;t changed the username, then it is still `pi`).



## Sources

* [VNC (Virtual Network Computing)](https://www.raspberrypi.org/documentation/remote-access/vnc/) - raspberry pi foundation