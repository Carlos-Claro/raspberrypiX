import RPi.GPIO as GPIO

LedPin1 = 12    # pin12 --- led
LedPin2 = 16    # pin16 --- led
BtnPin1 = 18    # pin18 --- button
BtnPin2 = 22    # pin22 --- button

GPIO.setmode(GPIO.BOARD)
GPIO.setup([LedPin1, LedPin2], GPIO.OUT)   # Pino de led como sada
GPIO.setup(BtnPin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Pino do boto como sada e aciona o pull-up
GPIO.setup(BtnPin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output([LedPin1, LedPin2], GPIO.LOW) # Desliga o led

# Loop principal
print('Pressione Ctrl+C para sair')
try:
    out1 = False
    out2 = False
    while True:
        if GPIO.wait_for_edge(BtnPin1, GPIO.RISING, timeout=2000):
            print('Borda detectada no botao 1...')
            out1 = not out1
            GPIO.output(LedPin1, out1)
        if GPIO.wait_for_edge(BtnPin2, GPIO.FALLING, timeout=2000):
            print('Borda detectada no botao 2...')
            out2 = not out2
            GPIO.output(LedPin2, out2)

except KeyboardInterrupt:
    # Ctrl+C foi pressionado
    pass

GPIO.output([LedPin1, LedPin2], 0)
GPIO.cleanup()  # Limpa configurao
