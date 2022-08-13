# File : lps22hb_simple_test.py
# Pico 10DOF IMU board
# Read pressure and temperature from LPS22HB
# Chip : https://www.waveshare.com/w/upload/2/20/Lps22hb.pdf
# Pico 10-DOF IMU module : https://www.waveshare.com/wiki/Pico-10DOF-IMU
# info@pcamus.be
# 12/8/2022

import uos
import utime
from lps22hb_mod import *
from machine import Pin

temp_cal = -2.3
pres_cal = 40

t=utime.localtime()
print("Start time : %02d:%02d:%02d"%(t[3],t[4],t[5]))

print("\nPressure Sensor Test Program ...\n")
lps22hb=LPS22HB()

for i in range (10):
    pressure, temperature = lps22hb.LPS22HB_READ_P_T()

    pressure=round(pressure+pres_cal,0)
    temperature=round(temperature+temp_cal,1)

    print("Pressure = %4.0f  Temperature = %3.1f\r\n"%(pressure, temperature))
    
    utime.sleep(1)

