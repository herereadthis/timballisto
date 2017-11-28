"""Use abc as a skeleton for subclasses."""
"""https://www.smartfile.com/blog/abstract-classes-in-python/"""

from abc import ABC, abstractmethod


class AbstractOperation(ABC):

    def __init__(self, operand_a, operand_b):
        """Initialize by storing 2 args."""
        self.operand_a = operand_a
        self.operand_b = operand_b
        super(AbstractOperation, self).__init__()

    @abstractmethod
    def execute(self):
        """Abstract method to enforce implementation of execute."""
        pass


class AddOperation(AbstractOperation):
    """Subclass to implement addition."""

    def execute(self):
        return self.operand_a + self.operand_b


class SubtractOperation(AbstractOperation):
    """Subclass to implement subtraction."""

    def execute(self):
        return self.operand_a - self.operand_b


class MultiplyOperation(AbstractOperation):
    """Subclass to implement multiplication."""

    def execute(self):
        return self.operand_a * self.operand_b


class DivideOperation(AbstractOperation):
    """Subclass to implement division."""

    def execute(self):
        return self.operand_a / self.operand_b

if __name__ == '__main__':
    a = AddOperation(6, 2)
    print(a.execute())
    # >>> 7
    a = SubtractOperation(6, 2)
    print(a.execute())
    # >>> 4
    a = MultiplyOperation(6, 2)
    print(a.execute())
    # >>> 12
    a = DivideOperation(6, 2)
    print(a.execute())
    # >>> 3
