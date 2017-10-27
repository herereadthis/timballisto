"""Demo staticmethod decorator."""

"""
A classmethod is a method that belongs to the class and not to an instance.
You can call the classmethod from the class or from the instance. Any that
happens to the class with a classmethod will affect all instances.
"""


class MyClass:
    """Demo staticmethod decorator."""

    fruit = 'raspberry'

    def __init__(self, vegetable='carrot'):
        """Initialize."""
        self.vegetable = vegetable

    def foo(self, vegetable):
        """Demo instance method."""
        self.vegetable = vegetable

    @classmethod
    def class_foo(cls, fruit_name):
        """Demo class method."""
        cls.fruit = fruit_name


my_first = MyClass()
my_second = MyClass()

print('\nCreate instances')
print(my_first.fruit, my_first.vegetable)
# >>> raspberry carrot
print(my_second.fruit, my_second.vegetable)
# >>> raspberry carrot
print(MyClass.fruit)
# >>> raspberry

print('\nRun instance method')
my_first.foo('green beans')
my_second.foo('turnip')
print(my_first.fruit, my_first.vegetable)
# >>> raspberry green beans
print(my_second.fruit, my_second.vegetable)
# >>> raspberry turnip

print('\nRun class method from instance')
my_first.class_foo('apple')
print(my_first.fruit == my_second.fruit)
# >>> True
print(MyClass.fruit)
# >>> apple

print('\nRun class method from class')
MyClass.class_foo('peach')
print(my_first.fruit == my_second.fruit)
# >>> True
print(MyClass.fruit)
# >>> peach
