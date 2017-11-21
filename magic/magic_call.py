"""Demo __call__."""

"""
__call__ gets called whenever an instance is called.
With decorators, we see that functions can be callable objects.
Classes can also be callable objects.
"""


class SimpleCall:
    """Demo __call__."""

    def __init__(self):
        """Initialize."""
        print('An instance of SimpleCall was initialized.')

    def __call__(self, *args, **kwargs):
        """Call."""
        print('SimpleCall has args: {0} {1}'.format(args, kwargs))


class Fibonacci:
    """Demo __call__to do fibonacci."""

    def __init__(self):
        """Initialize."""
        # Cache is going to build key-values where key is position in sequence,
        # value is value at that position.
        self.cache = {}

    def __call__(self, n):
        """Call."""
        # What will happen is when you do instance(count) then this class will
        # return the fibonacci number at that position
        if n not in self.cache:
            if n == 0:
                self.cache[0] = 0
            elif n == 1:
                self.cache[1] = 1
            else:
                # nth number in sequence is equal to n-1 + n-2 number
                self.cache[n] = self.__call__(n - 1) + self.__call__(n - 2)
        return self.cache[n]


if __name__ == "__main__":
    print('\nDemo basic class with __call__')
    x = SimpleCall()
    # >>> An instance of SimpleCall was initialized.
    x(5)
    # >>> SimpleCall has args: (5,) {}
    x(foo='bar')
    # >>> SimpleCall has args: () {'foo': 'bar'}

    print('\nDemo fibonacci class with __call__')
    fib = Fibonacci()

    doremi = Fibonacci()

    fib_range = 4
    for i in range(fib_range):
        if i == fib_range - 1:
            print(fib(i))
        else:
            print(fib(i), end=', ')

    print(fib.cache)
    print(doremi(fib_range - 1))
