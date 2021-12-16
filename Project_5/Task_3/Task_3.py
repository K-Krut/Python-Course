import json
import uuid
from abc import abstractmethod, ABC

ACADEMY_LOCATION = 'Lviv'


class ICourse(ABC):
    @property
    @abstractmethod
    def name_course_(self):
        pass

    @property
    @abstractmethod
    def teacher_(self):
        pass

    @property
    @abstractmethod
    def course_duration_(self):
        pass

    @property
    @abstractmethod
    def program_(self):
        pass

    @property
    @abstractmethod
    def capacity_(self):
        pass

    @property
    @abstractmethod
    def price_(self):
        pass

    @property
    @abstractmethod
    def id_course_(self):
        pass

    @id_course_.setter
    @abstractmethod
    def id_course_(self, id):
        pass

    @property
    @abstractmethod
    def teacher_id_(self):
        pass

    @price_.setter
    @abstractmethod
    def price_(self, cost):
        pass

    @name_course_.setter
    @abstractmethod
    def name_course_(self, name):
        pass

    @teacher_.setter
    @abstractmethod
    def teacher_(self, teacher):
        pass

    @course_duration_.setter
    @abstractmethod
    def course_duration_(self, time):
        pass

    @program_.setter
    @abstractmethod
    def program_(self, program):
        pass

    @capacity_.setter
    @abstractmethod
    def capacity_(self, num):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ILocalCourse(ABC):
    @property
    @abstractmethod
    def course_type_(self):
        pass

    @course_type_.setter
    @abstractmethod
    def course_type_(self, new_type):
        pass


class IOffsiteCourse(ABC):
    @property
    @abstractmethod
    def place_(self):
        pass

    @place_.setter
    @abstractmethod
    def place_(self, town):
        pass


