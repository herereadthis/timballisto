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


## Example



```python
# This is how you're not supposed to do it. The coupling is too tight.
class Parent():

    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.kids = []

    def havechild(self,firstname):
        print self.firstname,"is having a child"
        self.kids.append(Child(self,firstname))

class Child(Parent):

    def __init__(self,parent,firstname):
        self.parent = parent
        self.firstname = firstname
        self.lastname = parent.lastname
```

```python
# Do better: remove code repetition
class Person(object):

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_name(self):
        return '%s %s' % (self.firstname, self.lastname)


class Parent(Person):

    def __init__(self, firstname, lastname):
        super(Parent, self).__init__(firstname, lastname)
        self.kids = []

    def havechild(self, firstname):
        print self.firstname, "is having a child"
        self.kids.append(Child(self, firstname))


class Child(Person):

    def __init__(self, parent, firstname):
        super(Parent, self).__init__(firstname, parent.lastname)
        self.parent = parent
```

```python
# How to use composition
from collections import defaultdict

class Person(object):

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_name(self):
        return '%s %s' % (self.firstname, self.lastname)


class FamilyRegistry(object):

    def __init__(self):
        self.kids = defaultdict(list)

    def register_birth(self, parent, child_name):
        print parent.firstname, "is having a child"
        child = Person(child_name, parent.lastname)
        self.kids[parent.lastname].append(child)
        return child

    def print_children(self, person):
        children = self.kids[person.lastname]
        if len(children) == 0:
            print '%s has no children' % person.get_name()
            return
        for child in children:
            print child.get_name()

joe = Person('Joe', 'Black')
jill = Person('Jill', 'White')
registry = FamilyRegistry()
registry.register_birth(joe, 'Joe Junior')
registry.register_birth(joe, 'Tina') 
registry.print_children(joe)
```