"""Demo staticmethod decorator."""

"""
A staticmethod is a method that knows nothing about the class or the instance
it was called on. It just gets the arguments that were passed, with no implicit
first argument. You would want to use it because it logically belongs in a
class but it doesn't require access to the class.
"""


class MyClass:
    """Demo staticmethod decorator."""

    def foo(self, x):
        """Demo instance method."""
        print('execute foo(%s%s) method' % (self, x))

    @staticmethod
    def static_foo(x):
        """Demo static method."""
        print('execute foo(%s) method' % (x))


my_object = MyClass()

my_object.foo('x')
# >>> execute foo(<__main__.MyClass object at 0x10f0dc6a0>x) method
my_object.static_foo('x')
# >>> execute foo(x) method
