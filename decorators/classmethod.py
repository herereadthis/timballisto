"""Demo staticmethod decorator."""

from __future__ import print_function

# A classmethod is a method that belongs to the class and not to an instance.
# You can call the classmethod from the class or from the instance. Anything
# that happens to the class with a classmethod will affect all instances.


class MyClass(object):
    """Demo staticmethod decorator."""

    fruit = 'raspberry'

    def __init__(self, vegetable='carrot'):
        """Initialize."""
        self.vegetable = vegetable

    def foo_method(self, vegetable):
        """Demo instance method."""
        self.vegetable = vegetable

    @classmethod
    def class_foo(cls, fruit_name):
        """Demo class method."""
        cls.fruit = fruit_name


if __name__ == '__main__':
    MY_FIRST = MyClass()
    MY_SECOND = MyClass()

    print('\nCreate instances')
    print(MY_FIRST.fruit, MY_FIRST.vegetable)
    # >>> raspberry carrot
    print(MY_SECOND.fruit, MY_SECOND.vegetable)
    # >>> raspberry carrot
    print(MyClass.fruit)
    # >>> raspberry

    print('\nRun instance method')
    MY_FIRST.foo_method('green beans')
    MY_SECOND.foo_method('turnip')
    print(MY_FIRST.fruit, MY_FIRST.vegetable)
    # >>> raspberry green beans
    print(MY_SECOND.fruit, MY_SECOND.vegetable)
    # >>> raspberry turnip

    print('\nRun class method from instance')
    MY_FIRST.class_foo('apple')
    print(MY_FIRST.fruit == MY_SECOND.fruit)
    # >>> True
    print(MyClass.fruit)
    # >>> apple

    print('\nRun class method from class')
    MyClass.class_foo('peach')
    print(MY_FIRST.fruit == MY_SECOND.fruit)
    # >>> True
    print(MyClass.fruit)
    # >>> peach
