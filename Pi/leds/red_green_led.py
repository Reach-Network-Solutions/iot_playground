import RPi.GPIO as GPIO
from time import sleep

class RedGreenLed():
    ''' :red represent the red pin,
        :green represent the green pin,
    '''
    def __init__(self, red, green):
        self.red = red
        self.green = green

        #Setup
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.red, GPIO.OUT)
        GPIO.setup(self.green, GPIO.OUT)

    def red_on(self):
        '''
        Lights up the red led
        '''
        GPIO.output(self.red,GPIO.HIGH)

    def green_on(self):
        '''
        Lights up the green led
        '''
        GPIO.output(self.green,GPIO.HIGH)

    def red_off(self):
        '''
        Turns off the red led
        '''
        GPIO.output(self.red,GPIO.LOW)

    def green_off(self):
        '''
        Turns off the green led
        '''
        GPIO.output(self.green,GPIO.LOW)

'''
Example Usage
'''
# red_green = RedGreenLed(21,20)
# try:
#     while True:
#         red_green.red_on()
#         sleep(1)
#         red_green.red_off()

#         sleep(1)
#         red_green.green_on()
#         sleep(1)
#         red_green.green_off()
# except KeyboardInterrupt:
#     GPIO.cleanup()