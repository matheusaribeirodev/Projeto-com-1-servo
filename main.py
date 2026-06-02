import machine
import ssd1306
import time
 
led_vermelho = machine.Pin(25, machine.Pin.OUT)
led_verde = machine.Pin(26, machine.Pin.OUT)
 
botao_verde = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
botao_azul = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
 
i2c = machine.I2C(0, scl=machine.Pin(22), sda=machine.Pin(21))
 
oled_largura = 128
oled_tamanho = 64
 
oled = ssd1306.SSD1306_I2C(oled_largura, oled_tamanho, i2c)
 
 
servo = machine.PWM(machine.Pin(18))
servo.freq(50)
 
 
def mover_servo(angulo):
    pmin = 26
    pmax = 128
 
    calculo = int(pmin + (angulo / 180) * (pmax - pmin))
    servo.duty(calculo)
mover_servo(90)
 
while True:
    if botao_azul.value() == 0:
        oled.fill(0)
        oled.text("Luz acesa", 0, 10)
        oled.show()
        led_verde.on()
        time.sleep(0.15)
        led_verde.off()
        mover_servo(0)
    if botao_verde.value() == 0:
        oled.fill(0)
        oled.text("luz apagada", 0, 10)
        oled.show()
        led_vermelho.on()
        time.sleep(0.15)
        led_vermelho.off()
        mover_servo(90)
    time.sleep(0.1)