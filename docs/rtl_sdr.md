# RTL-SDR

RTL-SDR is software-defined radio using a DVB-TV tuner based on the RTL2832U chipset. We are going to get radio signals, and then use the Raspberry Pi to interpret the signals.

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
## Radio Spectrum

The SDR dongles have a maximum range of about 20–1800 MHz so we are only going to focus on those frequencies.

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
                <strong><a href="#user-content-high-frequency">High Frequency</a></strong>
                <br />HF
            </td>
            <td>3–30 MHz</td>
            <td>100 m – 10 m</td>
            <td>
                <ul>
                    <li>Shortwave broadcasts</li>
                    <li>Citizens' band radio,</li>
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
            <td>1 m – 100 mm</td>
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
            <td>usage</td>
            <td>Frequency</td>
            <td>Wavelenth</td>
            <td>1/4 Wave</td>
            <td>1/2 Wave</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>FM Radio</td>
            <td>88.1 Mhz</td>
            <td align="right"><code>340.3 cm</code></td>
            <td align="right"><code>85.1 cm</code></td>
            <td align="right"><code>170.1 cm</code></td>
        </tr>
        <tr>
            <td>FM Radio</td>
            <td>90 Mhz</td>
            <td align="right"><code>333.1 cm</code></td>
            <td align="right"><code>83.3 cm</code></td>
            <td align="right"><code>166.5 cm</code></td>
        </tr>
        <tr>
            <td>FM Radio</td>
            <td>95 Mhz</td>
            <td align="right"><code>315.6 cm</code></td>
            <td align="right"><code>78.9 cm</code></td>
            <td align="right"><code>157.8 cm</code></td>
        </tr>
        <tr>
            <td>FM Radio</td>
            <td>97.5 Mhz</td>
            <td align="right"><code>307.5 cm</code></td>
            <td align="right"><code>76.9 cm</code></td>
            <td align="right"><code>153.7 cm</code></td>
        </tr>
        <tr>
            <td>FM Radio</td>
            <td>100 Mhz</td>
            <td align="right"><code>299.8 cm</code></td>
            <td align="right"><code>74.9 cm</code></td>
            <td align="right"><code>149.9 cm</code></td>
        </tr>
        <tr>
            <td>FM Radio</td>
            <td>102.5 Mhz</td>
            <td align="right"><code>292.5 cm</code></td>
            <td align="right"><code>73.1 cm</code></td>
            <td align="right"><code>146.2 cm</code></td>
        </tr>
        <tr>
            <td>FM Radio</td>
            <td>105 Mhz</td>
            <td align="right"><code>285.5 cm</code></td>
            <td align="right"><code>71.4 cm</code></td>
            <td align="right"><code>142.8 cm</code></td>
        </tr>
        <tr>
            <td>FM Radio</td>
            <td>107.9 Mhz</td>
            <td align="right"><code>277.8 cm</code></td>
            <td align="right"><code>69.5 cm</code></td>
            <td align="right"><code>138.9 cm</code></td>
        </tr>
        <tr>
            <td><a href="http://www.airnav.com/airport/DCA">DCA UNICOM</a></td>
            <td>122.95 Mhz</td>
            <td align="right"><code>243.8 cm</code></td>
            <td align="right"><code>61.0 cm</code></td>
            <td align="right"><code>121.9 cm</code></td>
        </tr>
        <tr>
            <td>NOAA</td>
            <td>137 Mhz</td>
            <td align="right"><code>218.8 cm</code></td>
            <td align="right"><code>54.7 cm</code></td>
            <td align="right"><code>109.5 cm</code></td>
        </tr>
        <tr>
            <td></td>
            <td>420 Mhz</td>
            <td align="right"><code>71.4 cm</code></td>
            <td align="right"><code>17.8 cm</code></td>
            <td align="right"><code>35.7 cm</code></td>
        </tr>
        <tr>
            <td></td>
            <td>433 Mhz</td>
            <td align="right"><code>69.2 cm</code></td>
            <td align="right"><code>17.3 cm</code></td>
            <td align="right"><code>34.6 cm</code></td>
        </tr>
        <tr>
            <td></td>
            <td>450 Mhz</td>
            <td align="right"><code>66.6 cm</code></td>
            <td align="right"><code>16.7 cm</code></td>
            <td align="right"><code>33.3 cm</code></td>
        </tr>
        <tr>
            <td>ADS-B</td>
            <td>1090 MHz</td>
            <td align="right"><code>27.50 cm</code></td>
            <td align="right"><code>6.86 cm</code></td>
            <td align="right"><code>13.75 cm</code></td>
        </tr>
    </tbody>
</table>
