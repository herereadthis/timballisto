# Hacking the Amazon Dash Button

```bash
# Install Scapy, a packet manipulation program & library
sudo pip install scapy
sudo pip3 install scapy-python3
```

## Enable the Dash button and capture MAC address

* Using your Amazon app, go to the menu > "My Account" > "Dash Buttons & Devices" > "Set a new device".
* Follow the instructions to set up a new device, and associate a product with it.
* Buy the product, in order to redeem the Dash Button purchase.
* Then, go to "Dash Buttons & Devices" > "Manage Devices" and deactivate the button.
* Instructions for Verizon Routers: Go to 191.168.1.1 on an ethernet connection and log in. Wifi will not work.
* Go to System Monitoring, then choose "Advanced Status" and accept to proceed.
* Then click on "System Logging" and note what's there.
* Enable the Dash button again, but this time do not associate the product.
* Refresh the system log. You should see something new. Note its IP address
* (If you run `nmap` you won't see that IP address because it's not currently connected.)
* From the main navigation, go to "My Network" and find the device matching the IP address from the System Log.
* Copy its MAC address. To the right of it, choose "View Device Details"
* Click the button to "Test Connectivity" and it should fail, because the Dash Button is only on when pressed.

## Capture the Dash Button MAC Address

