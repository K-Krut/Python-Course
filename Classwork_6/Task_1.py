
# 1. Створити клас ОСОБА (прізвище, ім'я, по батькові, дата народження, стать та ін.).
# 2. Визначити методи для зміни і читання значень полів даного класу.
# 3. Перевантажити необхідні оператори.
# 4. Створити похідний клас СЛУЖБОВЕЦЬ з додатковими полями -
# організація, спеціальність за дипломом, посада, оклад, стаж роботи.
# Визначити необхідні дані, методи або перевантажити необхідні оператори.
# 5. Розробити клас ОРГАНІЗАЦІЯ, що містить послідовнясть
# об'єктів класу СЛУЖБОВЕЦЬ. Знайти кількість осіб, стаж роботи яких перевищує наперед задане значення.
# 6. Для роботи із послідовністю об'єктів побудувати та використати ітератор.

from datetime import datetime


class Person:
    def __init__(self, name, surname, date, gender):
        if not (isinstance(name, str) or isinstance(name, str)) or len(name) < 1 or len(surname) < 1:
            raise ValueError('invalid input')
        if not (gender == 'male' or gender == 'female'):
            raise ValueError('invalid input')
        get_date = lambda d: datetime.strptime(d, '%d.%m.%Y').date() <= datetime.today().date()
        if not (get_date(date)):
            raise ValueError('invalid input')
        self._name = name
        self._surname = surname
        self._date = date
        self._gender = gender

    @property
    def get_name(self):
        return self._name

    @property
    def get_surname(self):
        return self._surname

    @property
    def get_date(self):
        return self._date

    @property
    def get_gender(self):
        return self._gender

    @get_name.setter
    def get_name(self, name):
        self._name = name

    @get_surname
    def get_surname(self, surname):
        self._surname = surname

    @get_date.setter
    def get_date(self, date):
        self._date = date

    @get_gender.setter
    def get_gender(self, gender):
        self._gender = gender


class Worker(Person):
    def __init__(self, name, surname, date, gender, oraganization, specialty, position, salary, work_experience):
        super(Worker, self).__init__(name, surname, date, gender)
        if not (isinstance(salary, int) or isinstance(work_experience, int)):
            raise ValueError('invalid input')
        if not isinstance(position, str) or len(position) < 1:
            raise ValueError('inva;id input')
        self._oraganization = oraganization
        self._specialty = specialty
        self._position = position
        self._salary = salary
        self._work_experience = work_experience

    @property
    def get_oraganization(self):
        return self._oraganization

    @property
    def get_specialty(self):
        return self._specialty

    @property
    def get_position(self):
        return self._position

    @property
    def get_salary(self):
        return self._salary

    @property
    def get_work_experience(self):
        return self._work_experience

    @get_oraganization.setter
    def get_oraganization(self, org):
        self._oraganization = org

    @get_specialty.setter
    def get_specialty(self, speciality):
        self._specialty = speciality

    @get_position.setter
    def get_position(self, position):
        self._position = position

    @get_salary.setter
    def get_salary(self, salary):
        self._salary = salary

    @get_work_experience.setter
    def get_work_experience(self, exp):
        self._work_experience = exp


class Organization:
    def __init__(self, name, location, workers_amount):
        self._name = name
        self._location = location
        self._worker_amount = workers_amount
        self._workers = []

