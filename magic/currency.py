"""Overload operators to make a currency converter."""

from fixerio import Fixerio

fxrio = Fixerio(base='USD')
currencies = ['USD', 'GBP', 'EUR', 'CHF', 'JPY']
rates = fxrio.latest(symbols=currencies)['rates']

class Currency:
    rates = fxrio.latest(symbols=currencies)['rates']

if __name__ == "__main__":
    print(rates)