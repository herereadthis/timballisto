"""Demo usage of static method to create a counter for instances."""


class Robot:
    """Make a robot."""

    __counter = 0

    def __init__(self):
        """Initialize."""
        type(self).__counter += 1

    @staticmethod
    def robot_instances():
        """Return robot instances."""
        return Robot.__counter


if __name__ == "__main__":
    print(Robot.robot_instances())
    x = Robot()
    print(x.robot_instances())
    y = Robot()
    print(x.robot_instances())
    print(Robot.robot_instances())
