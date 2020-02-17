############################
# Conectar o lado positivo LED (anodo) ao pino 12 (GPIO 18) da RPi. O lado negativo conectar ao resistor e o outro lado do resistor ao terra (GND).
# Conectar o lado positivo do outro LED (anodo) ao pino 16 (GPIO 23) da RPi. O lado negativo conectar ao resistor e o outro lado do resistor ao terra (GND).
#   Conectar um lado do push button ao pino 18 (GPIO 24) da RPi e o outro lado ao terra (GND).
#   Conectar um lado do outro push button ao pino 22 (GPIO 25) e o outro lado ao 3.3V.#
###########################################
import RPi.GPIO as GPIO
import time

LedPin = 12    # pin12 --- led
BtnPin = 18    # pin12 --- button

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LedPin, GPIO.OUT)
GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(LedPin, GPIO.HIGH)

print('Pressione Ctrl+C para sair')
# Loop principal
try:
    while True:
        if GPIO.input(BtnPin) == GPIO.LOW:
            print('Liga o LED...')
            GPIO.output(LedPin, 1)
        else:
            print('Desliga o LED...')
            GPIO.output(LedPin, 0)
        # Aguarda um tempo
        time.sleep(1)

except KeyboardInterrupt:
    # Ctrl+C foi pressionado
    pass

GPIO.output(LedPin, 0)
GPIO.cleanup()  



