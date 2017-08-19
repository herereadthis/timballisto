# RTL-SDR

RTL-SDR is a computer-based radio scanner based on the Realtek RTL2832U chipset, a DVB-T COFDM demodulator that supports USB 2.0. In other words, it is a TV tuner with which we are going to get radio signals, i.e., SDR a.k.a. "software-defined radio." We will use the Raspberry Pi to interpret the signals.

The frequency range of SDR <a href="http://osmocom.org/projects/sdr/wiki/rtl-sdr">depends on the tuner and implementation</a>.

<table>
    <thead>
        <tr>
            <td>Tuner</td>
            <td>Frequency Range</td>
            <td>Secondary Range</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Elonics E4000</td>
            <td>52–1100 MHz</td>
            <td>1250–2200 MHz</td>
        </tr>
        <tr>
            <td>Rafael Micro R820T(2)</td>
            <td>24–1766 MHz</td>
            <td></td>
        </tr>
        <tr>
            <td>Rafael Micro R828D</td>
            <td>24–1766 MHz</td>
            <td></td>
        </tr>
        <tr>
            <td>Fitipower FC0013</td>
            <td>24–1100 MHz</td>
            <td></td>
        </tr>
        <tr>
            <td>Fitipower FC0012</td>
            <td>22–948.6 MHz</td>
            <td></td>
        </tr>
        <tr>
            <td>FCI FC2580</td>
            <td>146–308 MHz</td>
            <td>438–924 MHz</td>
        </tr>
    </tbody>
</table>

## Installation

### Pre-Install

```bash
# Qt is a cross-platform C++ application framework: provides GUI functionality

# QT 5 Core module - contains core non-GUI functionality
sudo apt-get install -y libqt5core5a

# Qt 5 GUI module - extends QtCore with GUI functionality
sudo apt-get install -y libqt5gui5

# Qt 5 network module - offers classes to write TCP/IP clients and servers
sudo apt-get install -ylibqt5network5

# Qt 5 widgets module - extends QtGui with C++ widget functionality
sudo apt-get install -y libqt5widgets5

# Qt 5 SVG module - classes for displaying the contents of SVG files
sudo apt-get install -y libqt5svg5

# Portable audio I/O - shared library/ cross-platform support of audio
sudo apt-get install -y libportaudio2

# all together
sudo apt-get install libqt5gui5 libqt5core5a libqt5network5 libqt5widgets5 libqt5svg5 libportaudio2
```

### Install Gqrx SDR

```bash
# Latest Releases at https://github.com/csete/gqrx/releases
# v2.6.1 as of 2017-02-16
cd ~/PATH/TO/REPOS
wget https://github.com/csete/gqrx/releases/download/v2.6/gqrx-2.6-rpi3-2.tar.xz
tar xvf gqrx-2.6-rpi3-2.tar.xz
cd gqrx-2.6-rpi3-2
./setup_gqrx.sh

# Run the application
./run_gqrx.sh
```

#### Startup

The first window you see will be Configure I/O devices.

* I/Q input
  * **Device**: use “Realtek RTL2838” if you are using an RTL-SDR dongle
  * **Device String**: “rtl=0”
  * **Input rate**: “2400000”

Then press play. At the top is the frequency to which you are currently tuned. Below that is a display of the FFT RF spectrum surrounding that frequency. and a waterfall display capturing the history of that RF spectrum.

* FFT: Fast Fourier Transform, something to decompose the waveform

#### Input Controls

* **LNB LO** (Local Oscillator Frequency) - Set to 0. Use this if you are using an up or down-converter before the SDR device
* **Hardware AGC** (Automatic Gain Control) - Toggle Off. Doesn't really make much of a difference on an RPi 
* **Swap I/Q** (swap I and Q Channels) - Toggle Off
* **No Limits** (allow tuning beyond RTL-SDR recommended frequencies ) - Toggle Off
* **DC remove** (remove DC bias) - Toggle Off
* **IQ balance** - Toggle Off
* **Freq. correction** - Use if there is a drift between the frequency setting and actual frequency
* **Antenna** - set to “RX” receive

#### FFT Settings

#### Receiver Options


### Install Dump 1090

Automatic dependent surveillance – broadcast (ADS–B) is communication operating on 1090 MHz which gives an aircraft's location and speed, to be shared with air traffic controls (ATC) for tracking.

```bash
# Install Dump 1090
git clone git://github.com/antirez/dump1090.git
cd dump1090/
make

# Run
./dump1090 --interactive

# Run while displayed on a google map
./dump1090 --interactive --net
# open localhost:8080
```

