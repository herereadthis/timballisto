"""Demo __new__() vs __init__()."""


class MyClass():
    """Demo __new__() vs __init__()."""

    def __new__(cls, *args, **kwds):
        """Do new."""
        obj = super().__new__(cls, *args, **kwds)
        # this is where code goes.
        print('hi! do this when class is instanced.')
        return obj

    def __init__(self):
        """Initialize."""
        print('hi! do this to initialize class.')


my_class_1 = MyClass()
my_class_2 = MyClass()
