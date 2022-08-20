# File : icm20948_lps22hb_speed_test.py
#
# Tests sampling rate of icm20948_mod together with lps22hb_mod 
# Takes 10 acceleration samples per second during 10 sec
# Then one pressure and one temperature sample.
#
# Append the result to binary files : 10 s = 600 bytes for acceleration
# and 4 bytes for pressure and temperature.
#
# Chip ICM20948 : https://www.waveshare.com/w/upload/5/57/ICM-20948-v1.3.pdf
# Chip LPS22HB : https://www.waveshare.com/w/upload/2/20/Lps22hb.pdf
# Pico 10-DOF IMU module : https://www.waveshare.com/wiki/Pico-10DOF-IMU
#
# Results : about 60 ms too slow each 10 seconds.
#
# info@pcamus.be
# 17/8/2022

from icm20948_mod import *
from lps22hb_mod import *
import utime
import uos

# Calibration values to add to temperature and pressure (for my LPS22HB sensor).
temp_cal = -2.3
pres_cal = 40

# Creates sensors instances
icm20948=ICM20948()
lps22hb=LPS22HB()

log_acc=[]
file_buf_acc= bytearray(600) # 100 x 2 bytes x 3 axis
file_buf_PT= bytearray(4) # pressure = 2 bytes, temperature 2 bytes

filn_acc="acc.bin"
filn_PT="Press_Temp.bin"

# removes old copy of files if they exist
try:
    uos.remove(filn_acc) 
except:
    pass

try:
    uos.remove(filn_PT) 
except:
    pass


while(True):
    
    smpl_start=utime.ticks_ms() # used to track the time neccessary for a group samples
                                # 100 acceleration + 1 pressure and 1 temperature sample
        
    for i in range(100): # take 100 acceleration samples
        
        start=utime.ticks_ms()
       
        Accel=icm20948.icm20948_Accel_Read()
        log_acc.append(Accel)
        
        while utime.ticks_diff(utime.ticks_ms(), start)<100:  # take a sample each 100 ms
            pass     

    pressure, temperature = lps22hb.LPS22HB_READ_P_T() # and take one pressure and temperature
                                                       # measurement each 10 sec
 
    # Convert data to bytearray
    for i in range(100):
        buf_index=i*6
        file_buf_acc[buf_index]=log_acc[i][0]//256   # Acc X MSB
        file_buf_acc[buf_index+1]=log_acc[i][0]%256  # Acc X LSB
        file_buf_acc[buf_index+2]=log_acc[i][1]//256 # Acc Y MSB 
        file_buf_acc[buf_index+3]=log_acc[i][1]%256  # Acc Y LSB
        file_buf_acc[buf_index+4]=log_acc[i][2]//256 # Acc Z MSB
        file_buf_acc[buf_index+5]=log_acc[i][2]%256  # Acc Z LSB
    
    # writes to a binary file
    f = open(filn_acc, "ab")
    f.write(file_buf_acc)
    f.close()
    
    # Convert data to bytearray
    int_pressure=int(pressure + pres_cal)
    int_temperature=int((temperature + temp_cal)*10) # scales temperature to keep tenth of degree
                 
    file_buf_PT[0]=int_pressure//256
    file_buf_PT[1]=int_pressure%256
    file_buf_PT[2]=int_temperature//256                 
    file_buf_PT[3]=int_temperature%256
    
    # writes to a binary file
    f = open(filn_PT, "ab")
    f.write(file_buf_PT)
    f.close()
        
    smpl_end=utime.ticks_ms()
    print("One pass sampling time :%d ms"%utime.ticks_diff(smpl_end,smpl_start))
    

