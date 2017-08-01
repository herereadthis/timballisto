# RTL-SDR

SDR is software-defined radio. We are going to get radio signals, and then use the Raspberry Pi to interpret the signals.

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
run_gqrx.sh
```
## Radio Spectrum

The RTL-SDR dongles have a maximum range of about 20 MHz to 2 GHz so we are only focus on those frequencies.

<table>
    <thead>
        <tr>
            <th>Band Name</th>
            <th>Abbreviation</th>
            <th>ITU Band</th>
            <th>Frequency</th>
            <th>Wavelength</th>
            <th>Example Usage</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>[High Frequency](#High-Frequency)</td>
            <td>HF</td>
            <td>7</td>
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
            <td>[Very High Frequency](#Very-High-Frequency)</td>
            <td>VHF</td>
            <td>8</td>
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
            <td>[Ultra High Frequency](#Ultra-High-Frequency)</td>
            <td>UHF</td>
            <td>9</td>
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