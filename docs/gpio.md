# GPIO

Rasberry Pi 3 Pinout - here are the GPIO (General Purpose Input/Output)

<table>
    <tbody>
        <tr>
            <td colspan="2"></td>
            <td>3.3V</td>
            <td>01</td>
            <td rowspan="20"></td>
            <td rowspan="20"></td>
            <td>02</td>
            <td>5.0V</td>
            <td colspan="2" rowspan="3"></td>
        </tr>
        <tr>
            <td align="right" rowspan="2">I<sup>2</sup>C</td>
            <td align="right">SDA</td>
            <td>02</td>
            <td>03</td>
            <td>04</td>
            <td>5.0V</td>
        </tr>
        <tr>
            <td align="right">SCL</td>
            <td>03</td>
            <td>05</td>
            <td>06</td>
            <td>GND</td>
        </tr>
        <tr>
            <td colspan="2" rowspan="6"></td>
            <td align="right">04</td>
            <td>07</td>
            <td>08</td>
            <td>14</td>
            <td>TXD</td>
            <td rowspan="2">UART</td>
        </tr>
        <tr>
            <td align="right">GND</td>
            <td>09</td>
            <td>10</td>
            <td>15</td>
            <td>RXD</td>
        </tr>
        <tr>
            <td align="right">17</td>
            <td>11</td>
            <td>12</td>
            <td>18</td>
            <td>CLK</td>
            <td>PCM</td>
        </tr>
        <tr>
            <td align="right">27</td>
            <td>13</td>
            <td>14</td>
            <td>GND</td>
            <td colspan="2" rowspan="5"></td>
        </tr>
        <tr>
            <td align="right">22</td>
            <td>15</td>
            <td>16</td>
            <td>23</td>
        </tr>
        <tr>
            <td align="right">3.3.v</td>
            <td>17</td>
            <td>18</td>
            <td>24</td>
        </tr>
        <tr>
            <td align="right" rowspan="3">SPI</td>
            <td align="right">MOSI</td>
            <td align="right">10</td>
            <td>19</td>
            <td>20</td>
            <td>GND</td>
        </tr>
        <tr>
            <td align="right">MISO</td>
            <td align="right">09</td>
            <td>21</td>
            <td>22</td>
            <td>25</td>
        </tr>
        <tr>
            <td align="right">SCLK</td>
            <td align="right">11</td>
            <td align="right">23</td>
            <td>24</td>
            <td>08</td>
            <td>CE0</td>
            <td rowspan="2">SPI</td>
        </tr>
        <tr>
            <td colspan="2" rowspan="5"></td>
            <td align="right">GND</td>
            <td>25</td>
            <td>26</td>
            <td>07</td>
            <td>CE1</td>
        </tr>
        <tr>
            <td align="right">ID SD</td>
            <td>27</td>
            <td>28</td>
            <td>ID SC</td>
            <td colspan="2" rowspan="5"></td>
        </tr>
        <tr>
            <td align="right">05</td>
            <td>29</td>
            <td>30</td>
            <td>GND</td>
        </tr>
        <tr>
            <td align="right">06</td>
            <td>31</td>
            <td>32</td>
            <td>12</td>
        </tr>
        <tr>
            <td align="right">13</td>
            <td>33</td>
            <td>34</td>
            <td>GND</td>
        </tr>
        <tr>
            <td align="right">PCM</td>
            <td align="right">FS</td>
            <td>19</td>
            <td>35</td>
            <td>36</td>
            <td>16</td>
        </tr>
        <tr>
            <td align="right" colspan="2" rowspan="2"></td>
            <td align="right">26</td>
            <td>31</td>
            <td>37</td>
            <td>38</td>
            <td>DIN</td>
            <td rowspan="2">PCM</td>
        </tr>
        <tr>
            <td align="right">GND</td>
            <td>39</td>
            <td>40</td>
            <td>21</td>
            <td>DOUT</td>
        </tr>
    </tbody>
</table>

More information avalable at [pinout.xyz](https://pinout.xyz/pinout/)

### I<sup>2</sup>C - Inter Integrated Circuit

* Pins: `GPIO2` (#3) and `GPIO3` (#5)
* I<sup>2</sup>C allows data exchange between microcontrollers and peripherals with a minimum of wiring

### UART 0 Universal Asynchronous Receiver/Transmitter

* Pins: `GPIO2` (#8) and `GPIO3` (#10)
* UART is an asynchronous serial communication protocol, meaning that it takes bytes of data and transmits the individual bits in a sequential fashion.

### SPI - Serial Peripheral Interface

* Pins: `GPIO10` (#19), `GPI09` (#21), `GPI11` (#23), `GPI08` (#24), and `GPI07` (#26)
* The Serial Peripheral Interface(SPI) is a communication protocol to transfer data between micro-computers like the Raspberry Pi and peripheral devices. These devices may be either sensors or actuators.

### PCM - Pulse-code Modulation

* Pins: `GPIO18` (#12), `GPI19` (#35), `GPI38` (#37), and `GPI21` (#40)
* PCM (Pulse-code Modulation) is a digital representation of sampled analog.



