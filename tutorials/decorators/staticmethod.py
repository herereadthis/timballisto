"""Demo staticmethod decorator."""

from __future__ import print_function

"""
A staticmethod is a method that knows nothing about the class or the instance
it was called on. It just gets the arguments that were passed, with no implicit
first argument. You would want to use it because it logically belongs in a
class but it doesn't require access to the class.
"""


class MyClass(object):
    """Demo staticmethod decorator."""

    def foo_method(self, input_str):
        """Demo instance method."""
        print('execute foo_method(%s%s) method' % (self, input_str))

    @staticmethod
    def static_foo(input_str):
        """Demo static method."""
        print('execute static_foo(%s) method' % (input_str))


if __name__ == '__main__':
    MY_INSTANCE = MyClass()

    MY_INSTANCE.foo_method('x')
    # >>> execute foo_method(<__main__.MyClass object at 0x10f0dc6a0>x) method
    MY_INSTANCE.static_foo('x')
    # >>> execute static_foo(x) method
