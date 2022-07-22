from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor() # create sensor object
temp = sensor.get_temperature() # get temperature in Celsius
# The first found sensor will be taken
