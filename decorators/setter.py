"""Demonstrate the pythonic way to do get and set."""


class SetterDecoratorClass:
    """show how to properly do get and set."""

    def __init__(self, x):
        """Initialize."""
        self.x = x

    @property
    def x(self):
        """Use property decorator to serve as the get."""
        return self.__x

    @x.setter
    def x(self, x):
        """Do logic for setter."""
        """
        In this setter, we want to say that instance.x = any number between 1
        and 1000. For all values over 1000, instance.x = 1000.
        The setter decorator allows us to say instance.x = 5000.
        We do this to prevent having to make a setter method
        e.g., my_instance.set_x(5000)
        """
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

if __name__ == "__main__":
    my_instance = SetterDecoratorClass(42)

    print(my_instance.x)
    # >>> 42
    my_instance.x = 500
    print(my_instance.x)
    # >>> 500
    my_instance.x = 1001
    print(my_instance.x)
    # 1000
