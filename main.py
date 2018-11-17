## testing ASDS9300 module

from apds9930 import APDS9930
import machine
import time 

i2c = machine.I2C(scl = machine.Pin(4), sda = machine.Pin(5))

sensor = APDS9930(i2c) #pass the i2c object into the sensor object

sensor.ALS_Enable()
sensor.getALS()  #ambient light reading

#initiate proximity NOTE requires VL connected to 3V3 on APDS9930 module
sensor.Proximity_Enable() 

#led turns on when prox sensor is triggered
led = machine.Pin(2, machine.Pin.OUT)
led.value(1)

while True:
    time.sleep(0.1)
    if sensor.getProximity()>100:
        led.value(0)
    else:
        led.value(1) 

