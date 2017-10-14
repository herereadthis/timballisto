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

    colour = 'gray'
    locked = True

    def open(self):
        """Open door."""
        if not self.locked:
            self.status = 'open'


door1 = Door(1, 'closed')
door2 = Door(2, 'closed')
