"""Graph the mandelbrot set."""

from numpy import linspace, reshape
from matplotlib import pyplot

# x range
xmin = -2.0
xmax = 0.5
# y range
ymin = -1.25
ymax = 1.25
# resoluteion
nx = 1000
ny = 1000
# max iterations
maxiter = 50


def mandelbrot(z):
    """Compute for each pixel."""
    c = z
    for n in range(maxiter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return maxiter


# lists of x and y
X = linspace(xmin, xmax, nx)
# pixel co-ordinates
Y = linspace(ymin, ymax, ny)


def reshape_array(values_array):
    """Change to rectangular array."""
    return reshape(values_array, (nx, ny))


def simple_loop():
    """Do the simplest version of mandelbrot."""
    loop_list = []
    for y in Y:
        for x in X:
            z = complex(x, y)
            # This version calls the mandelbrot function many many times.
            loop_list += [mandelbrot(z)]
    loop_list = reshape_array(loop_list)
    return loop_list


def map_loop():
    """Build a list of arguments in advance of mapping."""
    pre_map = [complex(x, y) for y in Y for x in X]
    loop_list = map(mandelbrot, pre_map)
    loop_list = reshape_array(loop_list)
    return loop_list


if __name__ == '__main__':

    # Simple loop version
    # N = simple_loop()

    # Map version
    N = map_loop()

    # plot the image
    pyplot.imshow(N)
    pyplot.show()
