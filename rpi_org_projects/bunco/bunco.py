"""Make Bunco classes."""

from random import randint


class Player:
    """Create player class."""

    def __init__(self):
        """Initialize stuff."""
        self.dice = []

    # This is a set method
    def roll(self):
        """Role the dice."""
        # clear dice settings when rolling
        self.dice = []
        for i in range(3):
            self.dice.append(randint(1, 6))

    # This is get method
    def get_dice(self):
        """Fetch the dice result."""
        return self.dice

    def get_result(self):
        """Print the result in a pretty format."""
        result = self.get_dice()
        if result == []:
            return 'has not rolled'
        else:
            rolled = 'rolled %s, %s, %s' % (result[0], result[1], result[2])
            roll_sum = sum(result)
            return '%s for %s total' % (rolled, roll_sum)
