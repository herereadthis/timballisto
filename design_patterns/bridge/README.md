# Bridge Pattern

**Decouple an abstraction from its implementation so that the two can vary independently.**

Create an interface which acts as a bridge which makes the functionality of concrete classes independent from interface implementer classes.    

Before:

* Shape Class
  * Rectangle Subclass
    * Red Rectangle
    * Blue Rectangle
  * Circle Subclass
    * Red Circle
    * Blue Circle

After

* Bridge
  * Shape Class
    * Rectangle
    * Circle
  * Color Class
    * Red
    * Blue

* **Abstraction** - define the interface
* **AbstractionImpl** - implement the abstraction using a reference to an implementor-type object
* **Implementor** - define interface for the implementation classes
* **ConcreteImpl** - implements the implementor interface

## Summary

* Create two different hierarchies, abstraction and implementation
* Remove the dependency between abstraction and implementation
* Create a bridge that coordinates between abstractiona and

