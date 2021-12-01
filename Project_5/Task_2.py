# 1. Modify the class Rational of Lab No2 to perform the following tasks:
# - adding two Rational numbers. The result should be stored in reduced form;
# - subtracting two Rational numbers. The result should be stored in reduced form;
# - multiplying two Rational numbers. The result should be stored in reduced form;
# - dividing two Rational numbers. The result should be stored in reduced form;
# - comparison two Rational numbers.
# 2.
# TI-01
# Create a class CALENDAR. Define methods for creating and working with a CALENDAR instances and overload operations^
# "+=, -=" - for adding and subtracting days, months, years to a given date
# "==, !=, >, >=, <, <=" - for comparing dates.
import math

MIN_YEAR = 1
MAX_YEAR = 9999
_MAXORDINAL = 3652059
_DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

_DAYS_BEFORE_MONTH = [0]  # 0 is a placeholder for indexing purposes.


class Calendar:
    """Concrete date type.
    Operators:
    """
    __slots__ = '_year', '_month', '_day'

    def __init__(self, year, month, day):
        """Constructor. Arguments: year, month, day """
        if not all(isinstance(i, int) for i in (year, month, day)):
            raise ValueError('incorrect input')
        if not MIN_YEAR <= year <= MAX_YEAR:
            raise ValueError('year must be in [1; 9999]')
        if not 1 <= month <= 12:
            raise ValueError('month must be in [1; 12]')
        days_in_month = 29 if month == 2 and year % 4 == 0 and \
                            (year % 100 != 0 or year % 400 == 0) else _DAYS_IN_MONTH[month]
        if not 1 <= day <= days_in_month:
            raise ValueError('day must be in 1..%d' % days_in_month)
        self._year = year
        self._month = month
        self._day = day

    @property
    def year(self):
        """year (1-9999)"""
        return self._year

    @property
    def month(self):
        """month (1-12)"""
        return self._month

    @property
    def day(self):
        """day (1-31)"""
        return self._day

    @property
    def _date(self):
        return self.year, self._month, self._day

    def _cmp(a, b):
        return 0 if a._date == b._date else 1 if a._date > b._date else -1

    def __eq__(self, other):
        if not isinstance(other, Calendar):
            raise ValueError('Invalid data type')
        return self._cmp(other) == 0

    def __le__(self, other):
        if not isinstance(other, Calendar):
            raise ValueError('Invalid data type')
        return self._cmp(other) <= 0

    def __lt__(self, other):
        if not isinstance(other, Calendar):
            raise ValueError('Invalid data type')
        return self._cmp(other) < 0

    def __ge__(self, other):
        if not isinstance(other, Calendar):
            raise ValueError('Invalid data type')
        return self._cmp(other) >= 0

    def __gt__(self, other):
        if not isinstance(other, Calendar):
            raise ValueError('Invalid data type')
        return self._cmp(other) > 0

    def __ne__(self, other):
        if not isinstance(other, Calendar):
            raise ValueError('Invalid data type')
        return self._cmp(other) != 0

    def __str__(self):
        return f'{self._year}/{self._month}/{self._day}'

    def __add__(self, d=0, m=0, y=0):
        global __day, __month, __year
        __day, __month, __year = self._day,  self._month, self._year
        for i in range(d):
            __day += 1
            if __day > _DAYS_IN_MONTH[__month]:
                d -= i
                if d < 0:
                    d = 0
                __day = 1
                __month += 1
                if __month > 12:
                    __month = 1
                    __year += 1
                    break
        return Calendar(__year + y, __month + m, __day + 1)

    def __sub__(self, d=0, m=0, y=0):
        global __day, __month, __year
        __day, __month, __year = self._day,  self._month, self._year
        for i in range(d):
            __day -= 1
            if __day < 1:
                d -= i
                if d < 0:
                    d = 0
                __day = _DAYS_IN_MONTH[__month - 1]
                __month -= 1
                if __month < 0:
                    __month = 12
                    __year -= 1
                    break
        return Calendar(__year, __month, __day - 1)

    def __iadd__(self, d=0):
        for i in range(d):
            self._day += 1
            if self._day > _DAYS_IN_MONTH[self._month]:
                d -= i
                if d < 0:
                    d = 0
                self._day = 1
                self._month += 1
                if self._month > 12:
                    self._month = 1
                    self._year += 1
                    break
        return self

    def __isub__(self, d=0, m=0, y=0):
        for i in range(d):
            self._day -= 1
            if self._day < 1:
                d -= i
                if d < 0:
                    d = 0
                self._day = _DAYS_IN_MONTH[self._month - 1]
                self._month -= 1
                if self._month < 0:
                    self._month = 12
                    self._year -= 1
                    break
        return self


A = Calendar(2020, 2, 12)
B = Calendar(2020, 2, 5)
C = Calendar(2020, 2, 5)
D = Calendar(2021, 11, 12)
E = Calendar(2022, 1, 10)
print(A)
print(A == B, A <= B, A < B, A > B)
print(A >= B, A != B, C != B)
print(D, D + 51, E - 11)

D += 32
print(D)
D -= 5
print(D)

