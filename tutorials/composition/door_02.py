"""Make Door class."""
# http://blog.thedigitalcatonline.com/blog/2014/08/20/
# python-3-oop-part-2-classes-and-members/


class Door:
    """Keep this simple."""

    color = 'brown'

    def __init__(self, number, status):
        """Initialize."""
        self.number = number
        self.status = status

    # Define a function that operates on the class instead of the instance
    # Class methods are functions that are bound to the class and not instance.
    # Decorator
    # cls argument is the class itself
    @classmethod
    def knock(cls):
        """Knock on door."""
        print("Knock!")

    # Paint method will change color of Door for all instances of Door
    @classmethod
    def paint(cls, colour):
        """Paint the door."""
        cls.colour = colour

    def open(self):
        """Open door."""
        self.status = 'open'

    def close(self):
        """Close Door."""
        self.status = 'closed'


door1 = Door(1, 'closed')
door2 = Door(2, 'closed')

print('\nDemo knock class method')

# knock is callable on both the instance and the class

print(door1.knock())
# >>> Knock!
print(Door.knock())
# >>> Knock!

print(Door.knock)
# >>> <bound method Door.knock of <class '__main__.Door'>>
print(door1.knock)
# >>> <bound method Door.knock of <class '__main__.Door'>>
print(type(Door.knock), type(door1.knock))
# >>> <class 'method'> <class 'method'>

print('\nDemo paint class method')

print(Door.color, door1.color, door2.color)
# >>> brown brown brown

# paint for all instances of Door
Door.paint('white')
print(Door.color, door1.color, door2.color)
# >>> white white white

# Remember, class methods are bound to the class, even when the instance calls
door1.paint('yellow')
print(Door.color, door1.color, door2.color)
# >>> yellow yellow yellow
