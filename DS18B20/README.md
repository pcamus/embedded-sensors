<h2>DS18B20.</h2>
<h3>Waterproof temperature sensor.</h3>
<p><em><strong>Features:</strong></em></p>
<ul>
<li>Range : -55&deg;C &agrave; +125&deg;C</li>
<li>Accuracy &plusmn;0.5&deg;C from -10&deg;C to +85&deg;C</li>
<li>Supply voltage : from 3V to 5.5V</li>
<li>Interface&nbsp;: <a href="https://en.wikipedia.org/wiki/1-Wire">OneWire</a></li>
<li>Datasheet&nbsp;: <a href="https://datasheets.maximintegrated.com/en/ds/DS18B20.pdf">DS18B20</a></li>
</ul>
<p><em><strong>Applications :</strong></em></p>
<ul>
<li>Thermostats.</li>
<li>Thermometers.</li>
<li>Heating control.</li>
</ul>

<em><strong>PDF in french :</strong></em> <a href="https://github.com/pcamus/embedded-sensors/blob/main/DS18B20/DS18B20.pdf">DS18B20.pdf</a>
<p>&nbsp;</p>
<p><em><strong>Arduino programming in C/C++.</strong></em></p>
<p>DallasTemperature library :<a href="https://github.com/milesburton/Arduino-Temperature-Control-Library">https://github.com/milesburton/Arduino-Temperature-Control-Library</a></p>
<p>Example : <a href="https://github.com/pcamus/embedded-sensors/blob/main/DS18B20/ds18b20.ino">ds18b20.ino</a></p>

<p>&nbsp;</p>
<p><em><strong>Pythonprogramming for the Raspberry Pi.</strong></em></p>
<p>OneWire bus must be enabled with the configuration utility of Raspbian,interface tab.<br />
Then add the following line in : /boot/config.txt<br />dtoverlay=w1-gpio,gpiopin=6<br />
You can specify which line to use for the sensor (in the exemple : GPIO6), GPIO4 is the default</p>
<p>Libray w1thermsensor :<br /><a href="https://github.com/timofurrer/w1thermsensor">https://github.com/timofurrer/w1thermsensor</a></p>
<p>Example : <a href="https://github.com/pcamus/embedded-sensors/blob/main/DS18B20/ds18b20.ino">https://github.com/pcamus/embedded-sensors/blob/main/DS18B20/ds18b20.py</a></p>

