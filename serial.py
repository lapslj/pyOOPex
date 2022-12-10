"""Python serial number generator."""

class SerialGenerator:
    def __init__(self,start=100,counter=0):
        self.start = start
        self.counter = counter

    def generate(self):
        new_number = self.start + self.counter
        self.counter += 1
        return new_number
    
    def reset(self):
        self.counter = 0

    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

