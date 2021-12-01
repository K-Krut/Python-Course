# TI-01
# Create a class CALENDAR. Define methods for creating and working with a CALENDAR instances and overload operations^
# "+=, -=" - for adding and subtracting days, months, years to a given date
# "==, !=, >, >=, <, <=" - for comparing dates.


MIN_YEAR = 1
MAX_YEAR = 9999
_DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
_DAYS_BEFORE_MONTH = [0]


class Calendar:
    """Class for creating right fractions
    Operators:
    __str__
    __eq__, __le__, __lt__, __ge__, __gt__, __ne__
    __iadd__, __isub__, __mul__, __truediv__
    Methods:
    _cmp()
    Attributes:
    __slots__
    year(), month(), day(), _date()
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
        """tuple of date -- (year, month, day)"""
        return self.year, self._month, self._day

    def _cmp(a, b):
        """Function for comparison"""
        return 0 if a._date == b._date else 1 if a._date > b._date else -1

    def __eq__(self, other):
        """a = b """
        if not isinstance(other, Calendar):
            raise ValueError('Invalid data type')
        return self._cmp(other) == 0

    def __le__(self, other):
        """a <= b """
        if not isinstance(other, Calendar):
            raise ValueError('Invalid data type')
        return self._cmp(other) <= 0

    def __lt__(self, other):
        """ a < b """
        if not isinstance(other, Calendar):
            raise ValueError('Invalid data type')
        return self._cmp(other) < 0

    def __ge__(self, other):
        """ a >= b """
        if not isinstance(other, Calendar):
            raise ValueError('Invalid data type')
        return self._cmp(other) >= 0

    def __gt__(self, other):
        """a > b """
        if not isinstance(other, Calendar):
            raise ValueError('Invalid data type')
        return self._cmp(other) > 0

    def __ne__(self, other):
        """ a != b """
        if not isinstance(other, Calendar):
            raise ValueError('Invalid data type')
        return self._cmp(other) != 0

    def __iadd__(self, other):
        """ a += b """
        if not isinstance(other, Calendar):
            raise ValueError('Invalid data type')
        _day = self._day + other._day
        _month = self._month + other._month
        _year = self._year + other._year

        if _day > _DAYS_IN_MONTH[self._month]:
            _day %= _DAYS_IN_MONTH[self._month]
            _month += 1
        if _month > 12:
            _month %= 12
            _year += 1

        return Calendar(_year, _month, _day)

    def __isub__(self, other):
        """ a -= b """
        if not isinstance(other, Calendar):
            raise ValueError('Invalid data type')
        _day = self._day - other._day
        _month = self._month - other._month
        _year = self._year - other._year
        if _day < 0:
            _month -= 1
            _day = _DAYS_IN_MONTH[_month] + _day

        if _month < 1:
            _year -= 1
            _month = 12
        return Calendar(_year, _month, _day)

        def __str__(self):
        """Return the string representation of the current group
               **Example**:
               .. doctest::
                   # >>>print(Calendar(2020, 2, 12))
                   2020/2/12
        """
        return f'{self._year}/{self._month}/{self._day}'

A = Calendar(2020, 2, 12)
B = Calendar(2020, 2, 5)
C = Calendar(2020, 2, 5)
D = Calendar(2021, 12, 2)
E = Calendar(2022, 1, 10)
F = Calendar(1, 1, 20)
print(A)
print(A == B, A <= B, A < B, A > B)
print(A >= B, A != B, C != B)
print(D)
D += F
print(D)
D -= F
print(D)








# print(D, D + 51, E - 11)
# print(D, D + 51)

# D += 32
# print(D)
# D -= 5
# print(D)


# def __add__(self, d=0, m=0, y=0):
#     global __day, __month, __year
#     __day, __month, __year = self._day,  self._month, self._year
#     for i in range(d):
#         __day += 1
#         if __day > _DAYS_IN_MONTH[__month]:
#             d -= i
#             if d < 0:
#                 d = 0
#             __day = 1
#             __month += 1
#             if __month > 12:
#                 __month = 1
#                 __year += 1
#                 break
#     return Calendar(__year + y, __month + m, __day + 1)

# def __sub__(self, d=0, m=0, y=0):
#     global __day, __month, __year
#     __day, __month, __year = self._day,  self._month, self._year
#     for i in range(d):
#         __day -= 1
#         if __day < 1:
#             d -= i
#             if d < 0:
#                 d = 0
#             __day = _DAYS_IN_MONTH[__month - 1]
#             __month -= 1
#             if __month < 0:
#                 __month = 12
#                 __year -= 1
#                 break
#     return Calendar(__year, __month, __day - 1)

# def __iadd__(self, other):
#
#     for i in range():
#         self._day += 1
#         if self._day > _DAYS_IN_MONTH[self._month]:
#             d -= i
#             if d < 0:
#                 d = 0
#             self._day = 1
#             self._month += 1
#             if self._month > 12:
#                 self._month = 1
#                 self._year += 1
#                 break
#     return self

# def __isub__(self, d=0, m=0, y=0):
#     for i in range(d):
#         self._day -= 1
#         if self._day < 1:
#             d -= i
#             if d < 0:
#                 d = 0
#             self._day = _DAYS_IN_MONTH[self._month - 1]
#             self._month -= 1
#             if self._month < 0:
#                 self._month = 12
#                 self._year -= 1
#                 break
#     return self

# def __add__(self, other):
#     if not isinstance(other, Calendar):
#         raise ValueError('Invalid data type')
#     _day = self._day
#     _month = self._month
#     _year = self._year
#     for i in range(other._day):
#         _day += 1
#         if _day > _DAYS_IN_MONTH[_month]:
#             other._day -= i
#             if other._day < 0:
#                 other._day = 0
#             _day = 1
#             _month += 1
#             if _month > 12:
#                  _month = 1
#                  _year += 1
#                  break
#     if _month > 12:
#         while 1 <= _month <= 12:
#             _month -= 12
#             _year += 1

# def __add__(self, d=0, m=0, y=0):
#     global __day, __month, __year
#     __day, __month, __year = self._day,  self._month, self._year
#     for i in range(d):
#         __day += 1
#         if __day > _DAYS_IN_MONTH[__month]:
#             d -= i
#             if d < 0:
#                 d = 0
#             __day = 1
#             __month += 1
#             if __month > 12:
#                 __month = 1
#                 __year += 1
#                 break
#     return Calendar(__year + y, __month + m, __day + 1)

# def __sub__(self, d=0, m=0, y=0):
#     global __day, __month, __year
#     __day, __month, __year = self._day,  self._month, self._year
#     for i in range(d):
#         __day -= 1
#         if __day < 1:
#             d -= i
#             if d < 0:
#                 d = 0
#             __day = _DAYS_IN_MONTH[__month - 1]
#             __month -= 1
#             if __month < 0:
#                 __month = 12
#                 __year -= 1
#                 break
#     return Calendar(__year, __month, __day - 1)

