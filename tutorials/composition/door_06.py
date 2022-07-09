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


class SecurityDoor:
    """Demo composition."""

    # Color has to be redefined all over again because it does not implicitly
    # come from Door class
    color = 'gray'
    locked = True

    def __init__(self, number, status):
        """Initialize."""
        # The door class is now part of Security Door as an attribute
        self.door = Door(number, status)

    def open(self):
        """Open the door."""
        if self.locked:
            return
        self.door.open()

    def close(self):
        """Close the door."""
        self.door.close()


sdoor = SecurityDoor(1, 'closed')

print(id(sdoor.color) == id(SecurityDoor.color))
# >>> True
print(id(Door.color) == id(sdoor.door.color))
# >>> True
