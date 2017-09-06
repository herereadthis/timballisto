"""Draw cards randomly from a self-replacing pile until you have a deck."""

import random
import collections
import matplotlib.pyplot as plt
import math

cards = 52
deck = []
turns = 0
trials = []
iterations = input('How many simulations [10]?') or 10
iterations = int(iterations)


def get_counter(trials_list):
    """Use collections."""
    counter = collections.Counter(trials_list)
    return counter


def get_average(num_list):
    """Get average of a list."""
    return sum(num_list) / len(num_list)


def get_most_common_frequency(trials_list):
    """Get the frequency of most commonly occuring result."""
    counter = get_counter(trials_list)
    common = list(counter.most_common(1))
    most_common = list(dict(common).values())[0]

    return most_common


def get_most_common_result(trials_list):
    """Get the most commonly occuring result."""
    counter = get_counter(trials_list)
    common = list(counter.most_common(1))
    most_common = list(dict(common).keys())[0]

    return most_common


for k in range(iterations):
    while len(deck) < cards:
        a = random.randint(1, cards)
        if a not in deck:
            deck.append(a)
        turns += 1

    trials.append(turns)
    turns = 0
    deck = []
    k += 1

most_common_frequency = get_most_common_frequency(trials)
most_common_result = get_most_common_result(trials)

print('Trials: %s' % (trials))
print('Sorted: %s' % (sorted(trials)))
print('Average: %s' % (get_average(trials)))
print('Most common result: %s' % (most_common_result))
print('Most common frequency: %s' % (most_common_frequency))

sorted_trials = sorted(trials)

counter = collections.Counter(sorted_trials)

values = list(counter.values())
keys = list(counter.keys())

y_max = math.ceil(most_common_frequency / 5) * 5
x_max = max(trials)

plt.plot(keys, values, 'ro')
plt.axis([0, x_max, 0, y_max])
plt.show()
