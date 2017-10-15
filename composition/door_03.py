"""Make Door class."""
# http://blog.thedigitalcatonline.com/blog/2014/08/20/
# python-3-oop-part-3-delegation-composition-and-inheritance/


class Door:
    """Keep this simple."""

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


class SecurityDoor(Door):
    """Inherit from Door class."""

    # Overrides Door.color
    color = 'gray'
    locked = True

    def open(self):
        """Open door."""
        # This will override Door.open()
        if not self.locked:
            self.status = 'open'


door1 = Door(1, 'closed')
door2 = SecurityDoor(2, 'closed')

print(door1.__dict__)
# >>> {'number': 1, 'status': 'closed'}
print(door2.__dict__)
# >>> {'number': 2, 'status': 'closed'}
print(id(door1.color) == id(Door.color))
# >>> True
print(id(door2.color) == id(SecurityDoor.color))
# >>> True



print(id(SecurityDoor.color))
print(id(Door.color))
