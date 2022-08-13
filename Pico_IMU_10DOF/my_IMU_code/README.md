## MicroPython classes for IMU_10DOF sensors.

**ICM20948.**

-----
**LPS22HB.**

Class to access the LPS22HB chip : [lps22hb_mod.py](lps22hb_mod.py).

The class definition begins after the definition of several LPS22HB registers and parameters values.

\
**`class LPS22HB(object):`**

The  class inherits of the **`object`** class. This is not mandatory, for a discussion on the subject see : [https://stackoverflow.com/questions/4015417/why-do-python-classes-inherit-object](https://stackoverflow.com/questions/4015417/why-do-python-classes-inherit-object)

\
**`def __init__(self,address=LPS22HB_I2C_ADDRESS):`**

- The constructor of the class starts with the definition of 5 data members and their initialisation.
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
 
 See [https://docs.micropython.org/en/latest/library/machine.I2C.html](https://docs.micropython.org/en/latest/library/machine.I2C.html) for details about the MicroPython I<sup>2</sup>C module.
 
 
