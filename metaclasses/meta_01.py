"""Explore metaclasses."""

a = 5
print(type(a))
# >>> <class 'int'>
print(a.__class__)
# >>> <class 'int'>
print(a.__class__.__bases__)
# >>> (<class 'object'>,)