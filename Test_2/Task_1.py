# 1. Створити клас ОСОБА (прізвище, ім'я, по батькові, дата народження, стать та ін.).
# 2. Визначити методи для зміни і читання значень полів даного класу.
# 3. Перевантажити необхідні оператори.
# 4. Створити похідний клас СЛУЖБОВЕЦЬ з додатковими полями -
# організація, спеціальність за дипломом, посада, оклад, стаж роботи.
# Визначити необхідні дані, методи або перевантажити необхідні оператори.
# 5. Розробити клас ОРГАНІЗАЦІЯ, що містить послідовнясть
# об'єктів класу СЛУЖБОВЕЦЬ. Знайти кількість осіб, стаж роботи яких перевищує наперед задане значення.
# 6. Для роботи із послідовністю об'єктів побудувати та використати ітератор.
import uuid
from datetime import datetime


WORK_EXPERIENCE = 10


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
        self._id = uuid.uuid1()

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
    def name_setter(self, name):
        self._name = name

    @get_surname.setter
    def surname_setter(self, surname):
        self._surname = surname

    @get_date.setter
    def date_setter(self, date):
        self._date = date

    @get_gender.setter
    def gender_setter(self, gender):
        self._gender = gender

    def __str__(self):
        return f'Name: {self._name}\tSurname: {self._surname} -- {self._gender}\nDate of bd: {self._date}'


class Worker(Person):
    def __init__(self, name, surname, date, gender, organization, specialty, position, salary, work_experience):
        super(Worker, self).__init__(name, surname, date, gender)
        if not (isinstance(salary, int) or isinstance(work_experience, int)):
            raise ValueError('invalid input')
        if not isinstance(position, str) or len(position) < 1:
            raise ValueError('invalid position input')
        if salary < 0 or 40 < work_experience < 0:
            raise ValueError('invalid salary/work_experience input')
        self._organization = organization
        self._specialty = specialty
        self._position = position
        self._salary = salary
        self._work_experience = work_experience

    @property
    def get_organization(self):
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

    @get_organization.setter
    def organization_setter(self, org):
        self._organization = org

    @get_specialty.setter
    def specialty_setter(self, speciality):
        self._specialty = speciality

    @get_position.setter
    def position_setter(self, position):
        self._position = position

    @get_salary.setter
    def salary_setter(self, salary):
        self._salary = salary

    @get_work_experience.setter
    def work_experience_setter(self, exp):
        self._work_experience = exp

    def __str__(self):
        return f'Worker:\nName: {self._name}\tSurname: {self._surname} -- {self._gender}\nDate of bd: {self._date}\n' \
               f'{self._organization}:\n\tPosition: {self._position}\t' \
                                     f'Salary: {self._salary}\n\tDiploma: {self._specialty}\t' \
                                     f'Experience:{self._work_experience}'


class Organization:
    def __init__(self, name, location, *args):
        if not isinstance(name, str) or len(name) < 1:
            raise ValueError('invalid name input')
        if not isinstance(location, str) or len(location) < 1:
            raise ValueError('invalid location input')
        self._name = name
        self._location = location
        self._workers = list(args)
        self._counter = 0

    def add_worker(self, worker):
        if not isinstance(worker, Worker):
            raise ValueError('invalid input')
        self._workers.append(worker)

    def __delete__(self, instance):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if self._counter < len(self._workers):
            self._counter += 1
            return self._workers[self._counter - 1]
        else:
            raise StopIteration

    def get_workers_by_experience(self):
        amount = 0
        for i in self._workers:
            if i.get_work_experience > WORK_EXPERIENCE:
                amount += 1
        return amount

    def __str__(self):
        return f'{self._name}\nLocation: {self._location}' + '\n'.join(str(i) for i in self._workers)


Worker_1 = Worker('N', 'SN', '12.10.1999', 'male', 'SMTH', 'dsg', 'aaaa', 23444, 3)
Worker_2 = Worker('K', 'Surname', '12.10.1999', 'male', 'SMTH', 'FGH', 'DFG', 23444, 3)
Worker_3 = Worker('F', 'Surname', '12.10.1999', 'male', 'SMTH', 'FGH', 'DFG', 23444, 24)
Worker_4 = Worker('L', 'Surname', '12.10.1999', 'male', 'SMTH', 'FGH', 'DFG', 23444, 12)
Worker_5 = Worker('M', 'Surname', '12.10.1999', 'male', 'SMTH', 'FGH', 'DFG', 23444, 3)

Organization_1 = Organization('SOME_NAME', 'Somewhere', Worker_1, Worker_2, Worker_3, Worker_4, Worker_5)

print(Organization_1)

for i in Organization_1:
    print(i)

print(Organization_1.get_workers_by_experience())


