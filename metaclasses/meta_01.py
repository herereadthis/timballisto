"""Explore metaclasses."""

a = 5
print(type(a))
# >>> <class 'int'>
print(a.__class__)
# >>> <class 'int'>
print(a.__class__.__bases__)
# >>> (<class 'object'>,)

print('\ntest type')
print('type(object)', type(object))
# >>> <class 'type'>
print('type(type)', type(type))
# >>> <class 'type'>
print('type.__bases__', type.__bases__)
# >>> (<class 'object'>,)

print('\ntest __class__')
print('object.__class__', object.__class__)
# >>> <class 'type'>
print('type.__class__', type.__class__)
# >>> <class 'type'>
