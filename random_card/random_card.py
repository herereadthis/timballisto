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
        self.trials = []
        self.iterations = int(iterations)

    def set_iterations(self, iterations=ITERATIONS):
        """Set the number of iterations to run simulation."""
        self.iterations = int(iterations)

    def set_deck_size(self, deck_size=DECK_SIZE):
        """Set the size of the card deck."""
        self.deck_size = int(deck_size)

    def sort_trials(self):
        """Sort the trials."""
        self.trials = sorted(self.trials)

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

            self.trials.append(turns)
            turns = 0
            deck = []
            k += 1

    def get_counter(self):
        """Use collections."""
        counter = collections.Counter(self.trials)
        return counter

    def get_average(self):
        """Return the average result."""
        return mean(self.trials)

    def get_median(self):
        """Return the median result."""
        return median(self.trials)

    def get_min(self):
        """Return the lowest result."""
        return min(self.trials)

    def get_max(self):
        """Return the highest result."""
        return max(self.trials)

    def get_most_common_frequency(self):
        """Get the frequency of most commonly occuring result."""
        counter = self.get_counter()
        common = list(counter.most_common(1))
        most_common = list(dict(common).values())[0]

        return most_common

    def get_most_common_result(self):
        """Get the most commonly occuring result."""
        counter = self.get_counter()
        common = list(counter.most_common(1))
        most_common = list(dict(common).keys())[0]

        return most_common

    def print_stats(self):
        """Display some useful stats."""
        num_trials = len(self.trials)
        average = self.get_average()
        median = self.get_median()
        mode = self.get_most_common_result()
        mode_frequency = self.get_most_common_frequency()

        print('\n')
        print('Results for %s trial(s):' % (num_trials))
        print('Average: %s' % (average))
        print('Median: %s' % (median))
        print('Shortest simulation: %s draws' % (self.get_min()))
        print('Longest simulation: %s draws' % (self.get_max()))
        print('Most common result (mode): %s' % (mode))
        print('Frequency of most common result: %s' % (mode_frequency))
        print('\n')

    def render_graph(self):
        """Display a graph of the trials."""
        self.sort_trials()
        counter = self.get_counter()

        values = list(counter.values())
        keys = list(counter.keys())

        y_max = math.ceil((1.05 * self.get_most_common_frequency()) / 10) * 10
        x_max = math.ceil((1.05 * self.get_max()) / 10) * 10

        plt.plot(keys, values, 'ro')
        plt.axis([0, x_max, 0, y_max])
        plt.show()
