"""Demo usage of static method to create a counter for instances."""


class Robot:
    """Make a robot."""

    __counter = 0

    def __init__(self):
        """Initialize."""
        type(self).__counter += 1

    @staticmethod
    def robotInstances():
        """Return robot instances."""
        return Robot.__counter


if __name__ == "__main__":
    print(Robot.robotInstances())
    x = Robot()
    print(x.robotInstances())
    y = Robot()
    print(x.robotInstances())
    print(Robot.robotInstances())
