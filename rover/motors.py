import RPi.GPIO as gpio
from time import sleep

class Motor():
    def __init__(self, leftPin, rightPin, orientation="right"):
        #the pins are always regarded as right and left for the motor
        self.orientation = orientation
        if orientation == "right":
            self.activePin = rightPin
            self.groundPin = leftPin
        else:
            self.activePin = leftPin
            self.groundPin = rightPin
        
        gpio.setmode(gpio.BCM)

        gpio.setup(self.activePin, gpio.OUT)
        gpio.setup(self.groundPin, gpio.OUT)
        self.off(self.groundPin)
        self.off(self.activePin)
        
    def on(self, pin):
        gpio.output(pin, gpio.LOW)

    def off(self, pin):
        gpio.output(pin, gpio.HIGH)

    def move_forward(self):
        print("Moving motor forward...")
        #turn off ground PIN
        self.off(self.groundPin)
        #turn on active PIN
        self.on(self.activePin)
        sleep(5)
        #switch everything off
        self.off(self.groundPin)
        self.off(self.activePin)

    def move_backward(self):
        print("Moving motor backward...")
        #turn off active PIN
        self.off(self.activePin)
        #turn on ground PIN
        self.on(self.groundPin)
        sleep(5)
        #switch everything off
        self.off(self.activePin)
        self.off(self.groundPin)
        

motor = Motor(21, 20, "right")
motor.move_forward()
sleep(3)
motor.move_backward()

gpio.cleanup()