from i2c_lcd import I2cLcd
from w1thermsensor import W1ThermSensor


def main():
    # Initialise display
    lcd = I2cLcd(16, 2)
    sensor = W1ThermSensor()

    try:
        while True:
            celsius = sensor.get_temperature(W1ThermSensor.DEGREES_C)
            temp_msg = '%s Celsius' % (round(celsius, 1))
            lcd.set_line(1, 'Temperature:')
            lcd.set_line(2, temp_msg)
            lcd.display_message(3)

            farenheit = sensor.get_temperature(W1ThermSensor.DEGREES_F)
            temp_msg = '%s Farenheit' % (round(farenheit, 1))
            lcd.set_line(1, 'Temperature')
            lcd.set_line(2, temp_msg)
            lcd.display_message(3)

    except KeyboardInterrupt:
        pass
    finally:
        lcd.clear_display()


if __name__ == '__main__':
    main()
