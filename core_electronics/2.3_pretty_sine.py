import math
import time

# number of cycles to run animation
number_cycle = 5
# pi
pi = math.pi

# return the sine of x
def sin(x):
    return math.sin(x)

x = 0

while x < (number_cycle * 2 * pi):
    # somewhere between -20 to 20
    bar = int(20 * sin(x))
    x += 0.3
    print((21 + bar) * '=')
    time.sleep(0.03)
