"""Demo @property Decorator."""

# @property turns a method into descriptor object


class MyClass:
    """Demo @property."""

    def __init__(self, my_string):
        """Initialize."""
        self.my_class_var = my_string

    def get_function(self):
        """Get my class variable."""
        return self.my_class_var

    @property
    def get_property(self):
        """Get my class variable as object."""
        return self.my_class_var


my_object = MyClass('hello world')

print(my_object.get_function())
# >>> hello world

print(my_object.get_function)
# >>> <bound method myClass.get_function of <__main__.myClass object at ###>>


print(my_object.get_function.__class__)
# >>> <class 'method'>

# notice how this is not a function
print(my_object.get_property)
# >>> hello world

print(my_object.get_property.__class__)
# >>> <class 'str'>
