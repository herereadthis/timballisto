"""Demo evolutio of a public attribute."""


class MyClass:
    """Have my_attr attribute in the simplest implementation."""

    def __init__(self, a):
        """Initialize."""
        self.my_attr = a


if __name__ == '__main__':
    print('\nDemo initial implementation.')
    x = MyClass(10)
    print(x.my_attr)
    x.my_attr = 50
    print(x.my_attr)
    x.my_attr = -50
    print(x.my_attr)
    x.my_attr = 5000
    print(x.my_attr)


class MyClass:
    """Have my_attr limited between 0 and 1000."""

    def __init__(self, a):
        """Initialize."""
        self.my_attr = a

    @property
    def my_attr(self):
        """Get."""
        return self.__my_attr

    @my_attr.setter
    def my_attr(self, val):
        """Set."""
        if val < 0:
            self.__my_attr = 0
        elif val > 1000:
            self.__my_attr = 1000
        else:
            self.__my_attr = val


if __name__ == '__main__':
    print('\nSuppose many instances already made, demo setter restriction.')
    x = MyClass(10)
    print(x.my_attr)
    x.my_attr = 50
    print(x.my_attr)
    x.my_attr = -50
    print(x.my_attr)
    x.my_attr = 5000
    print(x.my_attr)
