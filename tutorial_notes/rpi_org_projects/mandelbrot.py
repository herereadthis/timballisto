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


if __name__ == '__main__':
    # lists of x and y
    X = linspace(xmin, xmax, nx)
    # pixel co-ordinates
    Y = linspace(ymin, ymax, ny)

    # N = []
    # for y in Y:
    #     for x in X:
    #         z = complex(x, y)
    #         N += [mandelbrot(z)]
    Z = [complex(x, y) for y in Y for x in X]
    N = map(mandelbrot, Z)

    # change to rectangular array
    N = reshape(N, (nx, ny))

    # plot the image
    pyplot.imshow(N)
    pyplot.show()
