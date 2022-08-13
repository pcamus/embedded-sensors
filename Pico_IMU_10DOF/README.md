## Pico 10DOF IMU (Inertial Measurement Unit).

This repository is about a Raspberry Pi Pico (RP2040) module containing two sensors IC : 

- The ICM20948 which is a 3-axis accelerometer, 3-axis gyroscope and 3-axis magnetometer. This circuit also contains a Digital Motion Processor (DMP) and a temperature sensor. The DMP runs a motion algorithm relieving the processor of this task. See the [datasheet](ICM-20948-v1.5.pdf) for the detailed characteristics.
- The LPS22HB which is a barometric and temperature sensors. See the [datasheet](Lps22hb.pdf) for the detailed characteristics.

The [schematic](Pico-10DOF-IMU_Sch.pdf) of the board gives details of the circuitry.

The wiki of the manufacturer is : [https://www.waveshare.com/wiki/Pico-10DOF-IMU](https://www.waveshare.com/wiki/Pico-10DOF-IMU)

The board will be used with a MicroPyhton program.

The manufacturer gives two MicroPython programs to test the sensor. Although the programs work, I found them difficult to understand, cluttered with useless details and containing very few comments. The code is [here](waveshare_code).

So, I decided to make two modules, one containing a class for the ICM20948 and one with a class for the LPS22HB and two test files for each device.

Theses modules are simple and don't use all the features of the sensors. For instance, the ICM20948 class can only access the accelerometer and the temperature sensor. More functions will follow.

You can find my code [here](my_IMU_code)

The first application of these modules will be to measure the trajectory of a weather balloon.

- [ ] To do : add member functions for the gyroscope and magnetometer.
- [ ] To do : study how to use the DMP processor.
- [ ] To do : check data acquisition time in order to determine the maxime sampling speed (using a logic analyser).
