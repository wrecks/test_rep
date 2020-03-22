import machine
from machine import I2C, Pin, Signal


i2c = machine.I2C(-1,scl=machine.Pin(27), sda=machine.Pin(32))
#i2c.init(scl=machine.Pin(27), sda=machine.Pin(32),freq=400000)

devices=i2c.scan()
print(devices)


