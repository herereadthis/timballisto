"""Show use cases for decorators."""


def call_counter(func):
    """Check number of times a function is called."""
    # This decorator will add a "calls" attribute to the function which counts
    # the number of times it was called.
    def helper(*args, **kwargs):
        """Use the *args, **kwargs notation to cope with functions..."""
        """that have arbritary positional and keyword parameters."""
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0

    return helper


@call_counter
def succ(x):
    """Simple function."""
    return x + 1


@call_counter
def mul1(x, y=1):
    """Another function using decorator, with multiple params."""
    return x * y + 1

print(succ.calls)
for i in range(10):
    succ(i)

print(succ.calls)
# >>> 0
# >>> 10

mul1(3, 4)
mul1(4)
mul1(y=3, x=2)
print(mul1.calls)
# >>> 3


def greeting(expr):
    """Demo a decorator that accepts a parameter."""
    def greeting_decorator(func):
        def function_wrapper(x):
            print(expr + ", " + func.__name__ + " returns:")
            return func(x)
        return function_wrapper
    return greeting_decorator


@greeting('Jo napot')
def foo(x):
    """Foo."""
    print(x + 4)
    return x + 4

bar = foo(42)
print(bar)
