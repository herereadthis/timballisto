"""Demo creation of decorator."""

from __future__ import print_function
from time import sleep


def my_decorator(some_function):
    """Fake a decorator."""
    def wrapper():
        """Wrap."""
        print("This happens BEFORE some_function() is called.")
        some_function()
        print("This happens AFTER some_function() is called.")

    return wrapper


def just_some_function():
    """Demo."""
    print("Wheee!")


just_some_function = my_decorator(just_some_function)
just_some_function()
# >>> This happens BEFORE some_function() is called.
# >>> Wheee!
# >>> This happens AFTER some_function() is called.


def another_decorator(some_function):
    """Fake a decorator."""
    def wrapper():
        """Wrap."""
        num = 10

        if num == 10:
            print("Yes!")
        else:
            print("No!")
        some_function()
        print("This happens AFTER some_function() is called.")

    return wrapper


def just_another_function():
    """Demo."""
    print("Whoa!")


just_another_function = another_decorator(just_another_function)
just_another_function()
# >>> Yes!
# >>> Whoa!
# >>> This happens AFTER some_function() is called.


@another_decorator
def third_function():
    """Demo."""
    print("Lorem!")


third_function()
# >>> Yes!
# >>> Lorem!
# >>> This happens AFTER some_function() is called.


def sleep_decorator(function):
    """Limit how fast the function is called."""
    def wrapper(*args, **kwargs):
        """Sleep."""
        sleep(0.25)
        """Pass the function down with all its arguments and kw args."""
        return function(*args, **kwargs)
    return wrapper


@sleep_decorator
def print_number(num):
    """Print."""
    return num


print(print_number(222))

for num in range(1, 4):
    print(print_number(num))
# >>> 1
# >>> 2
# >>> 3
# >>> 4
