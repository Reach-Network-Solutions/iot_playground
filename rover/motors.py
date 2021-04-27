import RPi.GPIO as gpio
from time import sleep

class Motor():
    def __init__(self, leftPin, rightPin, orientation="right"):
        # The pins are always regarded as left and right respectively  for the motor
        # The right pin should always be connected to the ground NC connection
        # The left pin should always be connected to the live NO connection
        self.orientation = orientation
        if orientation == "right":
            self.activePin = rightPin
            self.groundPin = leftPin
        else:
            self.activePin = leftPin
            self.groundPin = rightPin
        
        gpio.setmode(gpio.BCM)

        # Set the PINs as output pins
        gpio.setup(self.activePin, gpio.OUT)
        gpio.setup(self.groundPin, gpio.OUT)

        # The pins always start in a high state
        # Set each pin to the low mode to reset them
        self.off(self.groundPin)
        self.off(self.activePin)
        
    def on(self, pin):
        # Simple on command to create abstraction for the confusing HIGH and LOW GPIO status
        gpio.output(pin, gpio.LOW)

    def off(self, pin):
        # Simple on command to create abstraction for the confusing HIGH and LOW GPIO status
        gpio.output(pin, gpio.HIGH)

    def move_forward(self):
        print("Moving motor forward...")
        # Ensure the ground PIN is off
        self.off(self.groundPin)
        # Turn on active PIN
        self.on(self.activePin)
        sleep(5)
        # Turn off every PIN
        self.off(self.groundPin)
        self.off(self.activePin)

    # Inverts the PINs to reverse the current
    def move_backward(self):
        print("Moving motor backward...")
        # Ensure the active PIN is off
        self.off(self.activePin)
        # Turn on ground PIN
        self.on(self.groundPin)
        sleep(5)
        #Turn off everything 
        self.off(self.activePin)
        self.off(self.groundPin)
        

motor = Motor(21, 20, "right")
motor.move_forward()
sleep(3)
motor.move_backward()

gpio.cleanup()