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

`type` is what is used to create a class. `type` is the metaclass Python uses to create all classes

```
type(name of the class, 
     tuple of the parent class (for inheritance, can be empty), 
     dictionary containing attributes names and values)
```

```python
MyManualClass = type('MyManualClass', (), {})


**Metaclasses are the stuff that creates classes.**

Classes are what creates objects. In python, classes themselves are objects. Metaclasses are what creates those objects

```python
MyClass = MetaClass()
my_object = MyClass()
```

```python
# Show that everything in Python is an object, and
# the class that creates those objects are the type metaclass.

# INTEGERS
my_integer = 10
print(my_integer.__class__)
# >>> <class 'int'>
print(int.__class__)
# >>> <class 'type'>
print(my_integer.__class__.__class__)
# >>> <class 'type'>

# STRINGS
my_string = 'hello world'
print(my_string.__class__)
# >>> <class 'str'>
print(str.__class__)
# >>> <class 'type'>
print(my_string.__class__.__class__)
# >>> <class 'type'>

# FUNCTIONS
def my_function():
    return ''
print(my_function.__class__)
# >>> <class 'function'>
print(my_function.__class__)
# >>> <class 'type'>
print(my_function.__class__.__class__)
# >>> <class 'type'>

# CLASSES
class MyClass:
    yum = 'yummy'

my_class = MyClass()
print(my_class.__class__)
# >>> <class '__main__.MyClass'>
print(MyClass.__class__)
# >>> <class 'type'>
print(my_class.__class__.__class__)
# >>> <class 'type'>
```