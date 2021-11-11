"""Task 2
Create a class called Rational for performing arithmetic with fractions.
Write a program to test your class. Use integer variables to represent the
private data of the class – the numerator and the denominator. Provide a __init__() method that
enables an object of this class to be initialized when it’s declared. The __init__() should contain default
parameter values in case no initializers are provided and should store the fraction in reduced form. For example,
the fraction 2/4 would be stored in the object as 1 in the numerator and 2 in the denominator.
Provide public methods that perform each of the following tasks:
- printing Rational numbers in the form a/b, where a is the numerator and b is the denominator.
- printing Rational numbers in floating-point format.
"""

import math


# the main class
# noinspection PyMethodParameters,PyProtectedMember
class Rational:
    def __init__(self, numerator, denominator=1):
        # checking the correction of the arguments' type
        if not (isinstance(numerator, int) or isinstance(denominator, int)):
            raise TypeError("Type Error")
        # classical check
        if denominator == 0:
            raise ZeroDivisionError(f'Rational({numerator}, 0)')
            # if all demands are met
        g = math.gcd(numerator, denominator)
        self._numerator = numerator // g
        self._denominator = denominator // g

    # function for arithmetic operations on fractions
    def __str__(self):
        return f'{self._numerator}' if self._denominator == 1 else f'{self._numerator}/{self._denominator}'

    def __add__(a, b):
        return Rational(a._numerator * b._denominator + a._denominator * b._numerator, a._denominator * b._denominator)

    def __sub__(a, b):
        return Rational(a._numerator * b._denominator - a._denominator * b._numerator, a._denominator * b._denominator)

    def __mul__(a, b):
        return Rational(a._numerator * b._numerator, a._denominator * b._denominator)

    def __truediv__(a, b):
        return Rational(a._numerator * b._denominator, b._numerator * a._denominator)

    # getters for numerator and denominator
    #
    # def numerator(self):
    #     return self._numerator
    #
    # def denominator(self):
    #     return self._denominator

    # functions for formatted displaying of a fraction
    def get_normal_format(self):
        return f'{self._numerator}' if self._denominator == 1 else f'{self._numerator}/{self._denominator}'

    def get_float_point_format(self):
        return f'{round(self._numerator / self._denominator, 2)}'


fraction_1 = Rational(8, 10)
fraction_2 = Rational(4, 12)
print(fraction_1, fraction_2, Rational(4))
print(fraction_1 + fraction_2, fraction_1 - fraction_2, fraction_1 * fraction_2, fraction_1 / fraction_2, fraction_1.get_normal_format())
print(fraction_1.get_float_point_format())
