"""Draw cards randomly from a self-replacing pile until you have a deck."""

import random
import collections
import matplotlib.pyplot as plt
import math

DECK_SIZE = 52

class RandomCard:
    """Create RandomCard class."""

    def __init__(self, iterations=10, show_graph=True, deck_size=DECK_SIZE):
        """Initialize stuff."""
        self.deck_size = deck_size
        self.trials = []
        self.iterations = int(iterations)
        self.show_graph = show_graph

    def set_iterations(self, iterations=10):
        """Set the number of iterations to run simulation."""
        self.iterations = int(iterations)

    def set_deck_size(self, deck_size=DECK_SIZE):
        """Set the size of the card deck."""
        self.deck_size = int(deck_size)

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

    def get_trials(self, sort_trials=True):
        """Print the trials."""
        if (sort_trials is True):
            print(sorted(self.trials))
        else:
            print(self.trials)

    def get_average(self):
        """Return the average result."""


if __name__ == '__main__':
    iterations = input('How many simulations [10]?') or 10
    show_graph_input = input('Want to see a graph y/n [y]?') or 'y'
    show_graph = True
    if (show_graph_input == 'n' or show_graph_input == 'N'):
        show_graph = False

    card_simulation = RandomCard()
    card_simulation.set_iterations(iterations)
    card_simulation.set_trials()
    card_simulation.get_trials()
    card_simulation.get_average()

    print(card_simulation.iterations)
    print(card_simulation.show_graph)


# cards = 52
# deck = []
# turns = 0
# trials = []
# iterations = input('How many simulations [10]?') or 10
# iterations = int(iterations)


# def get_counter(trials_list):
#     """Use collections."""
#     counter = collections.Counter(trials_list)
#     return counter


# def get_average(num_list):
#     """Get average of a list."""
#     return sum(num_list) / len(num_list)


# def get_most_common_frequency(trials_list):
#     """Get the frequency of most commonly occuring result."""
#     counter = get_counter(trials_list)
#     common = list(counter.most_common(1))
#     most_common = list(dict(common).values())[0]

#     return most_common


# def get_most_common_result(trials_list):
#     """Get the most commonly occuring result."""
#     counter = get_counter(trials_list)
#     common = list(counter.most_common(1))
#     most_common = list(dict(common).keys())[0]

#     return most_common


# for k in range(iterations):
#     while len(deck) < cards:
#         a = random.randint(1, cards)
#         if a not in deck:
#             deck.append(a)
#         turns += 1

#     trials.append(turns)
#     turns = 0
#     deck = []
#     k += 1

# most_common_frequency = get_most_common_frequency(trials)
# most_common_result = get_most_common_result(trials)

# print('Trials: %s' % (trials))
# print('Sorted: %s' % (sorted(trials)))
# print('Average: %s' % (get_average(trials)))
# print('Most common result: %s' % (most_common_result))
# print('Most common frequency: %s' % (most_common_frequency))

# sorted_trials = sorted(trials)

# counter = collections.Counter(sorted_trials)

# values = list(counter.values())
# keys = list(counter.keys())

# y_max = math.ceil(most_common_frequency / 5) * 5
# x_max = max(trials)

# plt.plot(keys, values, 'ro')
# plt.axis([0, x_max, 0, y_max])
# plt.show()



