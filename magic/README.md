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

* `object.__class--` returns the object's class

* `object.__dict__` returns list of the object's attributes


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

