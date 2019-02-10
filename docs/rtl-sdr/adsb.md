# ADS-B

* <strong>ADS-B (Automatic Dependent Surveillance-Broadcast)</strong> - modern aircraft have a transponder which broadcasts (at 1090Mhz frequency) location and altitude to air traffic controllers
* We can get this via RTL-SDR

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
  * [SMA Lightning Arrestor Surge Protector SMA Male to SMA Female](https://www.amazon.com/dp/B07K25Y1JW/)
  * Another (less likely) option is a surge protector the N-Type cable - [Lightning arrestor N Female to Female 50 Ohm Lightning Surge Protector](https://www.amazon.com/dp/B0751CCQN7/)
    * or combine the N-cable to the surge protector: [400-Series N-Male to N-Male In-Line Lightning Protector Cable Assemblies](http://www.l-com.com/surge-protector-400-series-n-male-to-n-male-in-line-lightning-protector-cable-assemblies)
    * In which case, get an N-Male to N-SMA adapter. Options: [JEFA Tech Adapter](https://www.amazon.com/dp/B001GUSCH6/) | [Phonetone N male to SMA female](https://www.amazon.com/dp/B00KL6PXMI/)
* Antenna Mounting assembly
  * [CHANNEL MASTER CM-3090 Universal J-Mount](https://www.amazon.com/dp/B000BSIABM) - antenna mount along fascia of house
  * [Everbilt 1-3/4 in. Stainless-Steel Clamp](https://www.homedepot.com/p/202309386) - to manage wires on mast - $1.10 each
  * [10 Gauge Copper ground wire](https://www.amazon.com/dp/B008OILG5I)

* [FlightAware 1090 MHz ADS-B Antenna](https://www.amazon.com/dp/B00WZL6WPO/) - $40

## Sources

* [ADS-B FlightAware Enclosure Build](https://imgur.com/gallery/dpyGo) - and [reddit discussion](https://www.reddit.com/r/RTLSDR/comments/7pkso6/)

