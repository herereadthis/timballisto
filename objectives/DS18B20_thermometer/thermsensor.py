from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()
temperature = sensor.get_temperature()
celsius = sensor.get_temperature(W1ThermSensor.DEGREES_C)
farenheit = sensor.get_temperature(W1ThermSensor.DEGREES_F)
kelvin = sensor.get_temperature(W1ThermSensor.KELVIN)

print(temperature)
print(celsius)
print(farenheit)
print(kelvin)
