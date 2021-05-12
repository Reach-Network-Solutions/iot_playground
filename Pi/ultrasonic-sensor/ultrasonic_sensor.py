import RPi.GPIO as GPIO
import time

class UltrasonicSensor():
    ''' :trig represent the trigger pin,
        :echo represent the echo pin,
        :signal_time represent the time for each signal burst to be sent.
    '''
    def __init__(self, trig, echo, signal_time):
        self.trig = trig
        self.echo = echo
        self.signal_time = signal_time

        # seting up the pin board mode, and pin
        # TRIG sends the Output signal
        # ECHO receives the Input 
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    #Sends a Hign signal from the trigger
    def trigger_high(self):
        GPIO.output(self.trig, GPIO.HIGH)

    #Sends a Low signal from the trigger
    def trigger_low(self):
        GPIO.output(self.trig, GPIO.LOW)

    def send_signal(self):

        ''' Sends a high and a low signal from the trigger pin,
            at a certain interval set by the signal_time.
        '''

        self.trigger_high()
        time.sleep(self.signal_time)
        self.trigger_low()

    #Calculates the distance taken by the signal. Use a constant of 17150 for cm
    def calculate_distance(self):
        pulse_duration = self.end_time - self.start_time
        distance = pulse_duration * 17150
        return distance

    #Gets the duration of the pulse sent by the trigger and received by the echo
    def signal_duration(self):
        while GPIO.input(self.echo) == 0:
            self.start_time = time.time()

        while GPIO.input(self.echo) == 1:
            self.end_time = time.time()


    #Gets the signal duration and call calculate distacne function retuning the distance
    def distance(self):

        ''' Calls the :signal_duration() function to get the signal duration and 
            Calls the :calculate_distance() function that calculates the 
            disance and sends the response
        '''

        self.signal_duration()

        return self.calculate_distance()
    

'''
Example Usage
'''
# sensor = UltrasonicSensor(21, 20, 0.0005)

# try :
#     while True:
#         sensor.send_signal()
#         print(sensor.distance())
# except KeyboardInterrupt:
#     GPIO.cleanup