## DS18B20.
### Waterproof temperature sensor.
***Features:***

- Range : -55°C to +125&°C
- Accuracy +/-0.5°C from -10°C to +85°C
- Supply voltage : from 3V to 5.5V
- Interface: [OneWire](https://en.wikipedia.org/wiki/1-Wire)
- Datasheet: [DS18B20](https://datasheets.maximintegrated.com/en/ds/DS18B20.pdf)

***Applications :***

- Thermostats.
- Thermometers.
- Heating control.

  

***PDF in french :*** [DS1820.pdf](DS18B20.pdf)

-----
***Arduino programming in C/C++.***
DallasTemperature library :[https://github.com/milesburton/Arduino-Temperature-Control-Library](https://github.com/milesburton/Arduino-Temperature-Control-Library)

Example : [ds18b20.ino](ds18b20.ino) 

***Python programming for the Raspberry Pi.***

First, OneWire bus must be enabled with the configuration utility of Raspbian (interface tab).

Then add the following line in : /boot/config.txt

`dtoverlay=w1-gpio,gpiopin=6`

You can specify which line to use for the sensor (in the exemple : GPIO6), GPIO4 is the default

Library w1thermsensor : [https://github.com/timofurrer/w1thermsensor](https://github.com/timofurrer/w1thermsensor)

Example : [ds18b20.py](ds18b20.py)
