import RPi.GPIO as GPIO
import time

#blink logic
def blink(pin):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)
    return

#set the board
GPIO.setmode(GPIO.BOARD)

#set the output channel
GPIO.setup(6, GPIO.OUT)

for i in range(0,50):
    blink(6)
GPIO.cleanup()
