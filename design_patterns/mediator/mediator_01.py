"""Demo mediator pattern."""

from abc import ABCMeta, abstractmethod


class UserABC(metaclass=ABCMeta):
    """Abstract class for User class - define interface."""

    def __init__(self, med, name):
        """Initialize by specifying mediator class and user name."""
        self.mediator = med
        self.name = name

    @abstractmethod
    def send(self, msg):
        """Abstract send."""
        pass

    @abstractmethod
    def receive(self, msg):
        """Abstract receive."""
        pass


class ChatMediatorImpl:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, msg, user):
        for u in self.users:
            if u != user:
                u.receive(msg)


class CasualUser(UserABC):
    """Creates a user which speaks casually."""

    def send(self, msg):
        print('{0} wants to say, \"{1}\"'.format(self.name, msg))
        self.mediator.send_message(msg, self)

    def receive(self, msg):
        print('{0} heard someone say, \"{1}\"'.format(self.name, msg))


class FormalUser(UserABC):
    """Creates a user which speaks formally."""

    def __init__(self, med, first_name, last_name):
        """Initilize formal user, from user abstract class."""
        full_name = '{0} {1}'.format(first_name, last_name)
        super().__init__(med, full_name)

    def send(self, msg):
        """Abstract method send."""
        print('{0} is sending a message: \"{1}\"'.format(self.name, msg))
        self.mediator.send_message(msg, self)

    def receive(self, msg):
        print('{0} has recieved a message: \"{1}\"'.format(self.name, msg))


if __name__ == '__main__':
    mediator = ChatMediatorImpl()
    user1 = CasualUser(mediator, "Liz")
    user2 = CasualUser(mediator, "Rick")
    user3 = CasualUser(mediator, "Jim")
    user4 = CasualUser(mediator, "Annie")
    user5 = FormalUser(mediator, 'Sebastian', 'Pendleton')
    mediator.add_user(user1)
    mediator.add_user(user2)
    mediator.add_user(user3)
    mediator.add_user(user4)
    mediator.add_user(user5)

    user1.send("Hi All")