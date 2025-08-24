from i2c_lcd import I2cLcd
from w1thermsensor import W1ThermSensor
from datetime import datetime


def get_time():
    local_now = datetime.now()
    return local_now.strftime('%I:%M:%S %p')


def main():
    # Initialise display
    lcd = I2cLcd(16, 2)
    sensor = W1ThermSensor()

    try:
        while True:
            celsius = sensor.get_temperature(W1ThermSensor.DEGREES_C)
            farenheit = sensor.get_temperature(W1ThermSensor.DEGREES_F)
            temp_msg = '%sC - %sF' % (round(celsius, 1), round(farenheit, 1))
            lcd.set_line(1, 'Temperature:')
            lcd.set_line(2, temp_msg)
            lcd.display_message(3)

            local_now = datetime.now()
            current_date = local_now.strftime('%a, %d %b %Y')
            lcd.set_line(1, current_date)
            lcd.set_line(2, get_time())
            lcd.display_message(1)
            lcd.set_line(2, get_time())
            lcd.display_message(1)
            lcd.set_line(2, get_time())
            lcd.display_message(0.5)

    except KeyboardInterrupt:
        pass
    finally:
        lcd.clear_display()


if __name__ == '__main__':
    main()
