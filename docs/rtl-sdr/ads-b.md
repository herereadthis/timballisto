# ADS-B

* <strong>ADS-B (Automatic Dependent Surveillance-Broadcast)</strong> - modern aircraft have a transponder which broadcasts (at 1090Mhz frequency) location and altitude to air traffic controllers
* We can get this via RTL-SDR

### Repositories

* [ADS-B Exchange](https://github.com/jprochazka/adsb-exchange)
* [ADS-B Receiver](https://github.com/jprochazka/adsb-receiver)
* [PiAware](https://github.com/flightaware/piaware)

### Installation

* <em>(Up-to-date as of 2019-02-19)</em>
* Have a Raspberry Pi ready with Raspbian Stretch Lite
  ```bash
  wget -S https://downloads.raspberrypi.org/raspbian_lite_latest -O raspbian.zip

### potential shopping list

* The basic flow is:
  * power + ethernet > Raspberry Pi > USB extension cable > RTL-SDR dongle - grounding block / surge protector > antenna cable > antenna
* Any price listed was accurate at time of writing. Who knows now?

* (Optional) A POE Switch
  * [TRENDnet 4xPoE+ / 2xNon Switch, 60W](https://www.amazon.com/dp/B0152WZRBM/) - Amazon, $38
  * POE splitter, multiple options:
    [UCTRONICS Micro USB PoE Splitter](https://www.amazon.com/dp/B01MDLUSE7/) |
    [ANVISION 2-Pack 5V 2.4A PoE Splitter](https://www.amazon.com/dp/B079D5452Z/) |
    [PLUSPOE Micro USB PoE Splitter ](https://www.amazon.com/dp/B075CQRX2H/)
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

* [FlightAware 1090 MHz ADS-B Antenna](https://www.amazon.com/dp/B00WZL6WPO/) - $40

## Sources

* [ADS-B FlightAware Enclosure Build](https://imgur.com/gallery/dpyGo) - and [reddit discussion](https://www.reddit.com/r/RTLSDR/comments/7pkso6/)
* [My ADS-B Setup - PiAware](https://www.reddit.com/r/ADSB/comments/akk01c/)
* [Do you want to build your own FlightAware PiAware ADS-B Ground Station?](https://flightaware.com/adsb/piaware/build)

