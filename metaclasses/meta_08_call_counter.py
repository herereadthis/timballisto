"""Use metaclass to create a call counter."""


class FunctionCallCounter(type):
    """decorates all the methods of the  subclass using call_counter."""

    @staticmethod
    def call_counter(func):
        """Decorator for counting the number of function  or method calls."""
        def helper(*args, **kwargs):
            helper.calls += 1
            return func(*args, **kwargs)
        helper.calls = 0
        helper.__name__ = func.__name__

        return helper

    def __new__(cls, clsname, superclasses, attributedict):
        """Decorate every method with the decorator call_counter."""
        print('__new__ class: {}'.format(clsname))
        for attr in attributedict:
            if not callable(attr) and not attr.startswith("__"):
                """
                Every attribute in the attribute dictionary gets decorated.
                Remember:

                @my_decorator
                my_function()

                is the same as my_decorator(my_function)
                """
                attributedict[attr] = cls.call_counter(attributedict[attr])

        return type.__new__(cls, clsname, superclasses, attributedict)


class MyClass(metaclass=FunctionCallCounter):
    """Show an actual usefulness of metaclasses: decorate every method."""

    def foo(self):
        """Foo."""
        pass

    def bar(self):
        """Bar."""
        pass

if __name__ == "__main__":
    x = MyClass()
    # >>> __new__ class: MyClass
    print('x.foo.calls: {0},  x.bar.calls: {1}'
          .format(x.foo.calls, x.bar.calls))
    # >>> x.foo.calls: 0,  x.bar.calls: 0
    x.foo()
    print('x.foo.calls: {0},  x.bar.calls: {1}'
          .format(x.foo.calls, x.bar.calls))
    # >>> x.foo.calls: 1,  x.bar.calls: 0
