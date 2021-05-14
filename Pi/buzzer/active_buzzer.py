import RPi.GPIO as GPIO
from time import sleep

class ActiveBuzzer():
    def __init__(self, pin):
        ''' pin represent the pin number connected to the pi,
        '''
        self.pin = pin

        #SET UP
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def send_high(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def send_low(self):
        GPIO.output(self.pin, GPIO.LOW)

'''
Example Usage
'''
# active_buzzer = ActiveBuzzer(21)
# try:
#     while True:
#         active_buzzer.send_high()
#         sleep(1)
#         active_buzzer.send_low()
#         sleep(1)
# except KeyboardInterrupt:
#     GPIO.cleanup()
    

