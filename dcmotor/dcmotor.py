import RPi.GPIO as GPIO
import sys
import time
IN1 = 17    # pin11
IN2 = 18
IN3 = 27
IN4 = 22
value = 0

def setStep(w1, w2, w3, w4):
	GPIO.output(IN1, w1)
	GPIO.output(IN2, w2)
	GPIO.output(IN3, w3)
	GPIO.output(IN4, w4)

def Up():
    for i in range(10000):
        setStep(1, 0, 0, 0)
def Left():
    for i in range(10000):
	    setStep(0, 1, 0, 0)
def Down():
    for i in range(10000):
    	setStep(0, 0, 1, 0)
def Right():
    for i in range(10000):
    	setStep(0, 0, 0, 1)

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(IN1, GPIO.OUT)      # Set pin's mode is output
	GPIO.setup(IN2, GPIO.OUT)
	GPIO.setup(IN3, GPIO.OUT)
	GPIO.setup(IN4, GPIO.OUT)

def decision(mode):
    if mode == 1:
        Up()
    elif mode == 2:
        Left()
    elif mode == 3:
        Down()
    elif mode == 4:
        Right()

def destroy():
	GPIO.cleanup()             # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		decision(value)
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child function destroy() will be  executed.
		destroy()
