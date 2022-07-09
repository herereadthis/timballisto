"""Explore decorators."""


"""
The output of a function is a reference to an object.
Therefore, functions can return references to functions, because everything is
an object.
"""


def f(x):
    """Return a function."""
    def g(y):
        return y + x + 3
    return g

nf1 = f(1)
nf2 = f(3)

print(nf1(1))
print(nf2(1))


def my_decorator(func):
    """Create a simple decorator."""
    def function_wrapper(x):
        print('Before calling {}'.format(func.__name__))
        """The function is the parameter."""
        func(x)
        print('After calling {}'.format(func.__name__))
    return function_wrapper


def foo(x):
    print("Hi, foo has been called with " + str(x))

@my_decorator
def bar(x):
    print("Hi, bar has been called with " + str(x))

print("\n***Call foo before decoration:\n")
foo("Hi")

print("\n***Decorate foo with f:\n")
# This is not a good design pattern. Now there are two versions of foo, one
# before and one after decoration.
foo = my_decorator(foo)

print("\n***Call foo after decoration:\n")
foo(42)


print("\n***Call decorated bar:\n")
bar(73)
