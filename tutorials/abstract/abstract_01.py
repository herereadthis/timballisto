"""Demo Abstract Base Classes."""
# http://blog.thedigitalcatonline.com/blog/2014/09/04/
# python-3-oop-part-6-abstract-base-classes/

from abc import ABCMeta


class MyABC(metaclass=ABCMeta):
    """Demo this."""

    pass


"""
The register() method is provided by the ABCMeta metaclass
sorta: tuple will be a subclass of MyABC (tuple inherits from MyABC)
the tuple class remains unchanged
registered types are stored in _abc_registry
"""
MyABC.register(tuple)

my_abc = MyABC()

print(issubclass(tuple, MyABC))
# >>> True
print(isinstance((), MyABC))
# >>> True

my_dict = {'a': 'b'}
my_tuple = ('a', 'b')

print('\ncheck is instance')
print(isinstance(my_dict, MyABC))
# >>> False
print(isinstance(my_tuple, MyABC))
# >>> True

print(MyABC.__class__.__instancecheck__)
# >>> <function ABCMeta.__instancecheck__ at 0x109646ae8>
print(MyABC.__class__.__instancecheck__(MyABC, my_dict))
# >>> False
print(MyABC.__class__.__instancecheck__(MyABC, ()))
# >>> True
print(MyABC.__class__.__instancecheck__(MyABC, my_tuple))
# >>> True

print(MyABC._abc_registry.data)
# >>> {<weakref at 0x10d829688; to 'type' at 0x10d43cdf0 (tuple)>}
