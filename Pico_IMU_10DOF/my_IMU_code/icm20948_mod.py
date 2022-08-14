# File : icm20948_mod.py
# ICM20948 MicroPython class
# Used to access ICM20948 chip on PICO 10DOF IMU.
# For now, restricted to acceleration and temperature
# Chip : https://www.waveshare.com/w/upload/5/57/ICM-20948-v1.3.pdf
# Pico 10-DOF IMU module : https://www.waveshare.com/wiki/Pico-10DOF-IMU
# info@pcamus.be
# 12/8/2022

from machine import I2C
import utime
import sys

# define ICM-20948 Device I2C address
I2C_ADD_ICM20948                = 0x68

# ICM-20948 Register
# ADD prefix = register address, VAL prefix = value to use

# user bank selection register
ADD_REG_BANK_SEL                = 0x7F
VAL_REG_BANK_0                  = 0x00
VAL_REG_BANK_2                  = 0x20


# user bank 0 used registers
ADD_WHO_AM_I                     = 0x00 # identification register
VAL_WHO_AM_I                     = 0xEA

ADD_PWR_MGMT_1                   = 0x06 # power management register
VAL_DEVICE_RESET                 = 0x80 # Device reset
VAL_CLKSEL                       = 0x01 # Best clock source

ADD_ACCEL_XOUT_H                 = 0x2D # 16 bits X,Y,Z acceleration registers MSB first
ADD_ACCEL_YOUT_H                 = 0x2F
ADD_ACCEL_ZOUT_H                 = 0x31

ADD_TEMP_OUT_H                   = 0x39 # 16 bits temperature register


# user bank 2 used registers
ADD_ACCEL_SMPLRT_DIV_2           = 0x10  # ACCEL_SMPLRT_DIV[11:8], sample rate divider MSB
                                         # not used assumed to be 0 (reset value)
ADD_ACCEL_SMPLRT_DIV_2           = 0x11  # ACCEL_SMPLRT_DIV[7:0], sample rate divider LSB
VAL_ACCEL_DLPFCFG                = 0x07  # ODR (Output Data Rate) = 140.6 Hz

ADD_ACCEL_CONFIG                 = 0x14
VAL_ACCEL_DLPCFG                 = 0x30  # bit[5:3] DLPCFG=3 Filter bandwith = 50.4 Hz
VAL_ACCEL_FS_SEL                 = 0x00  # bit[2:1] Full scale = +/-2g (+/-12.62 m/s2)
VAL_ACCEL_FCHOICE                = 0x01  # bit[0] Enable accel DLPF (enable the low pass filter)


class ICM20948(object):
  def __init__(self,address=I2C_ADD_ICM20948):
    self._address = address
    self._bus = I2C(1)
    self._accel = [0,0,0] # X, Y ,Z acceleration value
    self._temp = 0 # temperature
    
    # detect if ICM20948 is present
    if self._read_byte(ADD_WHO_AM_I)==VAL_WHO_AM_I:
        print("ICM20948 detected.\r\n")
    else :
        print("No ICM20948 detected - exiting program.")
        sys.exit()

    # Reset device and set clock source 
    self._write_byte( ADD_REG_BANK_SEL , VAL_REG_BANK_0)
    self._write_byte( ADD_PWR_MGMT_1 , VAL_DEVICE_RESET) # Reset
    utime.sleep(0.1)
    self._write_byte( ADD_PWR_MGMT_1 , VAL_CLKSEL)  # Clock source
    
    # Set accelerometer speed, filtering and full scale value
    self._write_byte( ADD_REG_BANK_SEL , VAL_REG_BANK_2)
    self._write_byte( ADD_ACCEL_SMPLRT_DIV_2 ,  VAL_ACCEL_DLPFCFG) # set Output Data Rate
    # set low pass characteristics and full scale value
    self._write_byte( ADD_ACCEL_CONFIG , VAL_ACCEL_DLPCFG | VAL_ACCEL_FS_SEL | VAL_ACCEL_FCHOICE)
     
    utime.sleep(0.1)

  def icm20948_Accel_Read(self):
    self._write_byte( ADD_REG_BANK_SEL , VAL_REG_BANK_0)
    data =self._read_block(ADD_ACCEL_XOUT_H, 6)
    self._accel[0] = (data[0]<<8)|data[1]  # convert to 16 bits values and put in _accel list
    self._accel[1] = (data[2]<<8)|data[3]
    self._accel[2] = (data[4]<<8)|data[5]
    
    #The acceleration value is a modulo 2 coded value,
    # so it must be converted in a signed value
    if self._accel[0]>=32767:             
      self._accel[0]=self._accel[0]-65535
    if self._accel[1]>=32767:
      self._accel[1]=self._accel[1]-65535
    if self._accel[2]>=32767:
      self._accel[2]=self._accel[2]-65535
    return self._accel 
     
  def icm20948_Temp_Read(self):
    self._write_byte( ADD_REG_BANK_SEL , VAL_REG_BANK_0)
    data =self._read_block(ADD_TEMP_OUT_H, 2)
    self._temp = (data[0]<<8)|data[1] # convert to 16 bits values and put in _temp
    return self._temp
    
  def _read_byte(self,cmd):
    rec=self._bus.readfrom_mem(int(self._address),int(cmd),1)
    return rec[0]

  def _write_byte(self,cmd,val):
    self._bus.writeto_mem(int(self._address),int(cmd),bytes([int(val)]))
    utime.sleep_us(100)  

  def _read_block(self, reg, length=1):
    rec=self._bus.readfrom_mem(int(self._address),int(reg),length)
    return rec

 
