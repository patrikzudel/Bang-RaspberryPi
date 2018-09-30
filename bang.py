import RPi.GPIO as GPIO
from time import sleep
import random
import os
import sys
from threading import Thread

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.OUT, initial = False)
GPIO.setup(23, GPIO.OUT, initial= False)
GPIO.setup(25, GPIO.OUT, initial= False)

player1 = 23
player2 = 12
button1 = 18
button2 = 21
zelena = 25
menuExit = 0
body = 0
body1 = 0
body2 = 0
tlacidlo = 0

def blink(n):
    for x in range(n):
        GPIO.output(23, True)
        sleep(1)
        GPIO.output(23, False)
 
try:
    while menuExit == 0:
        if(menuExit == 0):
            #Ked stlacis button menu skonci
            if (GPIO.input(button1) == 0 or GPIO.input(button2) == 0):
                menuExit += 1
            else:
                GPIO.output(player1, True)
                sleep(0.5)
                GPIO.output(player1, False)
                sleep(0.5)
                GPIO.output(player2, True)
                sleep(0.5)
                GPIO.output(player2, False)
                sleep(0.5)
            
    if(menuExit > 0) :
        GPIO.output(zelena, True)
        sleep(2)
        GPIO.output(zelena, False)
        
    while body != 5:
        tlacidlo = 0;
        sleep(random.uniform(2,4))
        GPIO.output(zelena, True)
        while tlacidlo < 1:
            if (GPIO.input(button1) == 0):
                tlacidlo += 1
                body1 += 1
                body = body1
                GPIO.output(player1, True)
                GPIO.output(zelena, False)
                sleep(2)
                if body1 == 1:
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                if body1 == 2:
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                    sleep(0.5)
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                if body1 == 3:
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                    sleep(0.5)
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                    sleep(0.5)
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                if body1 == 4:
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                    sleep(0.5)
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                    sleep(0.5)
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                    sleep(0.5)
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                if body1 == 5:
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                    sleep(0.5)
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                    sleep(0.5)
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                    sleep(0.5)
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                    sleep(0.5)
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
            if (GPIO.input(button2) == 0):
                tlacidlo += 1
                body2 += 1
                body = body2
                GPIO.output(player2, True)
                GPIO.output(zelena, False)
                sleep(2)
                if body2 == 1:
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                if body2 == 2:
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                    sleep(0.5)
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                if body2 == 3:
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                    sleep(0.5)
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                    sleep(0.5)
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                if body2 == 4:
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                    sleep(0.5)
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                    sleep(0.5)
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                    sleep(0.5)
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                if body2 == 5:
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                    sleep(0.5)
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                    sleep(0.5)
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                    sleep(0.5)
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
                    sleep(0.5)
                    GPIO.output(zelena, True)
                    sleep(0.5)
                    GPIO.output(zelena, False)
        sleep(1)
        GPIO.output(player1, False)
        GPIO.output(player2, False)
        sleep(1)
    os.execl(sys.executable, sys.executable, *sys.argv)
        
finally:
    GPIO.cleanup()
