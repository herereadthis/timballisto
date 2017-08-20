# GPIO

Rasberry Pi 3 Pinout - here are the GPIO (General Purpose Input/Output)

Wiring: [Link 1](https://www.youtube.com/watch?v=AbCuPrYhETw), [link 2](https://bitbucket.org/jschick/tft_st7735/src/a4ad4cc94d6a4a6e6c8be0c3ccdd4370564f9b83/wiring.txt)

https://www.youtube.com/watch?v=fdaCSBbm35c

<table>
    <tbody>
        <tr>
            <td colspan="2"></td>
            <td align="right"><strong>3.3V</strong></td>
            <td align="right">01</td>
            <td rowspan="20"></td>
            <td rowspan="20"></td>
            <td>02</td>
            <td><strong>5.0V</strong></td>
            <td colspan="2" rowspan="3"></td>
        </tr>
        <tr>
            <td align="right" rowspan="2">I<sup>2</sup>C</td>
            <td align="right">SDA</td>
            <td align="right"><strong>02</strong></td>
            <td>03</td>
            <td>04</td>
            <td><strong>5.0V</strong></td>
        </tr>
        <tr>
            <td align="right">SCL</td>
            <td align="right"><strong>03</strong></td>
            <td>05</td>
            <td>06</td>
            <td><strong>GND</strong></td>
        </tr>
        <tr>
            <td colspan="2" align="right">W1</td>
            <td align="right"><strong>04</strong></td>
            <td>07</td>
            <td>08</td>
            <td><strong>14</strong></td>
            <td>TXD</td>
            <td rowspan="2">UART</td>
        </tr>
        <tr>
            <td colspan="2" rowspan="5"></td>
            <td align="right"><strong>GND</strong></td>
            <td>09</td>
            <td>10</td>
            <td><strong>15</strong></td>
            <td>RXD</td>
        </tr>
        <tr>
            <td align="right"><strong>17</strong></td>
            <td>11</td>
            <td>12</td>
            <td><strong>18</strong></td>
            <td>CLK</td>
            <td>PCM</td>
        </tr>
        <tr>
            <td align="right"><strong>27</strong></td>
            <td>13</td>
            <td>14</td>
            <td><strong>GND</strong></td>
            <td colspan="2" rowspan="5"></td>
        </tr>
        <tr>
            <td align="right"><strong>22</strong></td>
            <td>15</td>
            <td>16</td>
            <td><strong>23</strong></td>
        </tr>
        <tr>
            <td align="right"><strong>3.3V</strong></td>
            <td>17</td>
            <td>18</td>
            <td><strong>24</strong></td>
        </tr>
        <tr>
            <td align="right" rowspan="3">SPI</td>
            <td align="right">MOSI</td>
            <td align="right"><strong>10</strong></td>
            <td>19</td>
            <td>20</td>
            <td><strong>GND</strong></td>
        </tr>
        <tr>
            <td align="right">MISO</td>
            <td align="right"><strong>09</strong></td>
            <td>21</td>
            <td>22</td>
            <td><strong>25</strong></td>
        </tr>
        <tr>
            <td align="right">SCLK</td>
            <td align="right"><strong>11</strong></td>
            <td>23</td>
            <td>24</td>
            <td><strong>08</strong></td>
            <td>CE0</td>
            <td rowspan="2">SPI</td>
        </tr>
        <tr>
            <td colspan="2" rowspan="5"></td>
            <td align="right"><strong>GND</strong></td>
            <td>25</td>
            <td>26</td>
            <td><strong>07</strong></td>
            <td>CE1</td>
        </tr>
        <tr>
            <td align="right"><strong>ID SD</strong></td>
            <td>27</td>
            <td>28</td>
            <td><strong>ID SC</strong></td>
            <td colspan="2" rowspan="5"></td>
        </tr>
        <tr>
            <td align="right"><strong>05</strong></td>
            <td>29</td>
            <td>30</td>
            <td><strong>GND</strong></td>
        </tr>
        <tr>
            <td align="right"><strong>06</strong></td>
            <td>31</td>
            <td>32</td>
            <td><strong>12</strong></td>
        </tr>
        <tr>
            <td align="right"><strong>13</strong></td>
            <td>33</td>
            <td>34</td>
            <td><strong>GND</strong></td>
        </tr>
        <tr>
            <td align="right">PCM</td>
            <td align="right">FS</td>
            <td align="right"><strong>19</strong></td>
            <td>35</td>
            <td>36</td>
            <td><strong>16</strong></td>
        </tr>
        <tr>
            <td align="right" colspan="2" rowspan="2"></td>
            <td align="right"><strong>26</strong></td>
            <td>37</td>
            <td>38</td>
            <td><strong>20</strong></td>
            <td>D<sub>IN</sub></td>
            <td rowspan="2">PCM</td>
        </tr>
        <tr>
            <td align="right"><strong>GND</strong></td>
            <td>39</td>
            <td>40</td>
            <td><strong>21</strong></td>
            <td>D<sub>OUT</sub></td>
        </tr>
    </tbody>
</table>

More information avalable at [pinout.xyz](https://pinout.xyz/pinout/)

### I<sup>2</sup>C - Inter Integrated Circuit

* Pins: `GPIO2` (#3) and `GPIO3` (#5)
* I<sup>2</sup>C allows data exchange between microcontrollers and peripherals with a minimum of wiring

### W1 - 1-Wire

* Pin: `GPIO4` (#7)
* 1-wire is a device communication data bus system, developed by Dallas Semiconductor.
* It provides low speed data, signalling and power over a single signal wire.

### UART 0 Universal Asynchronous Receiver/Transmitter

* Pins: `GPIO2` (#8) and `GPIO3` (#10)
* UART is an asynchronous serial communication protocol, meaning that it takes bytes of data and transmits the individual bits in a sequential fashion.

### SPI - Serial Peripheral Interface

* Pins: `GPIO10` (#19), `GPIO9` (#21), `GPIO11` (#23), `GPIO8` (#24), and `GPIO7` (#26)
* The Serial Peripheral Interface(SPI) is a communication protocol to transfer data between micro-computers like the Raspberry Pi and peripheral devices. These devices may be either sensors or actuators.
* `MOSI` - `GPIO10` - Master Out, Slave In
* `MISO` - `GPIO9` - Master In, Slave Out
* `SCLK` - `GPIO11` - Serial CLocK
* `CE0` - `GPIO08` - Chip Enable
* `CE1` - `GPIO07` - Chip Enable 

### PCM - Pulse-code Modulation

* Pins: `GPIO18` (#12), `GPIO19` (#35), `GPIO38` (#37), and `GPIO21` (#40)
* PCM (Pulse-code Modulation) is a digital representation of sampled analog.



