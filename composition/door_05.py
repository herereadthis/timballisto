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
        # super() lets you avoid referring to the base class explicitly
        # it is a representation which acts like the parent
        super().open()


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
