from i2c_lcd import I2cLcd


def main():
    # Initialise display
    lcd = I2cLcd(16, 2)

    try:
        while True:
            lcd.set_line(1, 'Hello World!')
            lcd.set_line(2, 'Lorem ipsum sit')
            lcd.display_message(3)

            lcd.set_line(1, 'Be kind; rewind.')
            lcd.set_line(2, 'Party on, dudes!')
            lcd.display_message(3)

    except KeyboardInterrupt:
        pass
    finally:
        lcd.clear_display()


if __name__ == '__main__':
    main()
