# Metaclasses

* everything in Python is an object, because everything inherits from `object`.

* everything is the instance of a class
* `type` is the class that is instanced to get classes

* `object` is the base of every object,
* `type` is the class of every type

```python
print(type(object))
# >>> <class 'type'>
print(type(object))
# >>> <class 'type'>
print(type.__bases__)
# >>> (<class 'object'>,)

print(object.__class__)
# >>> <class 'type'>
print(type.__class__)
# >>> <class 'type'>
```