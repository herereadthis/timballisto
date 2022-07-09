"""More on abstract classes."""

"""
AbstractClass isn't an abstract class because you can create an instance of it.
Subclass must implement the (abstract) methods of the parent abstract class.
MyClass does not show an implementation of do_something()
"""

from abc import ABC, abstractmethod


class AbstractClass(ABC):
    """A simple class."""

    @abstractmethod
    def do_something(self):
        """Demo abstract method."""
        print('from the abstract method')


class MyClass(AbstractClass):
    """Subclass of abstract class."""

    def do_something(self):
        """Demo subclass method."""
        super().do_something()
        print('from the sub class')


if __name__ == '__main__':
    a = MyClass()
    a.do_something()
    # >>> from the abstract method
    # >>> from the sub class
