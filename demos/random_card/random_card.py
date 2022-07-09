"""Draw cards randomly from a self-replacing pile until you have a deck."""

import random
import collections
import matplotlib.pyplot as plt
import math
from statistics import median, mean

DECK_SIZE = 52
ITERATIONS = 10000


class CardSimulator:
    """Create RandomCard class."""

    def __init__(self, iterations=ITERATIONS, deck_size=DECK_SIZE):
        """Initialize stuff."""
        self.deck_size = deck_size
        self.__trials = []
        self.iterations = int(iterations)

    def sort_trials(self):
        """Sort the trials."""
        self.__trials = sorted(self.__trials)

    def set_trials(self):
        """Run the simulation."""
        turns = 0
        deck = []
        for k in range(self.iterations):
            while len(deck) < self.deck_size:
                # treat every card in deck as a number.
                pick_a_card = random.randint(1, self.deck_size)
                if pick_a_card not in deck:
                    deck.append(pick_a_card)
                turns += 1

            self.__trials.append(turns)
            turns = 0
            deck = []
            k += 1

    @property
    def trials_count(self):
        """Get number of trials."""
        return len(self.__trials)

    @property
    def counter(self):
        """Use collections."""
        counter = collections.Counter(self.__trials)
        return counter

    @property
    def average(self):
        """Return the average result."""
        return mean(self.__trials)

    @property
    def median(self):
        """Return the median result."""
        return median(self.__trials)

    @property
    def minimum(self):
        """Return the lowest result."""
        return min(self.__trials)

    @property
    def maximum(self):
        """Return the highest result."""
        return max(self.__trials)

    @property
    def most_common_frequency(self):
        """Get the frequency of most commonly occuring result."""
        counter = self.counter
        common = list(counter.most_common(1))
        most_common = list(dict(common).values())[0]

        return most_common

    @property
    def most_common_result(self):
        """Get the most commonly occuring result."""
        counter = self.counter
        common = list(counter.most_common(1))
        most_common = list(dict(common).keys())[0]

        return most_common

    def print_stats(self):
        """Display some useful stats."""
        print('\n')
        print('Results for %s trial(s):' % (self.trials_count))
        print('Average: %s' % (self.average))
        print('Median: %s' % (self.median))
        print('Shortest simulation: %s draws' % (self.minimum))
        print('Longest simulation: %s draws' % (self.maximum))
        print('Most common result (mode): %s' % (self.most_common_result))
        print('Frequency of most common result: %s tries' % (
            self.most_common_frequency))
        print('\n')

    def render_graph(self):
        """Display a graph of the trials."""
        self.sort_trials()
        counter = self.counter

        values = list(counter.values())
        keys = list(counter.keys())

        y_max = math.ceil((1.05 * self.most_common_frequency) / 10) * 10
        x_max = math.ceil((1.05 * self.maximum) / 10) * 10

        plt.plot(keys, values, 'ro')
        plt.axis([0, x_max, 0, y_max])
        plt.show()
