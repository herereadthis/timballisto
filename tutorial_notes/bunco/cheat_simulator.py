"""Simulate a dice game."""

from bunco import CheatSwappedDice, CheatLoadedDice


def main():
    """Run the main simulator."""
    player1 = CheatSwappedDice()
    player2 = CheatLoadedDice()
    player1_wins = 0
    player2_wins = 0
    simulations = input('How many simulations [100000]?') or 100000

    try:
        for i in range(int(simulations)):
            player1.roll()
            player2.roll()

            player1.cheat()
            player2.cheat()

            while player1.get_sum() == player2.get_sum():
                # Always roll if tied
                player1.roll()
                player2.roll()

                player1.cheat()
                player2.cheat()

            if player1.get_sum() > player2.get_sum():
                player1_wins = player1_wins + 1
            else:
                player2_wins = player2_wins + 1

        print('Player 1 wins: %s' % (player1_wins))
        print('Player 2 wins: %s' % (player2_wins))

    except TypeError:
        print('Must be number.')


if __name__ == '__main__':
    main()
