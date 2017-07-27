import smbus
import time

# Define some device parameters
I2C_ADDR = 0x3f  # I2C device address, if any error, change this to 0x27
LCD_WIDTH = 16  # Maximum characters per line
LCD_HEIGHT = 2  # Can also be 4 for 20x4 displays

# Define some device constants
LCD_CHR = 1  # Mode - Sending data
LCD_CMD = 0  # Mode - Sending command

LCD_BACKLIGHT = 0x08  # On
# LCD_BACKLIGHT = 0x00  # Off

ENABLE = 0b00000100  # Enable bit

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005


class I2cLcd:

    def __init__(self, lcd_width=LCD_WIDTH, lcd_height=LCD_HEIGHT):
        # Maximum characters per line
        self.lcd_width = lcd_width
        self.lcd_height = lcd_height

        # Open I2C interface
        # Rev 2 Pi uses 1
        self.bus = smbus.SMBus(1)
        # Rev 1 Pi uses 0
        # self.bus = smbus.SMBus(0)

        # Initialise display
        self.lcd_byte(0x33, LCD_CMD)  # 110011 Initialise
        self.lcd_byte(0x32, LCD_CMD)  # 110010 Initialise
        self.lcd_byte(0x06, LCD_CMD)  # 000110 Cursor move direction
        self.lcd_byte(0x0C, LCD_CMD)  # 001100 Display On,Cursor Off, Blink Off
        # 101000 Data length, number of lines, font size
        self.lcd_byte(0x28, LCD_CMD)
        self.lcd_byte(0x01, LCD_CMD)  # 000001 Clear display
        time.sleep(E_DELAY)
        self.lines = []
        for i in range(self.lcd_height):
            self.lines.append('')

    def lcd_byte(self, bits, mode):
        bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
        bits_low = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT

        # High bits
        self.bus.write_byte(I2C_ADDR, bits_high)
        self.lcd_toggle_enable(bits_high)

        # Low bits
        self.bus.write_byte(I2C_ADDR, bits_low)
        self.lcd_toggle_enable(bits_low)

    def lcd_toggle_enable(self, bits):
        # Toggle enable
        time.sleep(E_DELAY)
        self.bus.write_byte(I2C_ADDR, (bits | ENABLE))
        time.sleep(E_PULSE)
        self.bus.write_byte(I2C_ADDR, (bits & ~ENABLE))
        time.sleep(E_DELAY)

    def format_message(self, message):
        """Format to be no more than width of LCD, or fill up with spaces."""
        return message.ljust(self.lcd_width, ' ')

    def set_line(self, line, text):
        self.lines[line - 1] = self.format_message(text)

    def display_message(self):
        lcd_line_1 = 0x80  # LCD RAM address for the 1st line
        lcd_line_2 = 0xC0  # LCD RAM address for the 2nd line
        lcd_line_3 = 0x94  # LCD RAM address for the 3rd line
        lcd_line_4 = 0xD4  # LCD RAM address for the 4th line

        ram_addresses = [lcd_line_1, lcd_line_2, lcd_line_3, lcd_line_4]

        for index, line in enumerate(self.lines):
            self.lcd_byte(ram_addresses[index], LCD_CMD)

            for i in range(self.lcd_width):
                self.lcd_byte(ord(line[i]), LCD_CHR)


def main():
    # Main program block

    # Initialise display
    i2c_lcd = I2cLcd(16, 2)

    try:
        while True:
            i2c_lcd.set_line(1, 'Em yeu chong!')
            i2c_lcd.set_line(2, 'An com chua?')
            i2c_lcd.display_message()
            time.sleep(3)

            i2c_lcd.set_line(1, 'Khong Biet!!!')
            i2c_lcd.set_line(2, 'Ai Biet Chong?')
            i2c_lcd.display_message()
            time.sleep(3)

    except KeyboardInterrupt:
        pass
    finally:
        i2c_lcd.lcd_byte(0x01, LCD_CMD)


if __name__ == '__main__':
    main()
