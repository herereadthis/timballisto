"""Demo memoisation - ways to store computed values, saving calculatios."""

import timeit



class Memoize:
    """Class as decorator."""

    def __init__(self, fn):
        """Initialize."""
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        """Call."""
        if args not in self.memo:
            self.memo[args] = self.fn(*args)

        return self.memo[args]


@Memoize
def fibonacci(n):
    """Do recursive fibonacci."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def undecorated_fibonacci(n):
    """Do recursive fibonacci."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":

    start = timeit.default_timer()
    for i in range(0, 10000):
        undecorated_fibonacci(100)
    stop = timeit.default_timer()
    print(stop - start)

    start2 = timeit.default_timer()
    for i in range(0, 10000):
        fibonacci(100)
    stop2 = timeit.default_timer()
    print(stop2 - start2)
