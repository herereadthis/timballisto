"""Demo abstract base classes."""

from abc import ABC, abstractmethod

"""
An abstract class serves as a skeleton for a subclass.
"""


class AbstractOperation(ABC):
    """Demo abstract base classes."""

    def __init__(self, operand_a, operand_b):
        """Initialize."""
        self.operand_a = operand_a
        self.operand_b = operand_b
        super(AbstractOperation, self).__init__()

    @abstractmethod
    # By using the @abstractmethod decorator - enforce implementation of this
    # "execute" method for ubclasses that inherit the AbstractOperation class.
    # Force the implementation of parent methods in derived classes:
    # separate interface from implementation.
    def execute(self):
        """Execute."""
        pass


# If you run this, you will get a super! error!
# a = AbstractOperation(1, 2)

"""
Traceback (most recent call last):
  File "abstract/abstract_03.py", line 21, in <module>
    a = AbstractOperation(1, 2)
TypeError: Can't instantiate abstract class AbstractOperation with abstract
methods execute
"""


class ConcreteOperation(AbstractOperation):
    pass


# Same deal here
# c = ConcreteOperation(1, 2)
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't instantiate abstract class ConcreteOperation with abstract 
methods execute
"""

"""
So before the ConcreteOperation class is instantiated, the ConcreteOperation
metaclass verifies all @abstractmethod decorated methods have been implemented.

An object class defines how an instance of a class behaves.
A metaclass defines how a class behaves.
"""


class AddOperation(AbstractOperation):
    def execute(self):
        return self.operand_a + self.operand_b


class SubtractOperation(AbstractOperation):
    def execute(self):
        return self.operand_a - self.operand_b
