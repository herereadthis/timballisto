# Mediator Design Pattern

Suppose you have a something that has many-to-many relationships. Imagine a system that has many groups, and many users. A user may belong to many groups, and a group may have many users.

One way to design this is to have user objects coupled to group objects.

Another way is to take this mapping of users to groups and turn it into an abstraction. Decoupling is helpful because it will be easier to maintain. You can control the relationships as a whole or part. The mediator acts as the hub.

If you use a mediator, the user objects no longer have to know how the group objects work.

* *Mediator* defines an interface for communicating with *Colleague* objects.
* *ConcreteMediator* knows the *Colleague* classes and *Colleague* objects. It implements the communication between *Colleague* classes.
* *Colleague* classes keep a reference to its *Mediator* object. Instead of communicating with other *Colleague* classes, it communicates with the *Mediator*.

