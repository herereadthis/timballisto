# RTL-SDR

SDR is software-defined radio. We are going to get radio signals, and then use the Raspberry Pi to interpret the signals.

## Installation

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