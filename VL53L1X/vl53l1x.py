import qwiic
import time

ToF = qwiic.QwiicVL53L1X()

while True:
    ToF.start_ranging()  # Write default configuration bytes      
    time.sleep(.005)
    distance = ToF.get_distance()  # Read distance
    time.sleep(.005)
    ToF.stop_ranging()
