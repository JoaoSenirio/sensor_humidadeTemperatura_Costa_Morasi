import utime
from machine import Pin, I2C
import ahtx0

# Instancia os barramento/pinos usados para comunicação I2C
i2c = I2C(1, scl=Pin(3), sda=Pin(2))

# Instancia objeto do sensor
sensor = ahtx0.AHT10(i2c)

reads_temp = []
reads_hum = []
window = 5

def mean(values):
    return sum(values) / len(values)

while True:

    if len(reads_temp) < window:
        reads_temp.append(sensor.temperature)
    else:
        i = 1
        for i in range(len(reads_temp)):
            reads_temp[i - 1] = reads_temp[i]
        reads_temp[window - 1] = sensor.temperature

        print("\nTemperatura por media movel: %0.2f C" % mean(reads_temp))
    
    if len(reads_hum) < window:
        reads_hum.append(sensor.relative_humidity)
    else:
        i = 1
        for i in range(len(reads_hum)):
            reads_hum[i - 1] = reads_hum[i]
        reads_hum[window - 1] = sensor.relative_humidity
        print("Humidade relativa por media movel: %0.2f %%" % mean(reads_hum))

    utime.sleep(1)
