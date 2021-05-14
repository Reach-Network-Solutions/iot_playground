import RPi.GPIO as GPIO
from time import sleep

class PassiveBuzzer():
    ''' Passive BUzzer requires a 50-100PWM frequency 
        :pin represent the pin number connected to the pi,
        :frequnecy represent the signal frequency,
    '''
    def __init__(self, pin, frequency=50):
        self.pin = pin
        self.frequency = frequency

        # setting up the pin board mode, and pin
        # pin represent the output
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

        # setting up the PWM Frequency
        self.pwm = GPIO.PWM(self.pin, self.frequency)


    def send_signal(self):
        self.pwm.start(self.frequency)

    def change_frequency(self, frequency):
        self.pwm.ChangeFrequency(frequency)

'''
Example Usage
'''
# passive_buzzer = PassiveBuzzer(12, 10)

# try:
#     while True:
#         passive_buzzer.send_signal()
#         sleep(0.5)

#         passive_buzzer.change_frequency(500)
#         sleep(0.5)

#         passive_buzzer.change_frequency(1000)
#         sleep(0.5)

#         passive_buzzer.change_frequency(2000)
#         sleep(0.5)

#         passive_buzzer.change_frequency(3000)
#         sleep(0.5)

#         passive_buzzer.change_frequency(4000)
#         sleep(0.5)

#         passive_buzzer.change_frequency(5000)
#         sleep(0.5)
# except KeyboardInterrupt:
#     GPIO.cleanup()
