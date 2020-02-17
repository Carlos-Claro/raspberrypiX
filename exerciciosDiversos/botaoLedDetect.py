import RPi.GPIO as GPIO
import time

LedPin1 = 12    # pin12 --- led
LedPin2 = 16    # pin16 --- led
BtnPin1 = 18    # pin18 --- button
BtnPin2 = 22    # pin22 --- button

GPIO.setmode(GPIO.BOARD)       # Pinagem fsica
GPIO.setup([LedPin1, LedPin2], GPIO.OUT)   # Pino de led como sada
GPIO.setup(BtnPin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Pino do boto como sada e aciona o pull-up
GPIO.setup(BtnPin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.output([LedPin1, LedPin2], GPIO.LOW) # Desliga o led

out1 = False
out2 = False

# Funcao de callback para botao 1
def callback_bt_1(channel):
    global out1
    print('Botao 1 pressionado...')
    out1 = not out1
    GPIO.output(LedPin1, out1)

# Funcao de callback para botao 2
def callback_bt_2(channel):
    global out2
    print('Botao 2 pressionado...')
    out2 = not out2
    GPIO.output(LedPin2, out2)

# Registra funcoes de callback
GPIO.add_event_detect(BtnPin1, GPIO.RISING, callback=callback_bt_1, bouncetime=200)
GPIO.add_event_detect(BtnPin2, GPIO.RISING, callback=callback_bt_2, bouncetime=200)

# Loop principal
print('Pressione Ctrl+C para sair')
try:
    while True:
        print('Aguardando evento...')
        time.sleep(5)
except KeyboardInterrupt:
    # Ctrl+C foi pressionado
    pass

GPIO.output([LedPin1, LedPin2], 0)
GPIO.cleanup()  # Limpa configurao
