import utime
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# estabelecendo comunicacao I2C
    # pinos GPIO 2 (SDA) e GPIO 3 (SCL)
i2c = I2C(1, scl=Pin(3), sda=Pin(2))


# inicializando display OLED
oled = SSD1306_I2C(128, 64, i2c)

# Teste OLED
oled.fill(0)  # Limpar display

# imprimindo endereços I2C encontrados
oled.text("Enderecos I2C:", 0, 0)
for i, addr in enumerate([hex(i) for i in i2c.scan()]):
    oled.text(addr, 0, 10 + i * 10)

oled.show() # atualizar o display

# printar no terminal
print ([hex(i)for i in i2c.scan()])
