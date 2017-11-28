"""Demo abstract base classes from https://pymotw.com/2/abc/."""

from abc import abstractmethod, ABCMeta


class PluginBase(metaclass=ABCMeta):
    """Demo an abstract class."""

    @abstractmethod
    def load(self, input):
        """Retrieve data from the input source and return an object."""
        return

    @abstractmethod
    def save(self, output, data):
        """Save the data object to the output."""
        return


class RegisteredWay(object):
    """This subclass implements and abstract through registration."""

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)

PluginBase.register(RegisteredWay)


class SubclassWay(PluginBase):
    """This subclass implements and abstract through inheritance."""

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)


if __name__ == '__main__':
    print('Subclass: {}'.format(issubclass(RegisteredWay, PluginBase)))
    # >>> True
    print('Instance: {}'.format(isinstance(RegisteredWay(), PluginBase)))
    # >>> True
    print('Subclass: {}'.format(issubclass(SubclassWay, PluginBase)))
    # >>> True
    print('Instance: {}'.format(isinstance(SubclassWay(), PluginBase)))
    # >>> True
