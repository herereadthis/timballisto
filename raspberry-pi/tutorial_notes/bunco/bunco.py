"""Make Bunco classes."""

from random import randint


class Player:
    """Create player class."""

    def __init__(self):
        """Initialize stuff."""
        self.dice = []
        self.dice_count = 3

    # This is a set method
    def roll(self):
        """Role the dice."""
        # clear dice settings when rolling
        self.dice = []
        for i in range(self.dice_count):
            self.dice.append(randint(1, 6))

    # This is get method
    def get_dice(self):
        """Fetch the dice result."""
        return self.dice

    def get_sum(self):
        """Get the sum."""
        result = self.get_dice()
        if result != []:
            return sum(result)

    def get_result(self):
        """Print the result in a pretty format."""
        result = self.get_dice()
        if result == []:
            return 'has not rolled'
        else:
            rolled = 'rolled %s, %s, %s' % (result[0], result[1], result[2])
            roll_sum = self.get_sum()
            return '%s for %s total' % (rolled, roll_sum)


class CheatSwappedDice(Player):
    """Cheat with swapped dice."""

    def cheat(self):
        """Take last die and make it 6."""
        # -1 means take last in array
        self.dice[-1] = 6


class CheatLoadedDice(Player):
    """Cheat by making dice higher value."""

    def cheat(self):
        """Raise value of each die."""
        for index, die in enumerate(self.dice):
            if die < 6:
                self.dice[index] = die + 1
