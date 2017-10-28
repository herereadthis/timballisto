# Polymorphism

* An object might have different implementations of its methods depending on the input parameters
* Methods understand the class hierarchy of a type.
* Python will ask the input objects to determine how they perform the operation (e.g., adding `int 5` to `float 5.555555`)
* Code written for any type must work for its derived type. If a list object is written to contain numbers, then the list must also be able to contain integers, because integers are numbers.
* Since subtypes provide the methods of the parent type, Python has subtype polymorphism

In Python, type is not explicity declared. Everything has a type, it's just that type is implicitly assigned. 

Variables are just pointers, they tell where in memory a variable has been stored.

* Python is *stongly typed* because everything has a well-defined type. Check with `type\()` function.
* Python is *dynamic* since the type of a variable is not explicitly declared. It changes with the content.

## EAFP

"easier to ask for forgiveness than permission"

Instead of checking if an object has a certain attribute or method before using it, just assume it works, and manage errors

```python
try:
    someobj.open()
    [...]
except AttributeError:
    [...]
```

## What about "program against an interface, not an implementation"?

* It doesn't really translate to Python because it doesn't have an interface feature.
* In python you use "duck typing"
* If you want to see if an object is a duck, then try using the `quack()` method and provide appropriate error handling
* Check for type only when necessary
* The equivalent in Python is you are not supposed to make your code too reliant on an object's type, but see whether it has the interface you need
  * "interface" is the bunch of attributes and methods of an object that provide a certain behavior
* The advantage of emphasizing interfaces over specific types, code is more flexible by allowing polymorphic substitution

```python
hasattr()
```

