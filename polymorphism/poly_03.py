"""Demo polymorphism - duck typing."""


class Room:
    """Make Room class."""

    def __init__(self, door):
        """Initialize."""
        self.door = door

    def open(self):
        """Open room."""
        self.door.open()

    def close(self):
        """Close Room."""
        self.door.close()

    def is_open(self):
        """Tell whether the room is open."""
        return self.door.is_open()


class Door:
    """Do string door class."""

    def __init__(self):
        """Initialize."""
        self.status = "closed"

    def open(self):
        """Open door."""
        self.status = "open"

    def close(self):
        """Close door."""
        self.status = "closed"

    def is_open(self):
        """Tell whether the door is open."""
        return self.status == "open"


class BooleanDoor:
    """Do boolean door class."""

    def __init__(self):
        """Initialize."""
        self.status = True

    def open(self):
        """Open door."""
        self.status = True

    def close(self):
        """Close door."""
        self.status = False

    def is_open(self):
        """Tell whether the door is open."""
        return self.status


door = Door()
bool_door = BooleanDoor()
room = Room(door)
bool_room = Room(bool_door)

room.open()
print(room.is_open())
# >>> True
room.close()
print(room.is_open())
# >>> False

bool_room.open()
print(bool_room.is_open())
# >>> True
bool_room.close()
print(bool_room.is_open())
# >>> False
