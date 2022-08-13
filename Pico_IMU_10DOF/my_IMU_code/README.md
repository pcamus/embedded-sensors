## MicroPython classes for IMU_10DOF sensors.

**ICM20948.**


**LPS22HB.**

Class to use the LPS22HB chip : [lps22hb_mod.py](lps22hb_mod.py).

The class definition begins after the definition of several LPS22HB registers and parameters values.

**`class LPS22HB(object):`**

The the class inherits of the **`object`** class. This is not mandatory, for a discussion on the subject see : [https://stackoverflow.com/questions/4015417/why-do-python-classes-inherit-object](https://stackoverflow.com/questions/4015417/why-do-python-classes-inherit-object)

**`def __init__(self,address=LPS22HB_I2C_ADDRESS):`**

- The constructor of the class starts with the definition of 5 data members and their initialisation.
- Tests if the right component is present.
-  Make a reset of the chip by calling the **`LPS22HB_RESET()`** method.

**`def LPS22HB_RESET(self):`**

Reset method, writes a 1 to the SWRESET bit of the CTRL_REG2 and the wait until this bit is clear by the chip indicting the end of the reset process.

**`def LPS22HB_READ_P_T(self):`**

Read pressure and temperature values inside the chip. Return them.
Note that these values are stored in the object data members and remains there between calls. If data is not available **`self._read_byte(ADD_STATUS) & P_DA_MASK`** return 0 and the code returns the previous sampled value.