class ITeacher(ABC):
    @property
    @abstractmethod
    def teacher_name_(self):
        pass

    @property
    @abstractmethod
    def teacher_surname_(self):
        pass

    @property
    @abstractmethod
    def courses_(self):
        pass

    @property
    @abstractmethod
    def get_teacher(self):
        pass

    @property
    @abstractmethod
    def teacher_info_(self):
        pass

    @property
    @abstractmethod
    def teacher_id_(self):
        pass

    @teacher_name_.setter
    @abstractmethod
    def teacher_name_(self, name):
        pass

    @teacher_surname_.setter
    @abstractmethod
    def teacher_surname_(self, surname):
        pass

    @courses_.setter
    @abstractmethod
    def courses_(self, new_courses):
        pass

    @get_teacher.setter
    def get_teacher(self, info):
        pass

    @teacher_info_.setter
    def teacher_info_(self, info):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class ICourseFactory(ABC):
    @abstractmethod
    def add_teacher(self, teacher):
        pass

    @abstractmethod
    def add_local_course(self, course_):
        pass

    @abstractmethod
    def add_offset_course(self, course_):
        pass

    @abstractmethod
    def see_courses(self):
        pass

    @abstractmethod
    def see_teachers(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Course(ICourse):
    def __init__(self, name, teacher, duration_, program, capacity, price):
        if self.check_course_exist(name):
            raise ValueError(f'course with the {name} exist')
        self._name = name
        self._teacher = teacher
        self._duration = duration_
        self._program = program
        self._capacity = capacity
        self._price = price
        self._course_id = uuid.uuid1()
        self._teacher = teacher[0]
        self._teacher_id = teacher[1]

    @staticmethod
    def check_course_exist(name):
        data_courses = json.load(open('Courses_.json'))
        return any(j == name for j in [i["name"] for i in (data_courses['Local'] | data_courses['OffSet']).values()])

    @property
    def name_course_(self):
        return self._name

    @property
    def teacher_(self):
        return self._teacher

    @property
    def program_(self):
        return self._program

    @property
    def capacity_(self):
        return self._capacity

    @property
    def price_(self):
        return self._price

    @property
    def id_course_(self):
        return self._course_id

    @id_course_.setter
    def id_course_(self, id):
        self._course_id = id

    @property
    def teacher_id_(self):
        return self._teacher_id

    @price_.setter
    def price_(self, cost):
        self._price = cost

    @name_course_.setter
    def name_course_(self, name):
        self._name = name

    @teacher_.setter
    def teacher_(self, teacher):
        self._teacher = teacher

    @property
    def course_duration_(self):
        return self._duration

    @course_duration_.setter
    def course_duration_(self, duration_):
        self._duration = duration_

    @program_.setter
    def program_(self, program):
        self._program = program

    @capacity_.setter
    def capacity_(self, num):
        self._capacity = num

    def __str__(self):
        return f'{self._name}\nProgram:{self._program}\nTeacher: {self._teacher}\n' \
               f'Time:{self._duration} hours Places: {self._capacity} Price: {self._price} UAH'


class LocalCourse(Course, ILocalCourse):
    def __init__(self, name, teacher, duration, program, type_, capacity, price):
        self._name = None
        if self.check_course_exist(name):
            raise ValueError(f'course {name} exist')
        super().__init__(name, teacher, duration, program, capacity, price)
        self._type = type_

    @staticmethod
    def check_course_exist(course):
        data = json.load(open('Courses_.json'))['Local']
        return any(data[i]['name'] == course for i in data)

    @property
    def course_type_(self):
        return self._type

    @course_type_.setter
    def course_type_(self, new_type):
        if not (new_type == 'offline' or new_type == 'online'):
            raise ValueError('invalid input')
        self._type = new_type

    def __str__(self):
        return f'{self._name}\nProgram:{self._program}\nTeacher: {self._teacher}\n' \
               f'Time:{self._duration} hours\tType: {self._type}\tPrice: {self._price} UAH'


class OffSetCourse(Course, IOffsiteCourse):
    def __init__(self, name, teacher, duration, program, capacity, price, place):
        if self.check_course_exist(name):
            raise ValueError(f'course {name} exist')
        super(OffSetCourse, self).__init__(name, teacher, duration, program, capacity, price)
        self._place = place

    @staticmethod
    def check_course_exist(course):
        data = json.load(open('Courses_.json'))['OffSet']
        return any(data[i]['name'] == course for i in data)

    @property
    def place_(self):
        return self._place

    @place_.setter
    def place_(self, town):
        self._place = town

    def __str__(self):
        return f'{self._name}\nProgram:{self._program}\nTeacher: {self._teacher}\n' \
               f'Time:{self._duration} hours\tPlace: {self._place}\tPrice: {self._price} UAH'


class Teacher(ITeacher):
    def __init__(self, name, surname, courses=[]):
        self._name = name
        self._surname = surname
        self._courses = courses
        self._id = uuid.uuid1()

    def add_courses(self, *courses):
        if not self.check_all_courses_exist(courses):
            raise ValueError('not all courses exist')
        data = json.load(open('Teachers.json'))
        for i in data:
            if str(self._id) == i:
                i["courses"] = courses
        json.dump(data, open('Teachers.json', 'w'), indent=4)

    @staticmethod
    def check_all_courses_exist(courses):
        data_courses = json.load(open('Courses_.json'))
        return all(i in [i["name"] for i in (data_courses['Local'] | data_courses['OffSet']).values()] for i in courses)

    @property
    def teacher_name_(self):
        return self._name

    @property
    def teacher_surname_(self):
        return self._surname

    @property
    def courses_(self):
        return self._courses

    @property
    def get_teacher(self):
        return self._name, self._surname

    @property
    def teacher_info_(self):
        return f'{self._name} {self._surname}', f'{self._id}'

    @property
    def teacher_id_(self):
        return self._id

    @teacher_name_.setter
    def teacher_name_(self, name):
        self._name = name

    @teacher_surname_.setter
    def teacher_surname_(self, surname):
        self._surname = surname

    @courses_.setter
    def courses_(self, new_courses):
        self._courses = new_courses

    @get_teacher.setter
    def get_teacher(self, info):
        self._name = info[0]
        self._surname = info[1]

    @teacher_info_.setter
    def teacher_info_(self, info):
        self._name = info.get[0]
        self._surname = info.get[1]
        self._courses = info.get[2]

    def __str__(self):
        return f'{self._name} {self._surname}\n'

    def __repr__(self):
        return f'{self._name} {self._surname} -- {self._courses}'


class CourseFactory(ICourseFactory):
    def __init__(self):
        self._location = ACADEMY_LOCATION

    def add_teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError('invalid input')
        self.file_teacher_write(teacher)

    def file_teacher_write(self, teacher):
        with open('Teachers.json') as file:
            database = json.load(file)
            id_of_teacher = str(teacher.teacher_id_)
        if self.check_teacher_exist(teacher):
            raise ValueError('teacher exist')
        database[id_of_teacher] = {
            'name': teacher.teacher_name_,
            'surname': teacher.teacher_surname_,
            'courses': []
        }
        json.dump(database, open('Teachers.json', 'w'), indent=4)

    @staticmethod
    def check_teacher_exist(teacher):
        database = json.load(open('Teachers.json'))
        return str(teacher.teacher_id_) in database and \
               any(i['name'] + i['surname'] == teacher.teacher_name_ + teacher.teacher_surname_ for i in database)

    def add_local_course(self, course_):
        if not isinstance(course_, LocalCourse):
            raise TypeError('invalid input')
        self.file_course_write('Local', course_)

    def add_offset_course(self, course_):
        if not isinstance(course_, OffSetCourse):
            raise TypeError('invalid input')
        self.file_course_write('OffSet', course_)

    @staticmethod
    def file_course_write(type_of_course, course):
        database = json.load(open('Courses_.json'))
        course_id = str(course.id_course_)
        if type_of_course not in database:
            database[type_of_course] = {}
        if course_id in database[type_of_course] and \
                any(database[i]['name'] == course.name_course_ for i in database):
            raise ValueError('course exist')
        if type_of_course == 'Local':
            database[type_of_course][course_id] = {
                'name': course.name_course_,
                'duration': course.course_duration_,
                'program': course.program_,
                'capacity': course.capacity_,
                'price': course.price_,
                'type': course.course_type_,
                'teacher': course.teacher_,
            }
        if type_of_course == 'OffSet':
            database[type_of_course][course_id] = {
                'name': course.name_course_,
                'duration': course.course_duration_,
                'program': course.program_,
                'capacity': course.capacity_,
                'price': course.price_,
                'place': course.place_,
                'teacher': course.teacher_,
            }
        json.dump(database, open('Courses_.json', 'w'), indent=4)

    @staticmethod
    def delete_teacher(teacher_id):
        data = json.load(open('Teachers.json'))
        if teacher_id not in data:
            raise ValueError('teacher don`t exist')
        data.pop(teacher_id)
        json.dump(data, open('Teachers.json', 'w'), indent=4)

    @staticmethod
    def delete_course(id_course):
        with open('Courses_.json') as file:
            data = json.load(file)
        if id_course in data["Local"]:
            data["Local"].pop(id_course)
            json.dump(data, open('Courses_.json', 'w'), indent=4)
        elif id_course in data["OffSet"]:
            data["OffSet"].pop(id_course)
            json.dump(data, open('Courses_.json', 'w'), indent=4)
        else:
            raise ValueError('Invalid input')

    def see_courses(self):
        database = json.load(open('Courses_.json'))
        return '\n'.join([''.join([f'{j}: {i[j]}\n' for j in i.keys()])
                          for i in (database["Local"] | database['OffSet']).values()])\


    def see_teachers(self):
        teachers_data = json.load(open('Teachers.json'))
        return '\n\n'.join([f'{teachers_data[i]["name"]} {teachers_data[i]["surname"]}\n'
                            f'Courses:\n{teachers_data[i]["courses"]}' for i in teachers_data])

    def __str__(self):
        return f'Courses: {self.see_courses()}\n\nTeachers: {self.see_teachers()}'


CourseFactory_1 = CourseFactory()
print(CourseFactory_1)
CourseFactory_1.add_teacher(Teacher("Sara", "Bravo"))
CourseFactory_1.add_local_course(LocalCourse('TESTLOCAL', Teacher("NAME", "SURNAME").teacher_info_,
                                             56, ['34', '34'], "online", 233, 45555))
