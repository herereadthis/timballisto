"""Demostrate the thermometer."""

# Make sure 1-Wire Interface is enabled.
# Go to Menu > Preferences > Raspberry Pi Configuration > Interfaces.

from w1thermsensor import W1ThermSensor

# new instance of thermometer
sensor = W1ThermSensor()

temperature = sensor.get_temperature()
celsius = sensor.get_temperature(W1ThermSensor.DEGREES_C)
farenheit = sensor.get_temperature(W1ThermSensor.DEGREES_F)
kelvin = sensor.get_temperature(W1ThermSensor.KELVIN)

if __name__ == '__main__':
    def get_rounded_float(float_num, figures=3):
        """Return number rounded to X number of places."""
        precision = '{0:.%sf}' % figures
        # float means return the formatted string as an actual number type
        return float(precision.format(float_num))

    print('DS18B20 Thermometer Demo')
    print('Temperature:    %s' % (get_rounded_float(temperature, 3)))
    print('Celsus:         %s' % (get_rounded_float(celsius, 3)))
    print('Farenheit:      %s' % (get_rounded_float(farenheit, 3)))
    print('Kelvin:         %s' % (get_rounded_float(kelvin, 3)))
