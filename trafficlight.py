#making of traffic light using raspberry pi
#using for loops and sleep time
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pin_1 = 4
led_pin_2 = 15
led_pin_3 = 18
GPIO.setup(led_pin_1, GPIO.OUT)
GPIO.setup(led_pin_2, GPIO.OUT)
GPIO.setup(led_pin_3, GPIO.OUT)


for i in range(1):
    GPIO.output(led_pin_1, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(led_pin_1, GPIO.LOW)
    time.sleep(0.5)


for i in range(1):
    GPIO.output(led_pin_2, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(led_pin_2, GPIO.LOW)
    time.sleep(0.5)
    
for i in range(1):
    GPIO.output(led_pin_3, GPIO.HIGH)
    time.sleep(10)
    GPIO.output(led_pin_3, GPIO.LOW)
    time.sleep(0.5)

GPIO.cleanup()
