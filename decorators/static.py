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
        print('execute foo(%s%s) method' % (self, x))

    @classmethod
    def class_foo(cls, x):
        print('execute foo(%s%s) method' % (cls, x))

    @staticmethod
    def static_foo(x):
        print('execute foo(%s) method' % (x))


my_object = MyClass()

my_object.foo('x')
my_object.class_foo('x')
my_object.static_foo('x')