"""Demo __str__."""


class ClassA():

    def __init__(self, foo='hello world'):
        self.foo = foo


class ClassB():

    def __init__(self, foo='hello world'):
        self.foo = foo

    def __str__(self):
        return 'hi there'


class Robot:

    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    def __repr__(self):
        return 'Robot(\'%s\', %s)' % (self.name, str(self.build_year))


if __name__ == '__main__':

    print('\nDemo Basic Class')
    a_instance = ClassA('foo')

    print(a_instance)
    # >>> <__main__.ClassA object at 0x109b1c6a0>

    print(a_instance.__dict__)
    # >>> {'foo': 'foo'}

    print(str(a_instance))
    # >>> <__main__.ClassA object at 0x10feee550>

    print(repr(a_instance))
    # >>> <__main__.ClassA object at 0x10e1186d8>

    print('\nDemo Class with magic methods')
    b_instance = ClassB('foo')
    print(b_instance)
    # >>> hi there
    print(b_instance.__dict__)
    # >>> {'foo': 'foo'}
    print(str(b_instance))
    # >>> hi there
    print(repr(b_instance))
    # >>> <__main__.ClassB object at 0x10344d160>

    print('\nDemo Robot Class')
    a_robot = Robot('Bender', 2979)
    print(str(a_robot))
    print(repr(a_robot))
