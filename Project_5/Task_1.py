# 1. Modify the class Rational of Lab No2 to perform the following tasks:
# - adding two Rational numbers. The result should be stored in reduced form;
# - subtracting two Rational numbers. The result should be stored in reduced form;
# - multiplying two Rational numbers. The result should be stored in reduced form;
# - dividing two Rational numbers. The result should be stored in reduced form;
# - comparison two Rational numbers.

import math


class Rational:
    """Class for creating right fractions
    Operators:
    __str__
    __eq__, __le__, __lt__, __ge__, __gt__, __ne__, __bool__
    __add__, __sub__, __mul__, __truediv__
    Methods:
    _cmp(), float_point_format()
    """
    def __init__(self, numerator, denominator=1):
        """Constructor
        :param numerator
        :param denominator, by default 1
        :raise  ValueError, ZeroDivisionError
        """
        if not (isinstance(numerator, int) or isinstance(denominator, int)):
            raise TypeError("Type Error")
        if denominator == 0:
            raise ZeroDivisionError(f'Rational({numerator}, 0)')
        self._numerator = numerator
        self._denominator = denominator
        g = math.gcd(numerator, denominator)
        self._numerator = numerator // g
        self._denominator = denominator // g

    @property
    def numerator(self):
        return self._numerator

    @numerator.setter
    def numerator(self, num):
        self._numerator = num

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, num):
        self._denominator = num

    def _reducing(self):
        g = math.gcd(self._numerator, self._denominator)
        return self._numerator // g, self._denominator // g

    def __add__(a, b):
        """ a + b """
        return Rational(a._numerator * b._denominator + a._denominator * b._numerator, a._denominator * b._denominator)

    def __sub__(a, b):
        """ a - b """
        return Rational(a._numerator * b._denominator - a._denominator * b._numerator, a._denominator * b._denominator)

    def __mul__(a, b):
        """ a * b """
        return Rational(a._numerator * b._numerator, a._denominator * b._denominator)

    def __truediv__(a, b):
        """ a / b"""
        return Rational(a._numerator * b._denominator, b._numerator * a._denominator)

    # __iadd__ = __add__
    # __isub__ = __sub__
    # __imul__ = __mul__
    # __idiv__ = __truediv__

    def _cmp(a, b):
        """Function for comparison"""
        if a._denominator == b._denominator:
            return 0 if a._numerator == b._numerator else 1 if a._numerator > b._numerator else -1
        if a._numerator == b._numerator:
            return 0 if a._numerator == b._numerator else 1 if a._numerator < b._numerator else -1
        g = math.lcm(a._denominator, b._denominator)
        A_num = a.numerator * (g / a.denominator)
        B_num = b.numerator * (g / b.denominator)
        return 0 if A_num == B_num else 1 if A_num > B_num else -1

    def __eq__(a, b):
        """a == b"""
        if not isinstance(b, Rational):
            raise ValueError('Invalid data type')
        return a._cmp(b) == 0

    def __le__(a, b):
        """a <= b"""
        if not isinstance(b, Rational):
            raise ValueError('Invalid data type')
        return a._cmp(b) <= 0

    def __lt__(a, b):
        """a < b"""
        if not isinstance(b, Rational):
            raise ValueError('Invalid data type')
        return a._cmp(b) < 0

    def __ge__(a, b):
        """a >= b"""
        if not isinstance(b, Rational):
            raise ValueError('Invalid data type')
        return a._cmp(b) >= 0

    def __gt__(a, b):
        """a > b"""
        if not isinstance(b, Rational):
            raise ValueError('Invalid data type')
        return a._cmp(b) > 0

    def __ne__(a, b):
        """ a != b """
        if not isinstance(b, Rational):
            raise ValueError('Invalid data type')
        return a._cmp(b) != 0

    def __str__(self):
        """Return the string representation of the fraction
               :return: String representation.
               :rtype: str
               **Example**:
               .. doctest::
                   # >>>print(Fraction(4, 12))
                   1/3
        """
        return f'{self._numerator}/{self._denominator}'

    def float_point_format(self):
        """Return the string representation of the fraction
               :return: String representation.
               :rtype: str
               **Example**:
               .. doctest::
                   # >>>print(Rational(8, 10).float_point_format)
                   0.8
        """
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
    fraction_1,
    fraction_1.float_point_format()
)

print(
    fraction_1 < fraction_2,
    fraction_1 > fraction_2,
    fraction_1 == fraction_2,
    fraction_1 != fraction_2,
    fraction_2 == fraction_3
)
