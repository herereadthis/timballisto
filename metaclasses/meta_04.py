"""Demo a meta class counting the number of instances of a class."""

import itertools


class InstanceCounterMeta(type):
    """Make instance counter not share count with descendants."""

    def __init__(cls, name, bases, attrs):
        """Call."""
        super().__init__(name, bases, attrs)
        cls._ids = itertools.count(1)


class MyClass(metaclass=InstanceCounterMeta):
    """Use singleton metaclass."""

    def __init__(self):
        self.id = next(self.__class__._ids)

my_first_class = MyClass()
my_second_class = MyClass()

print(id(my_first_class))
print(my_first_class.id)
# >>> 1
print(id(my_second_class))
print(my_second_class.id)
# >>> 2