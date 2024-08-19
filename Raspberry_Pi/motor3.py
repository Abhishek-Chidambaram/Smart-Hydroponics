import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)
GPIO.setwarnings(False)
try:
	while True:
		GPIO.output(13,GPIO.LOW)
		time.sleep(5)
		GPIO.output(13,GPIO.HIGH)

except KeyboardInterrupt:
        pass

finally:
    GPIO.cleanup() 
