import RPi.GPIO as GPIO
from time import sleep

class MoistureSensor():
    def __init__(self, channel):
        self.channel = channel
    
        #SET UP
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.channel, GPIO.IN)
        GPIO.add_event_detect(self.channel, GPIO.BOTH)
        GPIO.add_event_callback(self.channel, self.callback)


    def callback(self, channel):
        if GPIO.input(self.channel) == GPIO.LOW:
            print("Moisture Detected")
        
        else:
            print("No Moisture")

mositure = MoistureSensor(21)

try :
    while True:
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    