import utime
from machine import Pin, I2C
import ahtx0

# Instancia os barramento/pinos usados para comunicação I2C
i2c = I2C(1, scl=Pin(3), sda=Pin(2))

# Instancia objeto do sensor
sensor = ahtx0.AHT10(i2c)

while True:
    print("\nTemperatura: %0.2f C" % sensor.temperature)
    print("Humidade relativa: %0.2f %%" % sensor.relative_humidity)
    utime.sleep(1)
