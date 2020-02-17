#Programa : Raspberry push button e leds
#Autor : FILIPEFLOP

import RPi.GPIO as GPIO
import time


def main():  
    L1 = 5
    L2 = 6
    L3 = 13
    BTN = 10 
    CONTADOR = 0

    GPIO.setmode(GPIO.BCM)

   #Define os pinos dos leds como saida
    GPIO.setup(L1, GPIO.OUT)
    GPIO.setup(L2, GPIO.OUT)
    GPIO.setup(L3, GPIO.OUT)

    #Define o pino do botao como entrada
    GPIO.setup(BTN, GPIO.IN)

    #Apaga todos os leds
    GPIO.output(L1,1)
    GPIO.output(L2,1)
    GPIO.output(L3,1)
    time.sleep(2)
    GPIO.output(L1,0)
    GPIO.output(L2,0)
    GPIO.output(L3,0)


    while(1):
        #Verifica se o botao foi pressionado
        clique = GPIO.input(BTN)
        if clique == True:
            #Incrementa a variavel contador
            print(CONTADOR)
            CONTADOR = CONTADOR +1
            time.sleep(1)
            #Caso contador = 1, acende o led vermelho
        if CONTADOR == 1:
            GPIO.output(L1, 1)
            
        #Caso contador = 2, acende o led verde
        if CONTADOR == 2:
            GPIO.output(L2, 1)

        #Caso contador = 3, acende o led amarelo
        if CONTADOR == 3:
            GPIO.output(L3, 1)

            #Caso contador = 4, apaga todos os leds e
            #zera a variavel contador
        if CONTADOR == 4:
            GPIO.output( L1, 0)
            GPIO.output( L2, 0)
            GPIO.output( L3, 0)
            CONTADOR = 0


if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

