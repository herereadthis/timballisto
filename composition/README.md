# Composition


Object B is a specialization of object A when:

* B has all the features of A
* B has some other features too
* B can do some or all the things A can do, but differently


Delegation is an object that does only what it knows best, and leave everything else to other objects. There are two ways to do delegation: 

* composition (explicit delegation)
* inheritance (implicit delegation)

Composition is when an object knows about another object, and explicitly delegates some tasks to it.

Delegation is implicit in inheritance.


* Coupling - changing one thing affects the other. Avoid doing this