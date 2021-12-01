import math


class Rational:
   
    def __init__(self, numerator, denominator=1):
        if not (isinstance(numerator, int) or isinstance(denominator, int)):
            raise TypeError("Type Error")
        if denominator == 0:
            raise ZeroDivisionError(f'Rational({numerator}, 0)')
        g = math.gcd(numerator, denominator)
        self._numerator = numerator // g
        self._denominator = denominator // g

    def __add__(a, b):
        return Rational(a._numerator * b._denominator + a._denominator * b._numerator, a._denominator * b._denominator)

    def __sub__(a, b):
        return Rational(a._numerator * b._denominator - a._denominator * b._numerator, a._denominator * b._denominator)

    def __mul__(a, b):
        return Rational(a._numerator * b._numerator, a._denominator * b._denominator)

    def __truediv__(a, b):
        return Rational(a._numerator * b._denominator, b._numerator * a._denominator)

    # __iadd__ = __add__
    # __isub__ = __sub__
    # __imul__ = __mul__
    # __idiv__ = __truediv__

    def _cmp(self, other):
        a = self._numerator / self._denominator
        b = other._numerator / other._denominator
        return 0 if a == b else 1 if a > b else -1

    def __eq__(a, b):
        if not isinstance(a, Rational):
            raise ValueError('Invalid data type')
        return a._cmp(b) == 0

    def __le__(a, b):
        if not isinstance(a, Rational):
            raise ValueError('Invalid data type')
        return a._cmp(b) <= 0

    def __lt__(a, b):
        if not isinstance(a, Rational):
            raise ValueError('Invalid data type')
        return a._cmp(b) < 0

    def __ge__(a, b):
        if not isinstance(a, Rational):
            raise ValueError('Invalid data type')
        return a._cmp(b) >= 0

    def __gt__(a, b):
        if not isinstance(a, Rational):
            raise ValueError('Invalid data type')
        return a._cmp(b) > 0

    def __ne__(a, b):
        if not isinstance(a, Rational):
            raise ValueError('Invalid data type')
        return a._cmp(b) != 0

    def __bool__(a):
        return bool(a._numerator)

    def __str__(self):
        return f'{self._numerator}' if self._denominator == 1 else f'{self._numerator}/{self._denominator}'

    @property
    def get_normal_format(self):
        return f'{self._numerator}' if self._denominator == 1 else f'{self._numerator}/{self._denominator}'

    @property
    def get_float_point_format(self):
        return f'{round(self._numerator / self._denominator, 2)}'


fraction_1 = Rational(8, 10)
fraction_2 = Rational(4, 12)
fraction_3 = Rational(1, 3)
fraction_4 = Rational(0, 1)
fraction_5 = Rational(4)

print(
    fraction_1,
    fraction_2,
    fraction_5
)

print(
    fraction_1 + fraction_2,
    fraction_1 - fraction_2,
    fraction_1 * fraction_2,
    fraction_1 / fraction_2
)

print(
    fraction_1.get_normal_format,
    fraction_1.get_float_point_format
)

print(
    fraction_1 < fraction_2,
    fraction_1 > fraction_2,
    fraction_1 == fraction_2,
    fraction_1 != fraction_2,
    fraction_2 == fraction_3
)
