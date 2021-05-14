import RPi.GPIO as GPIO
from time import sleep

class MoistureSensor():
    def __init__(self, channel):
        '''
        :channel represent the DO input pin
        '''
        self.channel = channel
    
        #SET UP
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.channel, GPIO.IN)
        GPIO.add_event_detect(self.channel, GPIO.BOTH) #tells our script to listen to changes on the pin state
        GPIO.add_event_callback(self.channel, self.callback) #adds our callback funtion that is triggered when changes are detected


    def callback(self, channel):
        '''
        Callback is a function that will be called when there is change in DO pin state
        When moisture is present/detected DO sends a low signal,
        and when there is no moisture DO sends a high signal
        '''
        if GPIO.input(self.channel) == GPIO.HIGH:
            print ("No Moisture")
        
        else:
            print("Mositure Present")

'''
Example Usage
'''
# mositure = MoistureSensor(21)
# try :
#     while True:
#         sleep(1)
# except KeyboardInterrupt:
#     GPIO.cleanup()
    