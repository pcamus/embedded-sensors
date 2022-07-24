//Be sure the vacuum tape has been removed from the sensor.

#include <Wire.h>
#include "SparkFun_VL53L1X.h" 

SFEVL53L1X distanceSensor;

void setup(void)
{
Wire.begin();// return 0  if init is OK 
}

void loop(void)
{
//Write configuration bytes to initiate measurement
distanceSensor.startRanging();  
while (!distanceSensor.checkForDataReady())
  {
  delay(1);
  }
// Read distance
int distance = distanceSensor.getDistance();  distanceSensor.clearInterrupt();
distanceSensor.stopRanging();
}
