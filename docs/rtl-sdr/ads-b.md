# ADS-B

* <strong>ADS-B (Automatic Dependent Surveillance-Broadcast)</strong> - modern aircraft have a transponder which broadcasts (at 1090Mhz frequency) location and altitude to air traffic controllers
* We can get this via RTL-SDR


### Is my dongle working?

```bash
sudo apt-get install rtl-sdr
rtl_test -t
# If you see this error
# usb_open error -3
# Please fix the device permissions, e.g. by installing the udev rules file rtl-sdr.rules
sudo wget -O /etc/udev/rules.d/rtl-sdr.rules "https://raw.githubusercontent.com/osmocom/rtl-sdr/master/rtl-sdr.rules"
```

### Basic Setup

*Mostly taken from gist: [rpi-adsb-feeder.md](https://gist.github.com/kanchudeep/2068aa149b1f787f8f77d7b785de304a)*

```bash
wget https://uk.flightaware.com/adsb/piaware/files/packages/pool/piaware/p/piaware-support/piaware-repository_7.2_all.deb
sudo dpkg --install piaware-repository_7.2_all.deb
sudo apt update
sudo apt install dump1090-fa lighttpd piaware
# check piaware at http://my_ip :8080/
```

#### piaware commands

```bash
# allow updates
sudo piaware-config allow-auto-updates yes
sudo piaware-config allow-manual-updates yes
# check config
piaware-config -showall
# Is it running?
piaware-status
systemctl status piaware
# restart piaware
sudo systemctl restart piaware
```

* Claim new client: [flightaware.com/adsb/piaware/claim](https://flightaware.com/adsb/piaware/claim)
* View your page: [https://flightaware.com/account/manage](https://flightaware.com/account/manage)

#### adsbexchange

* Steps taken from [github.com/adsbxchange/adsb-exchange](https://github.com/adsbxchange/adsb-exchange)

```bash
wget -O /tmp/axfeed.sh https://adsbexchange.com/feed.sh
sudo bash /tmp/axfeed.sh
# web interface (Go to http://my_ip/adsbx)
sudo bash /usr/local/share/adsbexchange/git/install-or-update-interface.sh
# check status
sudo systemctl status adsbexchange-feed
# restart feed
sudo systemctl restart adsbexchange-feed
# uninstall
sudo bash /usr/local/share/tar1090/uninstall.sh adsbx
```


* check feed status [adsbexchange.com/myip/](https://adsbexchange.com/myip/) | [adsbx.org/sync](http://adsbx.org/sync)

### Todo

* Take pictures of the planes that fly by [github.com/IQTLabs/SkyScan](https://github.com/IQTLabs/SkyScan)

## Archived (likely outdated) notes

### Repositories

* [ADS-B Receiver](https://github.com/jprochazka/adsb-receiver)



### potential shopping list

* The basic flow is:
  * power + ethernet > Raspberry Pi > USB extension cable > RTL-SDR dongle - grounding block / surge protector > antenna cable > antenna
* Any price listed was accurate at time of writing. Who knows now?

* Raspberry Pi 3B
* RTL-SDR Dongle: [FlightAware Pro Stick Plus ADS-B USB Receiver with Built-in Filter](https://www.amazon.com/dp/B01M7REJJW/) - $20
* The grounding block and SMA end of the antenna cable should be inside a junction box.
  * [Junction Box](https://www.amazon.com/dp/B0719TB8TM/) - various sizes and prices
  * [PG11 Waterproof Cable Glands Connectors](https://www.amazon.com/dp/B00843UH4O/) - these are for sending wires into the box
* If the cable is N-Type to N-Type:
  * Cable Option: [Times Microwave LMR400 Cable](https://www.amazon.com/dp/B01N3CA5Y7/) | [Custom Cable Connection Coaxial Cable LMR-400](https://www.amazon.com/dp/B01N4M0DMH/)
  * Surge protector: [Lightning arrestor N Female to Female 50 Ohm Lightning Surge Protector](https://www.amazon.com/dp/B0751CCQN7/)
  * Combine surge protector and cable: [400-Series N-Male to N-Male In-Line Lightning Protector Cable Assemblies](http://www.l-com.com/surge-protector-400-series-n-male-to-n-male-in-line-lightning-protector-cable-assemblies)
  * N-Male to N-SMA adapter. Options: [JEFA Tech Adapter](https://www.amazon.com/dp/B001GUSCH6/) | [Phonetone N male to SMA female](https://www.amazon.com/dp/B00KL6PXMI/)
* If the cable is N-Type to SMA:
  * Cable option: [MPD Digital LMR-400 Coaxial Antenna Cable Line with N Male & SMA Male Connectors](https://www.amazon.com/dp/B00H9II8I2/) - (1ft, can also be a jumper between n-type surge protector to dongle
  * Surge protector for the SMA end: [SMA Lightning Arrestor Surge Protector SMA Male to SMA Female](https://www.amazon.com/dp/B07K25Y1JW/)
* Antenna Mounting assembly
  * [CHANNEL MASTER CM-3090 Universal J-Mount](https://www.amazon.com/dp/B000BSIABM) - antenna mount along fascia of house
  * [Everbilt 1-3/4 in. Stainless-Steel Clamp](https://www.homedepot.com/p/202309386) - to manage wires on mast - $1.10 each
  * [10 Gauge Copper ground wire](https://www.amazon.com/dp/B008OILG5I)


## Sources

* [ADS-B FlightAware Enclosure Build](https://imgur.com/gallery/dpyGo) - and [reddit discussion](https://www.reddit.com/r/RTLSDR/comments/7pkso6/)
* [My ADS-B Setup - PiAware](https://www.reddit.com/r/ADSB/comments/akk01c/)

