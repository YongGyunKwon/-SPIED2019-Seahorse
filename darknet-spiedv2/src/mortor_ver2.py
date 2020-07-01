import Jetson.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
#GPIO.cleanup()
#int = 0
#while(1):
GPIO.output(32, GPIO.HIGH)
GPIO.output(19, GPIO.HIGH)
GPIO.output(21, GPIO.LOW)
time.sleep(2)
GPIO.output(19, GPIO.LOW)
GPIO.output(21, GPIO.LOW)
	#time.sleep(1)
	#int+=1
	#if(int>3):
		#break
GPIO.cleanup()
