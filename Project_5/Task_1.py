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

_DAYS_BEFORE_MONTH = [0]  # -1 is a placeholder for indexing purposes.
dbm = 0
for dim in _DAYS_IN_MONTH[1:]:
    _DAYS_BEFORE_MONTH.append(dbm)
    dbm += dim
del dbm, dim


# def _days_before_year(year):
#     "year -> number of days before January 1st of year."
#     y = year - 1
#     return y * 365 + y // 4 - y // 100 + y // 400
#
#
# def _days_in_month(year, month):
#     "year, month -> number of days in that month in that year."
#     assert 1 <= month <= 12, month
#     if month == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         return 29
#     return _DAYS_IN_MONTH[month]
#
#
# def _days_before_month(year, month):
#     "year, month -> number of days in year preceding first day of month."
#     assert 1 <= month <= 12, 'month must be in 1..12'
#     return _DAYS_BEFORE_MONTH[month] + (month > 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
#
#
# def _ymd2ord(year, month, day):
#     "year, month, day -> ordinal, considering 01-Jan-0001 as day 1."
#     assert 1 <= month <= 12, 'month must be in 1..12'
#     dim = _days_in_month(year, month)
#     assert 1 <= day <= dim, ('day must be in 1..%d' % dim)
#     return _days_before_year(year) + _days_before_month(year, month) + day
#

class Calendar:
    """Concrete date type.
    Constructors:
    __new__()
    fromtimestamp()
    today()
    fromordinal()
    Operators:
    __repr__, __str__
    __eq__, __le__, __lt__, __ge__, __gt__, __hash__
    __add__, __radd__, __sub__ (add/radd only with timedelta arg)
    Methods:
    timetuple()
    toordinal()
    weekday()
    isoweekday(), isocalendar(), isoformat()
    ctime()
    strftime()
    Properties (readonly):
    year, month, day
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

    def __add__(self, d):
        global __day, __month, __year
        __day, __month, __year = self._day,  self._month, self._year
        for i in range(d):
            __day += 1
            print(__day)
            if __day > _DAYS_IN_MONTH[__month]:
                d -= i
                if d < 0:
                    d = 0
                __day = 1
                __month += 1
                print(d, __day, __month)
                if __month > 12:
                    __month = 1
                    __year += 1
                    print(d, __day, __month)
                    break
        return Calendar(__year, __month, __day + 1)
        # if not isinstance(other, Calendar):
        #     raise ValueError('Invalid data type')
        # y = self._year - 1
        # days_before_date = y * 365 + y // 4 - y // 100 + y // 400 + (_DAYS_BEFORE_MONTH[self._month] +
        #     (self._month > 2 and self._year % 4 == 0 and (self._year % 100 != 0 or self._year % 400 == 0))) + self._day
        # print(days_before_date)
        # sum_of_days = days_before_date + other._day
        # if 0 <= sum_of_days <= _MAXORDINAL:
        #     print(sum_of_days)

    # def __add__(self, other):
    #     "Add a date to a timedelta."
    #     if isinstance(other, Calendar):
    #         o = self.toordinal() + other.days
    #         if 0 < o <= _MAXORDINAL:
    #             return type(self).fromordinal(o)
    #         raise OverflowError("result out of range")
    #     return NotImplemented


#     __radd__ = __add__
#
#     def __sub__(self, other):
#         """Subtract two dates, or a date and a timedelta."""
#         if isinstance(other, timedelta):
#             return self + timedelta(-other.days)
#         if isinstance(other, date):
#             days1 = self.toordinal()
#             days2 = other.toordinal()
#             return timedelta(days1 - days2)
#         return NotImplemented
#


A = Calendar(2020, 2, 12)
B = Calendar(2020, 2, 5)
C = Calendar(2020, 2, 5)
D = Calendar(2021, 11, 12)
print(A)
# print(_DAYS_BEFORE_MONTH[3])
# print(_days_before_month(2021, 3))
# print(A + B)
# print(A == B)
# print(A <= B)
# print(A < B)
# print(A > B)
# print(A >= B)
# print(A != B)
# print(C != B)
print(D + 51)
