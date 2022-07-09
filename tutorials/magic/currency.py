"""Overload operators to make a currency converter."""

from fixerio import Fixerio

fxrio = Fixerio()
currencies = ['USD', 'CNY', 'GBP', 'EUR', 'CHF', 'JPY']
new_rates = fxrio.latest(base='USD', symbols=currencies)['rates']
new_rates['USD'] = 1


class Currency:
    """Demo currency overloading."""

    rates = new_rates

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
        """Define the - operator."""
        converted_value = self.convert_other_base(other)
        try:
            return Currency(self.value - converted_value, self.unit)
        except TypeError:
            print('Error: unsupported type')

    def __isub__(self, other):
        """Define the -= operator."""
        converted_value = self.convert_other_base(other)
        try:
            self.value -= converted_value
            return self
        except TypeError:
            print('Error: unsupported type')

    def __rsub__(self, other):
        """Define int - currency."""
        other_currency = Currency(other, 'USD')
        try:
            return other_currency - self
        except TypeError:
            print('Error: unsupported type')

    def __add__(self, other):
        """Define the + operator."""
        converted_value = self.convert_other_base(other)
        try:
            return Currency(converted_value + self.value, self.unit)
        except TypeError:
            print('Error: unsupported type')

    def __iadd__(self, other):
        """Define the += operator."""
        converted_value = self.convert_other_base(other)
        try:
            self.value += converted_value
            return self
        except TypeError:
            print('Error: unsupported type')

    def __radd__(self, other):
        """Define int + currency."""
        other_currency = Currency(other, 'USD')
        try:
            return self + other_currency
        except TypeError:
            print('Error: unsupported type')

    def __str__(self):
        """Return string representation of currency instance."""
        return '{0:,.2f} {1}'.format(self.value, self.unit)


if __name__ == "__main__":
    print('\nIf I have 1 US dollar, 1 Euro, and 1 British Pound,')
    print('then how much is that in US Dollars? (x + y + z)')
    x = Currency(1, 'USD')
    y = Currency(1, 'EUR')
    z = Currency(1, 'GBP')
    print('x = Currency(1, \'USD\'): {}'.format(x))
    print('y = Currency(1, \'EUR\'): {}'.format(y))
    print('z = Currency(1, \'GBP\'): {}'.format(z))
    print('x + y + z: {}'.format(x + y + z))

    print('\nAddition')
    print('x + y: {}'.format(x + y))
    print('y + x: {}'.format(y + x))
    print('1 + x: {}'.format(1 + x))
    print('1 + y: {}'.format(1 + y))
    print('x + 1: {}'.format(x + 1))
    print('y + 1: {}'.format(y + 1))
    print('x + \'foo\': {}'.format(x + 'foo'))

    print('\nAssignment')
    x_copy = Currency(1, 'USD')
    x_copy += 2
    print('x += 2: {}'.format(x_copy))
    y_copy = Currency(1, 'EUR')
    y_copy -= 2
    print('y -= 2: {}'.format(y_copy))

    print('\nSubtraction')
    print('y - x: {}'.format(y - x))
    print('x - y: {}'.format(x - y))
    print('2 - x: {}'.format(2 - x))
    print('2 - y: {}'.format(2 - y))
