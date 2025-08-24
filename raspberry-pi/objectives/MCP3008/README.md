# How to Wire MCP3008 Converter to a Raspberry PI GPIO

<table>
    <tbody>
        <tr>
            <td align="right"><strong>CH0</strong></td>
            <td align="right">01</td>
            <td rowspan="8"></td>
            <td>O</td>
            <td rowspan="8"></td>
            <td>16</td>
            <td><strong>V<sub>DD</sub></strong></td>
        </tr>
        <tr>
            <td align="right"><strong>CH1</strong></td>
            <td align="right">02</td>
            <td rowspan="7"></td>
            <td>15</td>
            <td><strong>V<sub>REF</sub></strong></td>
        </tr>
        <tr>
            <td align="right"><strong>CH2</strong></td>
            <td align="right">03</td>
            <td>14</td>
            <td><strong>AGND</strong></td>
        </tr>
        <tr>
            <td align="right"><strong>CH3</strong></td>
            <td align="right">04</td>
            <td>13</td>
            <td><strong>CLK</strong></td>
        </tr>
        <tr>
            <td align="right"><strong>CH4</strong></td>
            <td align="right">05</td>
            <td>12</td>
            <td><strong>D<sub>OUT</sub></strong></td>
        </tr>
        <tr>
            <td align="right"><strong>CH5</strong></td>
            <td align="right">06</td>
            <td>11</td>
            <td><strong>D<sub>IN</sub></strong></td>
        </tr>
        <tr>
            <td align="right"><strong>CH6</strong></td>
            <td align="right">07</td>
            <td>10</td>
            <td><strong>CS/SHDN</strong></td>
        </tr>
        <tr>
            <td align="right"><strong>CH7</strong></td>
            <td align="right">07</td>
            <td>09</td>
            <td><strong>DGND</strong></td>
        </tr>
    </tbody>
</table>

*Refer to the [GPIO Pinout](https://github.com/herereadthis/lutra/blob/master/docs/GPIO.md) doc as a reference*

The MCP3008 uses the Serial Peripheral Interface(SPI), which is a communication
protocol to transfer data between micro-computers like the Raspberry Pi and 
peripheral devices. These devices may be either sensors or actuators.

```python
from gpiozero import MCP3008
```


*  Go into Raspberry Pi Configuration > Interfaces > enable SPI
* The side with the notch is 16, the other side is 9.
* If the notch is facing to your left, connect wires from the raspberry pi from the side that is to the top of the notch (start from top left is pin 16, top right is 09)

## Instructions:

* pin `16` (**V<sub>DD</sub>**) goes to **3V**
* pin `15` (**V<sub>REF</sub>**) goes to **3V**
* pin `14` (**AGND**) goes to **GND** (or pin #17)
* pin `13` (**CLK**) goes to SPI SCLK **GP11**
* pin `12` (**D<sub>OUT</sub>**) goes to SPI MISO **GP09**
* pin `11` (**D<sub>IN</sub>**) goes to SPI MOSI **GP10**
* pin `10` (**CS/SHDN**) goes to SPI CE0 **GP08**
* pin `09` (**CS/SHDN**) goes to **GND** (or pin #20)