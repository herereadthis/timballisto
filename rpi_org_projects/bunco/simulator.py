"""Simulate a dice game."""

from bunco import Player

player1 = Player()
player2 = Player()

player1.roll()
player2.roll()

result1 = player1.get_result()
result2 = player2.get_result()

print('Player 1 %s' % (result1))
print('Player 2 %s' % (result2))
