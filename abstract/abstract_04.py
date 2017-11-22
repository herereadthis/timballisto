"""More on abstract classes."""

"""
AbstractClass isn't an abstract class because you can create an instance of it.
Subclass must implement the (abstract) methods of the parent abstract class.
MyClass does not show an implementation of do_something()
"""


class AbstractClass:
    """A simple class."""

    def do_something(self):
        pass


class MyClass(AbstractClass):
    """Subclass of abstract class."""
    pass

if __name__ == '__main__':
    a = AbstractClass()
    b = MyClass()