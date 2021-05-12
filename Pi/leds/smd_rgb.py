import RPi.GPIO as GPIO
from time import sleep

class SmdRgB():
    ''' :red represent the red pin,
        :green represent the green pin,
        :blue represent the blue pin,
    '''
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

        # setting up the pin board mode, and pin
        # all the Leds represent outputs
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.red, GPIO.OUT)
        GPIO.setup(self.green, GPIO.OUT)
        GPIO.setup(self.blue, GPIO.OUT)

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

    def blue_on(self):
        '''
        Lights up the blue led
        '''
        GPIO.output(self.blue,GPIO.HIGH)

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

    def blue_off(self):
        '''
        Turns off the blue led
        '''
        GPIO.output(self.blue,GPIO.LOW)

'''
Example Usage
'''
# smg_led = SmdRgB(21, 20, 16)

# try:
#     while True:
#         smg_led.red_on()
#         smg_led.green_off()
#         smg_led.blue_off()
#         sleep(0.05)

#         smg_led.red_off()
#         smg_led.green_on()
#         smg_led.blue_off()
#         sleep(0.05)

#         smg_led.red_off()
#         smg_led.green_off()
#         smg_led.blue_on()
#         sleep(0.05)
# except KeyboardInterrupt:
#     GPIO.cleanup()

