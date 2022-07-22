#include <OneWire.h>
#include <DallasTemperature.h>

// Data wire is connected to the Arduino digital pin 4
#define ONE_WIRE_BUS 4

// Create a OneWire object to communicate with the sensor(s)
OneWire oneWire(ONE_WIRE_BUS);

// Pass OneWire object to Dallas Temperature library
DallasTemperature sensors(&oneWire);

void setup(void)
{
// Start up the library
sensors.begin();
}

void loop(void)
{
// Global temperature request to all devices on the bus
sensors.requestTemperatures();
// Why "byIndex"?
// You can have more than one IC on the same bus.
// 0 refers to the first IC on the wire
float temp = sensors.getTempCByIndex(0));
}
