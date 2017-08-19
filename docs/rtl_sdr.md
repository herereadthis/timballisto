# RTL-SDR

RTL-SDR is a computer-based radio scanner based on the Realtek RTL2832U chipset, a DVB-T COFDM demodulator that supports USB 2.0. In other words, it is a TV tuner with which we are going to get radio signals, i.e., SDR a.k.a. &ldquo;software-defined radio.&rdquo; We will use the Raspberry Pi to interpret the signals.

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
  * **Device**: use &ldquo;Realtek RTL2838&rdquo; if you are using an RTL-SDR dongle
  * **Device String**: &ldquo;rtl=0&rdquo;
  * **Input rate**: &ldquo;2400000&rdquo;

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
* **Antenna** - set to &ldquo;RX&rdquo; receive

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

## Resources

* [Ham Repeater Book](https://www.repeaterbook.com/repeaters/index.php?state_id=none)
* [Radio Reference Frequency Database](https://www.radioreference.com/apps/db/)
* [SDR Signal Identification Guide](http://www.sigidwiki.com/wiki/Signal_Identification_Guide)
* [Reducing noise from USB extension cables](http://www.radioforeveryone.com/p/reducing-electrical-noise.html)
* [Wavelength Frequency Calculator](http://www.procato.com/calculator-wavelength-frequency/)

