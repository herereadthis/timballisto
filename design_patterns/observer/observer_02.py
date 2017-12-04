"""Demo the observer pattern, but make it more flexible."""

# Allow observers to register with a subject even if it doesn't have the same
# update class


class ObserverOne:
    """The observer class."""

    def __init__(self, name):
        """Initialize with the name."""
        self.name = name

    def update(self, message):
        """Want to be notified when listening for changes."""
        print('{} got message "{}"'.format(self.name, message))


class ObserverTwo:
    """The observer class."""

    def __init__(self, name):
        """Initialize with the name."""
        self.name = name

    def receive(self, message):
        """Want to be notified when listening for changes."""
        print('{} - message sent to "{}"'.format(message, self.name))


class Subject:
    """The subject class aka observerable."""

    def __init__(self):
        """A set is an unordered collection with no duplicate examples."""
        self.observers = dict()

    def register(self, observer, callback=None):
        """Allow observers to register with the subject, with a callback."""
        if callback is None:
            # Fallback to the original if not subscribe
            callback = getattr(observer, 'update')
        self.observers[observer] = callback

    def unregister(self, observer):
        """Allow observers to unregister with the subject."""
        del self.observers[observer]

    def dispatch(self, message):
        """Every observer has its update method invoked."""
        # python3 items() turns dictionary into an iterable e.g, for key, value
        for observer, callback in self.observers.items():
            callback(message)


if __name__ == '__main__':
    subject = Subject()

    bob = ObserverOne('Bob')
    alice = ObserverOne('Alice')
    john = ObserverTwo('John')

    subject.register(bob)
    subject.register(alice, alice.update)
    subject.register(john, john.receive)

    print(subject.observers)

    subject.dispatch('hello world, this is my first message')
    # >>> Bob got message "hello world, this is my first message"
    # >>> Alice got message "hello world, this is my first message"
    # >>> hello world, this is my first message - message sent to "John"
    subject.unregister(bob)
    subject.dispatch('yo wassup here is speech number 2')
    # >>> Alice got message "yo wassup here is speech number 2"
    # >>> yo wassup here is speech number 2 - message sent to "John"
