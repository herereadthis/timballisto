"""Demo creation of decorator."""


def my_decorator(some_function):
    """Fake a decorator."""
    def wrapper():
        """Wrap."""
        print("This happens BEFORE some_function() is called.")
        some_function()
        print("This happens AFTER some_function() is called.")

    return wrapper


def just_some_function():
    """Demo."""
    print("Wheee!")

just_some_function = my_decorator(just_some_function)
just_some_function()
