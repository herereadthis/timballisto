# Abstract Base Classes

* Invocation: interacting with an object by calling its methods
* Polymorphism: invoking a method may run different code depending on type of an object
* Inspection: ability for code to examine the type or properties of an object

* In basic OOP theory, Invocation is preferred usage pattern.
* Inspection is discouraged because it comes from older procedural patterns
* However don't be too dogmatic and inflexible

## EAFP - Easier to Ask for Forgiveness than Permission

* Trust the incoming objects to provide the attributes and methods you need.
* It's up to you to manage the exceptions

Suppose you are interested if an object acts like a list, but then you have to work on all possible list methods...

```python
# This is typical EAFP pattern
# it is trying to access (but not call) methods of list type, so that if they
# are not present, it will raise AttributeError
try:
    obj.append
    obj.count
    obj.extend
    obj.index
    obj.insert
    [...etc...]
except AttributeError:
    [...]


# Here is a better way to do it:
class FakeList:
    def fakemethod(self):
        pass

    def __getattr__(self, name):
        if name in ['append', 'count', 'extend', 'index', 'insert', ...]:
            return self.fakemethod
```

* To check type, use `isInstance()` instead of `type()` because `isInstance()` returns a boolean.

```python
print(isinstance([], list))
# >>> True
print(isinstance(1, int))
# >>> True
print(isinstance(1, object))
# >>> True
print(issubclass(int, object))
# >>> True

class Door:
    pass

door = Door()
print(isinstance(door, Door))
# >>> True

class EnhancedDoor(Door):
    pass

enhanced_door = EnhancedDoor()
print(isinstance(enhanced_door, EnhancedDoor))
# >>> True
print(isinstance(enhanced_door, Door))
# >>> True
print(issubclass(EnhancedDoor, Door))
# >>> True
``` 

If you create a class that does not inherit from `list`, then `isinstance` will not work to see if it is a list

```python```
class MyList:
    pass

my_list = MyList()
print(isinstance(my_list, list))
# >>> False

### What is the best way to test that an object exposes a given interface?

* Give the object an attribute that has the list of interfaces it promises to implement. Any time we want to test the behavior of an object, just check the contents of that attribute.
* So inject the "behavior promise" into classes and instances
* Remember metaclasses are the classes that build Classes, so they should be used to change the structure of a class, and therefore, its instances

`ABCMeta` metaclass gives two meta classes

```python
def __instancecheck__(cls, inst):
   [...]

def __subclasscheck__(cls, sub):
   [...]
```

##  more about ABC

* A class that contains one or more abstract methods is an Abstract Class.
* A method that is declared but contains no implementation is an Abstract Method.
* Abstract classes may not be instantiated.
* Abstract classes require require subclasses to provide implementations for the abstract methods.
* Subclasses (of an abstract class) are not required to implement abstract methods of the parent class.


* Abstract base classes are a form of interface checking more strict than individual hasattr() checks for particular methods.
* By defining an abstract base class, you can define a common API for a set of subclasses.
* This capability is especially useful in situations where a third-party is going to provide implementations, such as with plugins to an application,
* But it can also aid you when working on a large team or with a large code-base where keeping all classes in your head at the same time is difficult or not possible.

