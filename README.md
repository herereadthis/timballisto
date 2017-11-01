# Timballisto

[![Build Status](https://travis-ci.org/herereadthis/timballisto.svg?branch=master)](https://travis-ci.org/herereadthis/timballisto)

Random Python stuff


### Built-In Functions

`id()` returns memory position of an object

```python
x = 1
print(id(x))
y = 1
print(id(y))

# these two are the same: x and y are both instances of int class,
# and there is one address for the int class
print(id(x.__class__))
print(id(y.__class__))
```

