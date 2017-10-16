"""Demo polymorphism."""

# b is an integer
b = 17
# c is a float
c = 6.77778

print(b + c)
print(b.__add__(c))


def echo(a):
    """Do something simple."""
    # Python functions can accept any variable without checking the type and
    # rely on the variable itself to provide the correct methods
    return a

# polymorphism: echo() can handle different types
print(echo(5))
# >>> 5
print(echo('five'))
# >>> five

# len() function is polymorphic
my_list = [1, 2, 3]
print(len(my_list))
print(my_list.__len__())
# >>> 3
my_string = 'hello world'
print(len(my_string))
# >>> 11
