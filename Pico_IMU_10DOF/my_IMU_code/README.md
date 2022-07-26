## MicroPython classes for IMU_10DOF sensors.

**ICM20948.**

Class to access the ICM20948 chip : [icm20948_mod.py](icm20948_mod.py).

The class definition begins after the definition of several ICM20948 registers and parameters values.

\
**`class ICM20948(object):`**

The  class inherits of the **`object`** class. This is not mandatory, for a discussion on the subject see : [https://stackoverflow.com/questions/4015417/why-do-python-classes-inherit-object](https://stackoverflow.com/questions/4015417/why-do-python-classes-inherit-object).

\
**`def __init__(self,address=I2C_ADD_ICM20948):`**

- The constructor of the class starts with the definition of 4 data members and their initialisation.
- Tests if the right component is present.
- Makes a reset of the chip by writing 1 in  the **`VAL_DEVICE_RESET`** bit of the PWR_MGMT_1 register.
- Chooses the clock source.
- Sets sample rate, filtering characteristics and range of the accelerometer.

\
**`def icm20948_Accel_Read(self):`**

Reads X,Y,Z acceleration. Corrects values to take into account the fact that the values are signed and returns the values.

\
**`def icm20948_Temp_Read(self):`**

Reads temperature and return it.

\
**`def _read_byte(self,cmd):`** et **`def _write_byte(self,cmd,val):`** are read and write methods on the I<sup>2</sup>C bus.

**`def _read_block(self, reg, length=1):`** reads a block of contiguous registers starting with reg register.

See [https://docs.micropython.org/en/latest/library/machine.I2C.html](https://docs.micropython.org/en/latest/library/machine.I2C.html) for details about the MicroPython I<sup>2</sup>C module.
 
\
Program to test the class : [icm20948_simple_test.py](icm20948_simple_test.py).

Reads **`N_SAMPLE`** of acceleration at **`SAMPLE_INTER_MS`** intervals and stores them in a csv file.

- Imports icm20948_mod and creates the **`icm20948`** object from the **`ICM20948`** class.
- Creates the csv file and writes columns header.
- Reads temperature with a call to **`icm20948.icm20948_Temp_Read()`** method.
- Loops for the acceleration logging and stores the value in a list (**`log_data`**).
- Writes **`log_data`** in the csv file and adds temperature reading to the file.

-----
**LPS22HB.**

Class to access the LPS22HB chip : [lps22hb_mod.py](lps22hb_mod.py).

The class definition begins after the definition of several LPS22HB registers and parameters values.

\
**`class LPS22HB(object):`**

The  class inherits of the **`object`** class. This is not mandatory, for a discussion on the subject see : [https://stackoverflow.com/questions/4015417/why-do-python-classes-inherit-object](https://stackoverflow.com/questions/4015417/why-do-python-classes-inherit-object).

\
**`def __init__(self,address=LPS22HB_I2C_ADDRESS):`**

- The constructor of the class starts with the definition of 4 data members and their initialisation.
- Tests if the right component is present.
- Makes a reset of the chip by calling the **`LPS22HB_RESET()`** method.

\
**`def LPS22HB_RESET(self):`**

Reset method, writes a 1 to the SWRESET bit of the CTRL_REG2 and the wait until this bit is cleared by the chip indicating the end of the reset process.

\
**`def LPS22HB_READ_P_T(self):`**

Reads pressure and temperature values inside the chip. Returns them.

Note that these values are stored in the object data members and remains there between calls. If data is not available **`self._read_byte(ADD_STATUS) & P_DA_MASK`** returns 0 and the method returns the previous sampled value.

\
**`def LPS22HB_START_ONESHOT(self):`**

This method triggers an acquisition.

\
**`def _read_byte(self,cmd):`** et **`def _write_byte(self,cmd,val):`** are read and write methods on the I<sup>2</sup>C bus.

**`def _read_block(self, reg, length=1):`** reads a block of contiguous registers starting with reg register. 

See [https://docs.micropython.org/en/latest/library/machine.I2C.html](https://docs.micropython.org/en/latest/library/machine.I2C.html) for details about the MicroPython I<sup>2</sup>C module.
 
\
Program to test the class : [lps22hb_simple_test.py](lps22hb_simple_test.py).

Imports lps22hb_mod, creates the **`lps22hb`** object from the **`LPSHB22`** class then calls **`LPS22HB_READ_P_T()`** method 10 times and dsiplays returned values with 1 second delay between each call.
