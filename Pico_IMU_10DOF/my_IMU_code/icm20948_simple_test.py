# File : icm20948_simple_test.py
# Test icm20948_mod MicroPython module
# Take N acceleration samples with a defined interval
# and store them into a csv file, then measure and add temperature
# Used to access ICM20948 chip on PICO 10DOF IMU.
# For now, restricted to acceleration and temperature
# Chip : https://www.waveshare.com/w/upload/5/57/ICM-20948-v1.3.pdf
# Pico 10-DOF IMU module : https://www.waveshare.com/wiki/Pico-10DOF-IMU
# info@pcamus.be
# 12/8/2022

from icm20948_mod import *
import utime

N_SAMPLE=50 # number of sample taken before writing into the file
SAMPLE_INTER_MS=100 # interval between to samples
   
  
icm20948=ICM20948()

filename="acc.csv"
f = open(filename, "w")
f.write("Ax;Ay;Az\r\n")

log_data=[]
utime.sleep(0.5)

Temp=icm20948.icm20948_Temp_Read()
Temp=(Temp/333.87)+21
print("Temperature : %4.1f"%Temp)
print()

for i in range(N_SAMPLE): # take N_SAMPLE
    start=utime.ticks_ms()

    Accel=icm20948.icm20948_Accel_Read()
    log_data.append(Accel)
    print("-------------------------------------------------------------")
    print("Acceleration:  X = %d , Y = %d , Z = %d\r\n"%(Accel[0],Accel[1],Accel[2]))  

    while utime.ticks_diff(utime.ticks_ms(), start)<SAMPLE_INTER_MS:  # logging rate
        pass     

for i in range(len(log_data)):
    for j in range(2):
        f.write("%d;"%log_data[i][j])
    f.write("%d\r\n"%log_data[i][2])

f.write("Temperature = ;%4.1f\r\n"%Temp)
f.close()
