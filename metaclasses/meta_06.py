"""Explore purpose of metaclasses."""

"""
Suppose we have 3 classes, all of which need a particular method if a
condition is met. One possible way is to use decorators.
"""

x = input("Do you need the answer? (y/n): ")
if x == "y":
    required = True
else:
    required = False

@property
def the_answer(self, *args):
    return 42


def augment_answer(cls):
    if required:
        cls.the_answer = the_answer
    # we have to return the class now:
    return cls


@augment_answer
class Philosopher1:
    pass


@augment_answer
class Philosopher2:
    pass


@augment_answer
class Philosopher3:
    pass

plato = Philosopher1()
kant = Philosopher2()

if required:
    print(plato.the_answer)
    print(kant.the_answer)
else:
    print('not required')