## Radio Spectrum

The SDR dongles have a maximum range of about 500 Khz –1800 MHz so we are only going to focus on those frequencies.

<table>
    <thead>
        <tr>
            <th>Band Name</th>
            <th>Frequency</th>
            <th>Wavelength</th>
            <th>Example Usage</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">
                <strong><a href="#user-content-medium-frequency">Medium Frequency</a></strong>
                <br />HF
            </td>
            <td>300–3000 KHz</td>
            <td>1000 m – 100 m</td>
            <td>
                <ul>
                    <li>AM Broadcasts</li>
                    <li>Amateur radio</li>
                    <li>Avalanche beacons</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td align="center">
                <strong><a href="#user-content-high-frequency">High Frequency</a></strong>
                <br />HF
            </td>
            <td>3–30 MHz</td>
            <td>100 m – 10 m</td>
            <td>
                <ul>
                    <li>Shortwave broadcasts</li>
                    <li>Citizens' band radio</li>
                    <li>Amateur radio</li>
                    <li>Over-the-horizon aviation communications</li>
                    <li>RFID</li>
                    <li>Over-the-horizon radar</li>
                    <li>ALE (Automatic Link Establishment) HF radio</li>
                    <li>NVIS (Near vertical incidence skywave)</li>
                    <li>Marine and mobile radio telephony</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td align="center">
                <strong><a href="#user-content-very-high-frequency">Very High Frequency</a></strong>
                <br />VHF
            </td>
            <td>30–300 MHz</td>
            <td>10 m – 1 m</td>
            <td>
                <ul>
                    <li>FM radio</li>
                    <li>TV broadcasts</li>
                    <li>Line-of-sight aircraft communication</li>
                    <li>Land mobile and maritime mobile</li>
                    <li>Amateur radio</li>
                    <li>Weather radio</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td align="center">
                <strong><a href="#user-content-ultra-high-frequency">Ultra High Frequency</a></strong>
                <br />UHF
            </td>
            <td>300–3000 MHz</td>
            <td>100 cm – 10 cm</td>
            <td>
                <ul>
                    <li>TV broadcasts</li>
                    <li>Microwave ovens/devices/communications</li>
                    <li>Radio Astronomy</li>
                    <li>Mobile Phones</li>
                    <li>Wireless LAN, Bluetooth, Zigbee</li>
                    <li>GPS</li>
                    <li>2-way radios (e.g. walkie talkies)</li>
                    <li>Amateur radio</li>
                    <li>Satellite radio</li>
                    <li>Remote control systems</li>
                    <li>ADSB (air traffic positioning)</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

### Medium Frequency



### High Frequency

* Known as "decameter band" and shortwave radio
* Waves in this band can be reflected back to earth by the ionosphere, so can be used for intercontinental communications
* Noise from electrical equipment has a great effect.

### Very High Frequency

* Waves are restricted to radio horizon, so less than 100 miles.
* Less affected by atmospheric noise and interference from electrical equipment
* Blocked by hills and mountains but less affected by buildings

### Ultra High Frequency

* Known as "decimeter band"
* Propagate by line-of-site propagation (LOS) so it can blocked by hills and large buildings, but not necessarily through walls
* Signals can be degraded by atmospheric moisture

## Hardware considerations

### Impedence

* SDR dongles will typically have an impedence of 75 Ohms, but any mismatch between 50 Ohm cables and the receiver will be minimal because we are not transmitting.

## Antennas

