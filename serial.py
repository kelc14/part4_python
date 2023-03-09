"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    Attributes 
    ----------
    start: int 
    the number passed in by the user from which the serial numbers begin incrementing

    count: int
    current value that the generate function has reached

    initial: int 
    start value at time of initialization 
    
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

    def __init__(self, start):
        self.count = start
        self.initial = start
    
    def __repr__(self):
        return f"<SerialGenerator start={self.initial} current={self.count}>"
    
    
    def generate(self):
        """Generate a serial number one higher than the previous number"""
        self.count = self.count + 1
        return self.count
    
    def reset(self):
        """Reset the serial number to the value provided at intialization"""
        self.count = self.initial

    
    

