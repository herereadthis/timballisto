"""Demo the singleton."""


class Singleton(type):
    """Make a singleton."""

    instance = None

    def __call__(cls, *args, **kw):
        """Call when class is instanced."""
        if not cls.instance:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.instance


class ASingleton(metaclass=Singleton):
    """Inherit singleton."""

    def __init__(self):
        """Initialize."""
        self.foo = 'bar'

a = ASingleton()
b = ASingleton()

print('\ntwo instances of a class are the same.')
print(a == b)
# >>> True
print(a.foo, b.foo)
# >>> bar bar
print(a.__class__.__name__, b.__class__.__name__)
# >>> ASingleton ASingleton


class BSingleton(metaclass=Singleton):
    """Inherit singleton."""

    pass

c = BSingleton()
d = BSingleton()
print(c == d)
# >>> True
print(c.__class__.__name__, d.__class__.__name__)
# BSingleton BSingleton
print(c == a)
# >>> False
