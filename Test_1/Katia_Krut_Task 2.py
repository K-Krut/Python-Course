import datetime


class Timer:
    def __init__(self):
        data = datetime.datetime.now()
        self.__hours = data.hour
        self.__minutes = data.minute
        self.__seconds = data.second

    @property
    def get_hours(self):
        return self.__hours

    @get_hours.setter
    def get_hours(self, value):
        if not (isinstance(int, value) or 0 <= value <= 23):
            raise ValueError('Invalid data input')
        self.__hours = value

    @property
    def get_minutes(self):
        return self.__minutes

    @get_minutes.setter
    def get_minutes(self, value):
        if not (isinstance(int, value) or 0 <= value <= 59):
            raise ValueError('Invalid data input')
        self.__minutes = value

    @property
    def get_seconds(self):
        return self.__seconds

    @get_seconds.setter
    def get_seconds(self, value):
        if not (isinstance(int, value) or 0 <= value <= 59):
            raise ValueError('Invalid data input')
        self.__seconds = value

    # def standart_time(self):
    #     return f"\n{self.__hours} годин, {self.__minutes} хвилин, {self.__seconds} секунд"


    def meridiem_time(self):
        if self.__hours <= 12:
            return f"\n{self.__hours} a.m. {self.__minutes} хвилин, {self.__seconds} секунд\n"
        else:
            return f"\n{self.__hours} p.m. {self.__minutes} хвилин, {self.__seconds} секунд\n"

    def __str__(self):
        return f"\n{self.__hours} годин, {self.__minutes} хвилин, {self.__seconds} секунд"


time = Timer()
print(time, time.meridiem_time())
