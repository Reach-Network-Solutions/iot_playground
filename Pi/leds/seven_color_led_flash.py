import RPi.GPIO as GPIO
from time import sleep

class SevenColorLedFlash():
    ''' 
    :pin represent the pin number connected to the pi
    '''
    def __init__(self, pin):
        self.pin = pin

        #Setup
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def led_on(self):
        ''' 
        :Turns the LED on
        '''
        GPIO.output(self.pin, GPIO.HIGH)

    def led_off(self):
        ''' 
        :Turns the LED off
        '''
        GPIO.output(self.pin, GPIO.LOW)

'''
Example Usage
'''
# seven_color_led = SevenColorLedFlash(20)

# try:
#     while True:
#         seven_color_led.led_on()
#         # sleep(2)
#         # seven_color_led.led_off()
# except KeyboardInterrupt:
#     GPIO.cleanup()