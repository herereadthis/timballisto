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


# Classes are objects


class MyClass:
    """Pass."""

    pass


print('\nyou can print a class')
print(MyClass)
# >>> <class '__main__.MyClass'>


def echo(the_object):
    """Print the object."""
    print(the_object)


print('\nYou can pass a class as a function parameter')
echo(MyClass)
# >>> <class '__main__.MyClass'>

print('\nYou can add attributes to a class')
print(hasattr(MyClass, 'foo'))
MyClass.foo = 'bar'
# >>> False
print(hasattr(MyClass, 'foo'))
# >>> True
print(MyClass.foo)
# >>> bar

print('\nYou assign a class to a variable')
MyMirroredClass = MyClass
print(MyMirroredClass.foo)
# >>> bar
MyMirroredClass.foo = 'rum'
print(MyClass.foo == 'rum')
# >>> True

print(type(MyClass))
# >>> <type 'type'>
my_class = MyClass()
print(my_class)
# >>> <__main__.MyClass object at 0x102b1c400>
print(type(MyClass()))
# >>> <class '__main__.MyClass'>


print('\ntype is what\'s used to create a class.')
