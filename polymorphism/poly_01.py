"""Demo polymorphism."""

# a is implicitly a number
a = 5
print(a)
# >>> 5

# not asking the type of a, but the type of the content of a
print(type(a))
# >>> <class 'int'>
print(id(a))
# >>> 4446665408

# a is is now implicitly a string
a = 'five'
print(a)
# >>> five
print(type(a))
# >>> <class 'string'>

# same place in memory
print(id(a))
# >>> 4446665408
