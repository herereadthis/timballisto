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
            <td>Quarter Wave</td>
            <td>Half Wave</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td></td>
            <td>24.89-24.99 MHz</td>
            <td>12 Meters</td>
            <td>asdf</td>
            <td>asdf</td>
        </tr>
        <tr>
            <td>FM Radio</td>
            <td>95 Mhz</td>
            <td>315 cm</td>
            <td>78.9 cm</td>
            <td>158 cm</td>
        </tr>
        <tr>
            <td>FM Radio</td>
            <td>100 Mhz</td>
            <td>300 cm</td>
            <td>74.9 cm</td>
            <td>150 m</td>
        </tr>
        <tr>
            <td>NOAA</td>
            <td>137 Mhz</td>
            <td>219 cm</td>
            <td>54.7 cm</td>
            <td>109 cm</td>
        </tr>
        <tr>
            <td></td>
            <td>420-450 MHz</td>
            <td>70 cm</td>
            <td>17.5 cm</td>
            <td>35 cm</td>
        </tr>
        <tr>
            <td>ADS-B</td>
            <td>1090 MHz</td>
            <td>27.5 cm</td>
            <td>6.5 cm</td>
            <td>13.8 cm</td>
        </tr>
    </tbody>
</table>
