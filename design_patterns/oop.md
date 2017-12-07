# OOP

## Summary

* Think of oop as looking at a program lots of little self-contained programs, each with their own name, data, and logic, and these little programs interact with each other to form a whole application.
* Objects are things that have attributes and behaviors bundled together.
* Classes are the templates to create objects. Objects created from a class will behave similarly but have their own characteristics

## Abstraction

* Describe the general concept of an object without defining its specific details.

* Suppose if we wanted to create an class for motorcycles. There are many different motorcycles, but they generally have two wheels, an engine, handlebars, and go fast, slow down, and turn. These attributes and behaviors can become a `Motorcycle` class.

### Attributes

* Attributes are the properties that represent the current state of the object.
* For example, a `Person` class will have `name`, `age`, `hair_color` information aka data aka attributes

### Behaviors

* Behaviors define the things an object can do
* a `Person` can `walk()` and `speak()` and `eat()`
* In OOP, behaviors are **methods**
* Methods may alter the state of an object (setter) or provide ways of accessing it (getter)

### Class

* A class is the blueprint or template or plan for creating new objects.
* After declaring a class, you can create (**instantiate**) an object by declaring a new identifier against the class.
* A class has an identity (its name), data (attributes), and logic (methods)

### Object

* an object is an instance of a class
* We can create a `johnSmith` object, which is an instance of the `Person` class

## Encapsulation

* The idea of bundling data with logic - combining attributes and methods into a single named entity
* Apply different levels of visiblity to allow objects to interact with it at only an appropriate level
* Only publicly-declared methods (aka **"interface"**) should be utilized and seen by other objects
* For example a `johnSmith` instance of a `Person` class needs to access the `walk()` and `speak()` methods, but does need to use or know about `digest()` or `set_heart_rate()`
* An object should not care about how the methods are **implemented**. It should only care about providing the required information (**parameters**) or message to the method (e.g. `speak('hello world')`) so that it can receive an expected result or action. In other words, don't be too concerned about how speaking actually works.
* **Data hiding** - Access to an object's attributes should be controlled by the object itself, and other objects shouldn't be able to directly change that object's attributes
* As long as the interface stays the same, the internal methods can changed to do whatever

### Visibility

## Inheritance

## Polymorphism