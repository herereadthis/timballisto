# Magic Attributes

```python
# show all types
dir(type)

[
    '__abstractmethods__',
    '__base__',
    '__bases__',
    '__basicsize__',
    '__call__',
    '__class__',
    '__delattr__',
    '__dict__',
    '__dictoffset__',
    '__doc__',
    '__eq__',
    '__flags__',
    '__format__',
    '__ge__',
    '__getattribute__',
    '__gt__',
    '__hash__',
    '__init__',
    '__instancecheck__',
    '__itemsize__',
    '__le__',
    '__lt__',
    '__module__',
    '__mro__',
    '__name__',
    '__ne__',
    '__new__',
    '__reduce__',
    '__reduce_ex__',
    '__repr__',
    '__setattr__',
    '__sizeof__',
    '__str__',
    '__subclasscheck__',
    '__subclasses__',
    '__subclasshook__',
    '__weakrefoffset__',
    'mro'
 ]
 ```

* `class.__bases__` returns the object's base classes, in order of occurance
* `object.__class__` returns the object's class
* `object.__dict__` returns list of the object's attributes
* `object.__str__` returns object a string that tries to be readable (is whatever you think is that object in text form)
* `object.__repr__` returns object a string that tries to unambiguous (representation of python object usually eval will convert it back to that object)


```python
import sys
dir(type(sys))

[
    '__class__',
    '__delattr__',
    '__dict__',
    '__doc__',
    '__format__',
    '__getattribute__',
    '__hash__',
    '__init__',
    '__new__',
    '__reduce__',
    '__reduce_ex__',
    '__repr__',
    '__setattr__',
    '__sizeof__',
    '__str__',
    '__subclasshook__'
]
```

* `def __new__():` is the method called before `__init__` It's rarely used for classes, unless you want to control how the object is created, perforn actions needed when creating an instance.
* `def __init__():` initializes an object - this is the constructor.
* `def __del__():` the destructor - rarely used called when object is destroyed.
* `def __call__():` called whenever we instance the class

