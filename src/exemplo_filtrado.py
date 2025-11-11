import utime
from machine import Pin, I2C
import ahtx0

# Instancia os barramento/pinos usados para comunicação I2C
i2c = I2C(1, scl=Pin(3), sda=Pin(2))

# Instancia objeto do sensor
sensor = ahtx0.AHT10(i2c)

reads_temp = [] # Leituras de temperatura
reads_hum = [] # Leituras de humidade
window = 5 # Tamanho da lista/buffer para média móvel

# Cálculo da média
def mean(values):
    return sum(values) / len(values)

while True:

    if len(reads_temp) < window:
        # Caso a lista não esteja cheia apenas adiciona uma nova leitura
        reads_temp.append(sensor.temperature)
    else:
        # Caso a lista esteja cheia, desloca todas as medidas anteriores
        # para a esquerda e adiciona uma nova ao final da lista.
        i = 1
        for i in range(len(reads_temp)):
            reads_temp[i - 1] = reads_temp[i]
        reads_temp[window - 1] = sensor.temperature

        # Impressão na tela da temperatura com média móvel
        print("\nTemperatura por media movel: %0.2f C" % mean(reads_temp))
    
    if len(reads_hum) < window:
        # Caso a lista não esteja cheia apenas adiciona uma nova leitura
        reads_hum.append(sensor.relative_humidity)
    else:
        # Caso a lista esteja cheia, desloca todas as medidas anteriores
        # para a esquerda e adiciona uma nova ao final da lista.
        i = 1
        for i in range(len(reads_hum)):
            reads_hum[i - 1] = reads_hum[i]
        reads_hum[window - 1] = sensor.relative_humidity

        # Impressão na tela da humidade com média móvel
        print("Humidade relativa por media movel: %0.2f %%" % mean(reads_hum))

    utime.sleep(1)
