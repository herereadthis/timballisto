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
        if self.locked:
            return
        # explicitly call parent method. This is bad news. Too much coupling!
        # If you change the parent class of SecurityDoor, you have to edit or
        # propogate the change dow to everything else
        # Also, you don't really know what is open() - is it Door.open(), or
        # open of Door's parent class?
        Door.open(self)


sdoor = SecurityDoor(1, 'closed')

print(sdoor.status)
# >>> closed

sdoor.open()
print(sdoor.status)
# >>> closed

sdoor.locked = False

sdoor.open()
print(sdoor.status)
# >>> open
