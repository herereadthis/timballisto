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

In most languages, a class is something that describes how to produce an object. In Python, classes are objects too. This means that with a class you can

* assign it to a variable
* copy it, 
* add attributes to it
* pass it as a function parameter

```python
class MyClass():
    pass


print(MyClass)
# >>> <class '__main__.MyClass'>
```

Type is what is used to create a class

```
type(name of the class, 
     tuple of the parent class (for inheritance, can be empty), 
     dictionary containing attributes names and values)
```