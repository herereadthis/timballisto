"""Demo the MPU-6050 accelerometer."""

import smbus
import math
import time

# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c


def read_byte(adr):
    """Read Byte."""
    return bus.read_byte_data(address, adr)


def read_word(adr):
    """Read word."""
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr + 1)
    val = (high << 8) + low
    return val


def read_word_2c(adr):
    """Read word 2c."""
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val


def dist(a, b):
    """Get distance."""
    return math.sqrt((a * a) + (b * b))


def get_y_rotation(x, y, z):
    """Get y-rotation."""
    radians = math.atan2(x, dist(y, z))
    return -math.degrees(radians)


def get_x_rotation(x, y, z):
    """Get x-rotation."""
    radians = math.atan2(y, dist(x, z))
    return math.degrees(radians)


# or bus = smbus.SMBus(1) for Revision 2 boards
bus = smbus.SMBus(1)
# This is the address value read via the i2cdetect command
address = 0x68

# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(address, power_mgmt_1, 0)

while True:
    time.sleep(0.1)
    gyro_xout = read_word_2c(0x43)
    gyro_yout = read_word_2c(0x45)
    gyro_zout = read_word_2c(0x47)

    print('gyro_xout: %s scaled: %s' % (gyro_xout, gyro_xout / 131))
    print('gyro_yout: %s scaled: %s' % (gyro_yout, gyro_yout / 131))
    print('gyro_zout: %s scaled: %s' % (gyro_zout, gyro_zout / 131))

    accel_xout = read_word_2c(0x3b)
    accel_yout = read_word_2c(0x3d)
    accel_zout = read_word_2c(0x3f)

    accel_xout_scaled = accel_xout / 16384.0
    accel_yout_scaled = accel_yout / 16384.0
    accel_zout_scaled = accel_zout / 16384.0

    print('accel_xout: %s scaled: %s' % (accel_xout, accel_xout_scaled))
    print('accel_yout: %s scaled: %s' % (accel_yout, accel_yout_scaled))
    print('accel_zout: %s scaled: %s' % (accel_zout, accel_zout_scaled))

    x_rotation = get_x_rotation(
        accel_xout_scaled, accel_yout_scaled, accel_zout_scaled
    )
    y_rotation = get_y_rotation(
        accel_xout_scaled, accel_yout_scaled, accel_zout_scaled
    )
    print('x rotation: %s' % (x_rotation))
    print('y rotation: %s' % (y_rotation))

    time.sleep(0.5)
