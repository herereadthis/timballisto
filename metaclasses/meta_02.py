"""Do more meta."""

MyManualClass = type('MyManualClass', (), {})

print(MyManualClass)
# >>> <class '__main__.MyManualClass'>
bar = MyManualClass()
print(bar)
# >>> <__main__.MyManualClass object at 0x10adfcbe0>


class MyClass:
    """Pass."""

    pass


print(MyClass)
# >>> <class '__main__.MyClass'>

MyOtherManualClass = type('MyFooClass', (), {})

print(MyOtherManualClass)
# >>> <class '__main__.MyFooClass'>
foo = MyOtherManualClass()
print(foo)
# 0x10a5db4e0 is location of MyOtherManualClass instance in memory
# >>> <__main__.MyFooClass object at 0x10a5db4e0>

MyOtherManualClass = type('MyOtherManualClass', (), {'yum': True})
baz = MyOtherManualClass()

print(baz.yum)
# >>> True

# Demostrate how to instance a class from another class by type
MyManualChildClass = type('MyManualChildClass', (MyOtherManualClass, ), {
    'towel': True
})

fff = MyManualChildClass()
print(fff.yum)
# >>> True