<table>
    <thead>
        <tr>
            <td>Usage</td>
            <td>Frequency</td>
            <td>1/1 λ</td>
            <td>1/4 λ</td>
            <td>1/2 λ</td>
            <td>5/8 λ</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>KIB229</td>
            <td>45.08 MHz</td>
            <td align="right"><code>340.3 cm</code></td>
            <td align="right"><code>85.1 cm</code></td>
            <td align="right"><code>170.1 cm</code></td>
            <td align="right"><code>212.7 cm</code></td>
        </tr>
        <tr>
            <td>FM Radio</td>
            <td>88.1 MHz</td>
            <td align="right"><code>340.3 cm</code></td>
            <td align="right"><code>85.1 cm</code></td>
            <td align="right"><code>170.1 cm</code></td>
            <td align="right"><code>212.7 cm</code></td>
        </tr>
        <tr>
            <td>FM Radio</td>
            <td>90 MHz</td>
            <td align="right"><code>333.1 cm</code></td>
            <td align="right"><code>83.3 cm</code></td>
            <td align="right"><code>166.5 cm</code></td>
            <td align="right"><code>208.2 cm</code></td>
        </tr>
        <tr>
            <td>FM Radio</td>
            <td>92.5 MHz</td>
            <td align="right"><code>324.1 cm</code></td>
            <td align="right"><code>81.0 cm</code></td>
            <td align="right"><code>162.0 cm</code></td>
            <td align="right"><code>202.6 cm</code></td>
        </tr>
        <tr>
            <td>FM Radio</td>
            <td>95 MHz</td>
            <td align="right"><code>315.6 cm</code></td>
            <td align="right"><code>78.9 cm</code></td>
            <td align="right"><code>157.8 cm</code></td>
            <td align="right"><code>197.2 cm</code></td>
        </tr>
        <tr>
            <td>FM Radio</td>
            <td>97.5 MHz</td>
            <td align="right"><code>307.5 cm</code></td>
            <td align="right"><code>76.9 cm</code></td>
            <td align="right"><code>153.7 cm</code></td>
            <td align="right"><code>192.2 cm</code></td>
        </tr>
        <tr>
            <td>FM Radio</td>
            <td>100 MHz</td>
            <td align="right"><code>299.8 cm</code></td>
            <td align="right"><code>74.9 cm</code></td>
            <td align="right"><code>149.9 cm</code></td>
            <td align="right"><code>187.4 cm</code></td>
        </tr>
        <tr>
            <td>FM Radio</td>
            <td>102.5 MHz</td>
            <td align="right"><code>292.5 cm</code></td>
            <td align="right"><code>73.1 cm</code></td>
            <td align="right"><code>146.2 cm</code></td>
            <td align="right"><code>182.8 cm</code></td>
        </tr>
        <tr>
            <td>FM Radio</td>
            <td>105 MHz</td>
            <td align="right"><code>285.5 cm</code></td>
            <td align="right"><code>71.4 cm</code></td>
            <td align="right"><code>142.8 cm</code></td>
            <td align="right"><code>173.7 cm</code></td>
        </tr>
        <tr>
            <td>FM Radio</td>
            <td>107.9 MHz</td>
            <td align="right"><code>277.8 cm</code></td>
            <td align="right"><code>69.5 cm</code></td>
            <td align="right"><code>138.9 cm</code></td>
            <td align="right"><code>173.7 cm</code></td>
        </tr>
        <tr>
            <td><a href="http://www.airnav.com/airport/DCA">DCA UNICOM</a></td>
            <td>122.95 MHz</td>
            <td align="right"><code>243.8 cm</code></td>
            <td align="right"><code>61.0 cm</code></td>
            <td align="right"><code>121.9 cm</code></td>
            <td align="right"><code>152.4 cm</code></td>
        </tr>
        <tr>
            <td><a href="http://en.wikipedia.org/wiki/Aircraft_Communications_Addressing_and_Reporting_System">ACARS</a></td>
            <td>131.550 MHz</td>
            <td align="right"><code>227.9 cm</code></td>
            <td align="right"><code>57.0 cm</code></td>
            <td align="right"><code>113.9 cm</code></td>
            <td align="right"><code>142.4 cm</code></td>
        </tr>
        <tr>
            <td><a href="http://www.ospo.noaa.gov/Operations/POES/status.html#noaa19">NOAA-19</a></td>
            <td>137.1 MHz</td>
            <td align="right"><code>217.4 cm</code></td>
            <td align="right"><code>54.7 cm</code></td>
            <td align="right"><code>109.3 cm</code></td>
            <td align="right"><code>136.7 cm</code></td>
        </tr>
        <tr>
            <td><a href="http://www.ospo.noaa.gov/Operations/POES/status.html#noaa15">NOAA-15</a></td>
            <td>137.62 MHz</td>
            <td align="right"><code>218.8 cm</code></td>
            <td align="right"><code>54.5 cm</code></td>
            <td align="right"><code>108.9 cm</code></td>
            <td align="right"><code>136.2 cm</code></td>
        </tr>
        <tr>
            <td><a href="http://www.ospo.noaa.gov/Operations/POES/status.html#noaa18">NOAA-18</a></td>
            <td>137.9125 MHz</td>
            <td align="right"><code>218.8 cm</code></td>
            <td align="right"><code>54.3 cm</code></td>
            <td align="right"><code>108.7 cm</code></td>
            <td align="right"><code>135.9 cm</code></td>
        </tr>
        <tr>
            <td><a href="http://www.nvfma.org/">NV4FM Repeater</a></td>
            <td>146.91 MHz</td>
            <td align="right"><code>204.1 cm</code></td>
            <td align="right"><code>51.0 cm</code></td>
            <td align="right"><code>102.0 cm</code></td>
            <td align="right"><code>127.5 cm</code></td>
        </tr>
        <tr>
            <td><a href="https://one-button.org/node/48">NOAA NWR</a> <a href="http://www.nws.noaa.gov/nwr/coverage/site2.php?State=DC&Site=WNG736">DC</a></td>
            <td>162.450 MHz</td>
            <td align="right"><code>218.8 cm</code></td>
            <td align="right"><code>54.7 cm</code></td>
            <td align="right"><code>109.5 cm</code></td>
            <td align="right"><code>115.3 cm</code></td>
        </tr>
        <tr>
            <td>70 cm band (low)</td>
            <td>420 MHz</td>
            <td align="right"><code>71.4 cm</code></td>
            <td align="right"><code>17.8 cm</code></td>
            <td align="right"><code>35.7 cm</code></td>
            <td align="right"><code>136.8 cm</code></td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/LPD433">LPD433 ch.01</a></td>
            <td>433.075 MHz</td>
            <td align="right"><code>69.2 cm</code></td>
            <td align="right"><code>17.3 cm</code></td>
            <td align="right"><code>34.6 cm</code></td>
            <td align="right"><code>43.3 cm</code></td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/LPD433">LPD433 ch.30</a></td>
            <td>433.800 MHz</td>
            <td align="right"><code>69.1 cm</code></td>
            <td align="right"><code>17.3 cm</code></td>
            <td align="right"><code>34.6 cm</code></td>
            <td align="right"><code>43.2 cm</code></td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/LPD433">LPD433 ch.69</a></td>
            <td>434.775 MHz</td>
            <td align="right"><code>68.9 cm</code></td>
            <td align="right"><code>17.2 cm</code></td>
            <td align="right"><code>34.5 cm</code></td>
            <td align="right"><code>43.1 cm</code></td>
        </tr>
        <tr>
            <td><a href="http://www.nvfma.org/">NV4FM Repeater</a></td>
            <td>447.025 MHz</td>
            <td align="right"><code>67.1 cm</code></td>
            <td align="right"><code>16.8 cm</code></td>
            <td align="right"><code>33.5 cm</code></td>
            <td align="right"><code>41.9 cm</code></td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/Family_Radio_Service">FRS ch.01</a></td>
            <td>462.5625 MHz</td>
            <td align="right"><code>64.8 cm</code></td>
            <td align="right"><code>16.2 cm</code></td>
            <td align="right"><code>32.4 cm</code></td>
            <td align="right"><code>40.6 cm</code></td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/Family_Radio_Service">FRS ch.14</a></td>
            <td>467.7125 MHz</td>
            <td align="right"><code>64.1 cm</code></td>
            <td align="right"><code>16.0 cm</code></td>
            <td align="right"><code>32.0 cm</code></td>
            <td align="right"><code>40.1 cm</code></td>
        </tr>
        <tr>
            <td>70 cm band (high)</td>
            <td>450 MHz</td>
            <td align="right"><code>66.6 cm</code></td>
            <td align="right"><code>16.7 cm</code></td>
            <td align="right"><code>33.3 cm</code></td>
            <td align="right"><code>41.6 cm</code></td>
        </tr>
        <tr>
            <td><a href="https://www.faa.gov/nextgen/programs/adsb/">ADS-B</a></td>
            <td>1090 MHz</td>
            <td align="right"><code>27.50 cm</code></td>
            <td align="right"><code>6.86 cm</code></td>
            <td align="right"><code>13.75 cm</code></td>
            <td align="right"><code>17.19 cm</code></td>
        </tr>
    </tbody>
</table>

* [Ham Repeater Book](https://www.repeaterbook.com/repeaters/index.php?state_id=none)
* [Radio Reference Frequency Database](https://www.radioreference.com/apps/db/)
* [SDR Signal Identification Guide](http://www.sigidwiki.com/wiki/Signal_Identification_Guide)
* [Reducing noise from USB extension cables](http://www.radioforeveryone.com/p/reducing-electrical-noise.html)
* [Wavelength Frequency Calculator](http://www.procato.com/calculator-wavelength-frequency/)

