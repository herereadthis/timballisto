"""Demo the observer pattern, simplest version."""


class Observer:
    """The observer class."""

    def __init__(self, name):
        """Initialize with the name."""
        self.name = name

    def update(self, message):
        """Want to be notified when listening for changes."""
        print('{} got message "{}"'.format(self.name, message))


class Subject:
    """The subject class aka observerable."""

    def __init__(self):
        """A set is an unordered collection with no duplicate examples."""
        self.observers = set()

    def register(self, observer):
        """Allow observers to register with the subject."""
        self.observers.add(observer)

    def unregister(self, observer):
        """Allow observers to unregister with the subject."""
        self.observers.discard(observer)

    def dispatch(self, message):
        """Every observer has its update method invoked."""
        for observer in self.observers:
            observer.update(message)


if __name__ == '__main__':
    subject = Subject()

    bob = Observer('Bob')
    alice = Observer('Alice')
    john = Observer('John')

    subject.register(bob)
    subject.register(alice)
    subject.register(john)

    subject.dispatch('hello world, this is my first message')
    # >>> John got message "hello world, this is my first message"
    # >>> Bob got message "hello world, this is my first message"
    # >>> Alice got message "hello world, this is my first message"
    subject.unregister(bob)
    subject.dispatch('yo wassup here is speech number 2')
    # >>> John got message "yo wassup here is speech number 2"
    # >>> Alice got message "yo wassup here is speech number 2"
