"""Create metaclasses."""


class UpperAttrMetaclass1(type):
    """Create the metaclass class."""

    def __new__(cls, future_class_name,
                future_class_parents, future_class_attr):
        """Convert all attributes to uppercase."""
        # cls is upperattr_metaclass.
        uppercase_attr = {}
        for name, val in future_class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        """
        don't do this.
        return type.__new__(upperattr_metaclass, future_class_name,
                            future_class_parents, uppercase_attr)
        """
        # reuse the type.__new__ method
        # this is basic OOP, nothing magic in there
        return type.__new__(cls, future_class_name,
                            future_class_parents, uppercase_attr)


class UpperAttrMetaclass2(type):
    """Use shorter param names."""

    def __new__(cls, clsname, bases, dct):
        """Convert all attributes to uppercase."""
        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return type.__new__(cls, clsname, bases, uppercase_attr)


class UpperAttrMetaclass(type):
    """Use super to clean up inheritance."""

    def __new__(cls, clsname, bases, dct):
        """Convert all attributes to uppercase."""
        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases,
                                                      uppercase_attr)


class MyClass(metaclass=UpperAttrMetaclass):
    """Do with a metaclass."""

    bar = 'baz'


my_class = MyClass()
print(hasattr(MyClass, 'bar'))
# >>> False
print(hasattr(MyClass, 'BAR'))
# >>> True
print(hasattr(my_class, 'bar'))
# >>> False
print(hasattr(my_class, 'BAR'))
# >>> True
