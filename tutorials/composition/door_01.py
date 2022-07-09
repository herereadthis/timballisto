"""Make Door class."""
# http://blog.thedigitalcatonline.com/blog/2014/08/20/
# python-3-oop-part-2-classes-and-members/

a = 1
# a is an instance of the int class
print(type(a))
# >>> <class 'int'>

# int class is an object: an instance of the type class
print(type(int))
# >>> <class 'type'>

# Basically, everything in Python is an object


class Door:
    """Keep this simple."""

    # color is not defined on the constructor (not defined for each instance)
    # so this variable is shared amongst all instances
    color = 'brown'

    def __init__(self, number, status):
        """Initialize."""
        self.number = number
        self.status = status

    def open(self):
        """Open door."""
        self.status = 'open'

    def close(self):
        """Close Door."""
        self.status = 'closed'


# door1 is an instance of Door
door1 = Door(1, 'closed')

print('\nDemo Door instances.')

print(type(door1))
# >>> <class '__main__.Door'>
print(door1.status)
# >>> closed

door1.open()
print(door1.status)
# >>> open

door2 = Door(2, 'closed')

print('\nDemo Door shared color attribute.')

print(door1.color)
# >>> brown
print(door2.color)
# >>> brown

Door.color = 'white'
# shared value amongst all instances of Door
print(door1.color)
# >>> white
print(door2.color)
# >>> white

# these are all same memory address
print(id(Door.color))
print(id(door1.color))
print(id(door1.color))


print('\nDemo Door attritubes using python attributes.')

# get attributes
print(door1.__dict__)
# Note that color is not an attribute of door1
# >>> {'number': 1, 'status': 'closed'}
# this will traverse until it finds the attrubute
print(door1.__getattribute__('color'))
# >>> white
print(door1.__class__.__dict__['color'])
# >>> white


print('\nDemo functions and methods.')

# this is a BOUND method: linked to the instance
door1.open()
# Door.open() will not work
# this will work
Door.open(door1)

# this is a function because it is defined by the class
print(type(Door.open))
# >>> function

# this is a method because it is bound by the instance
print(type(door1.open))
# >>> method
