#using infared sensor to turn on program
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT) #output pin
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor

while True:
    i = GPIO.input(11)
    if i==1: #no motion detected
        time.sleep(0.1)#run application/turn on screen
    time.sleep(2.5)