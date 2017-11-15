"""Overload operators to make a currency converter."""

from fixerio import Fixerio

fxrio = Fixerio(base='USD')
currencies = ['USD', 'CNY', 'GBP', 'EUR', 'CHF', 'JPY']


class Currency:
    """Demo currency overloading."""

    rates = fxrio.latest(symbols=currencies)['rates']
    rates['USD'] = 1

    def __init__(self, value, unit='USD'):
        """Initilize a money instance."""
        self.value = value
        self.unit = unit

    def convert_other_base(self, other):
        """Covert the value of another instance to self's currency type."""
        base_value = None
        try:
            # convert the other currency instance to the current currency
            # instance.
            base_value = (other.value / Currency.rates[other.unit])
        except AttributeError:
            try:
                # Values with unspecified currency are treated as USD
                base_value = other / Currency.rates['USD']
            except TypeError:
                pass

        if base_value is not None:
            return base_value * Currency.rates[self.unit]

    def __sub__(self, other):
        """Define the + operator."""
        converted_value = self.convert_other_base(other)
        try:
            return Currency(converted_value - self.value, self.unit)
        except TypeError:
            print('Error: unsupported type')

    def __add__(self, other):
        """Define the + operator."""
        converted_value = self.convert_other_base(other)
        try:
            return Currency(converted_value + self.value, self.unit)
        except TypeError:
            print('Error: unsupported type')

    def __str__(self):
        """Return string representation of currency instance."""
        return '{0:,.2f} {1}'.format(self.value, self.unit)


if __name__ == "__main__":
    x = Currency(1, 'USD')
    y = Currency(1, 'EUR')
    z = 1
    n = 'foo'
    print('x: {}'.format(x))
    print('y: {}'.format(y))
    print('z: {}'.format(z))
    print('n: {}'.format(n))
    print('x + y: {}'.format(x + y))
    print('y - x: {}'.format(y - x))
    print('x - y: {}'.format(x - y))
    print('y + z: {}'.format(y + z))
    print('x + n: {}'.format(x + n))
