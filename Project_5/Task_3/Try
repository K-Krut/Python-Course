# A software academy teaches two types of courses: local courses that
# are held in some of the academy’s local labs and offsite courses
# held in some other town outside of the academy’s headquarters.
#
# Each course has a name, a teacher assigned to teach it and a course
# program (sequence of topics).
#
# Each teacher has a name and knows the courses he or she teaches.
#
# Both courses and teachers could be printed in human-readable text form.
#
# All your courses should implement ICourse. Teachers should implement ITeacher.
#
# Local and offsite courses should implement
# ILocalCourse and IOffsiteCourse respectively. Courses and teachers should be
# created only through the ICourseFactory interface implemented by a class
# named CourseFactory. Write a program that will form courses of software academy.
import json
import uuid

ACADEMY_LOCATION = 'Lviv'


class Course:
    def __init__(self, name, teacher, duration, program, capacity, price):
        if self.check_course_exist(name):
            raise ValueError(f'course with the {name} exist')
        self._name = name
        self._teacher = teacher
        self._duration = duration
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
    def duration_(self):
        return self._duration

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
    ####################################

    @price_.setter
    def price_(self, cost):
        self._price = cost

    @name_course_.setter
    def name_course_(self, name):
        self._name = name

    @teacher_.setter
    def teacher_(self, teacher):
        self._teacher = teacher

    # @duration_.setter
    # def duration(self, time):
    #     self._duration = time

    @program_.setter
    def program_(self, program):
        self._program = program

    @capacity_.setter
    def capacity_(self, num):
        self._capacity = num

    def __str__(self):
        return f'{self._name}\nProgram:{self._program}\nTeacher: {self._teacher}\n' \
               f'Time:{self._duration} hours Places: {self._capacity} Price: {self._price} UAH'


class LocalCourse(Course):
    def __init__(self, name, teacher, duration, program, type_, capacity, price):
        if self.check_course_exist(name):
            raise ValueError(f'course {name} exist')
        super(LocalCourse, self).__init__(name, teacher, duration, program, capacity, price)
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


class OffSetCourse(Course):
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


class ICourses:
    def __init__(self, filename, args=None):
        if isinstance(args, (LocalCourse, OffSetCourse)):
            self.file_course_write(self.get_type(args), args)
        if isinstance(args, list) and self.check_all_are_courses(args):
            self.add_courses(args)
        self._file = filename

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
                'duration': course.duration_,
                'program': course.program_,
                'capacity': course.capacity_,
                'price': course.price_,
                'type': course.course_type_,
                'teacher': course.teacher_,
            }
        if type_of_course == 'OffSet':
            database[type_of_course][course_id] = {
                'name': course.name_course_,
                'duration': course.duration_,
                'program': course.program_,
                'capacity': course.capacity_,
                'price': course.price_,
                'place': course.place_,
                'teacher': course.teacher_,
            }
        json.dump(database, open('Courses_.json', 'w'), indent=4)

    def add_courses(self, args):
        for i in args:
            self.file_course_write(self.get_type(i), i)

    @staticmethod
    def get_type(course):
        return 'Local' if isinstance(course, LocalCourse) else \
            ('OffSet' if isinstance(course, OffSetCourse) else 'Course')

    @staticmethod
    def check_all_are_courses(args):
        return all(isinstance(i, (LocalCourse, OffSetCourse)) for i in args)
        # return all(isinstance(i, (Course, LocalCourse, OffSetCourse)) for i in args)

    def add_local_course(self, course_):
        if not isinstance(course_, LocalCourse):
            raise TypeError('invalid input')
        self.file_course_write('Local', course_)

    def add_offset_course(self, course_):
        if not isinstance(course_, OffSetCourse):
            raise TypeError('invalid input')
        self.file_course_write('OffSet', course_)

    def delete_course(self, id_course):
        with open(self._file) as file:
            data = json.load(file)
        if id_course in data["Local"]:
            data["Local"].pop(id_course)
            json.dump(data, open(self._file, 'w'), indent=4)
        elif id_course in data["OffSet"]:
            data["OffSet"].pop(id_course)
            json.dump(data, open(self._file, 'w'), indent=4)
        else:
            raise ValueError('Invalid input')

    def __str__(self):
        database = json.load(open('Courses_.json'))
        return '\n'.join([''.join([f'{j}: {i[j]}\n' for j in i.keys()])
                          for i in (database["Local"] | database['OffSet']).values()])


class Teacher:
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

    # @courses_.setter
    # def get_course(self, new_courses):
    #     self._courses = new_courses
    #
    # @get_teacher.setter
    # def get_teacher(self, info):
    #     self._name = info[0]
    #     self._surname = info[1]
    #
    # @teacher_info_.setter
    # def get_teacher_info(self, info):
    #     self._name = info.get[0]
    #     self._surname = info.get[1]
    #     self._courses = info.get[2]

    def __str__(self):
        return f'{self._name} {self._surname}\n'

    def __repr__(self):
        return f'{self._name} {self._surname} -- {self._courses}'


class ITeachers:
    def __init__(self, filename='Teachers.json', args=None):
        print(type(args), args)
        self.add_many_teachers(args)
        self._file = filename

    @property
    def file_name(self):
        return self._file

    def add_teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError('invalid input')
        self.file_teacher_write(teacher)

    def add_many_teachers(self, args):
        for i in args:
            print(i)
            self.add_teacher(i)

    @staticmethod
    def delete_teacher(teacher_id):
        data = json.load(open('Teachers.json'))
        if teacher_id not in data:
            raise ValueError('teacher don`t exist')
        data.pop(teacher_id)
        json.dump(data, open('Teachers.json', 'w'), indent=4)

    def file_teacher_write(self, teacher):
        with open('Teachers.json') as file:
            database = json.load(file)
            id_of_teacher = str(teacher.teacher_id_)
        if not self.check_teacher_exist(teacher):
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

    def __str__(self):
        teachers_data = json.load(open('Teachers.json'))
        return '\n\n'.join([f'{teachers_data[i]["name"]} {teachers_data[i]["surname"]}\n'
                            f'Courses:\n{teachers_data[i]["courses"]}' for i in teachers_data])

    def __repr__(self):
        teachers_data = json.load(open('Teachers.json'))
        return '\n\n'.join([f'{teachers_data[i]["name"]} {teachers_data[i]["surname"]}\n'
                            f'Courses:\n{teachers_data[i]["courses"]}\nID: {i}' for i in teachers_data])


class Academy:
    # ICourseFactory
    def __init__(self, courses_, teachers_):
        if not (isinstance(courses_, ICourses) or isinstance(teachers_, ITeachers)):
            raise TypeError('invalid input')
        self._location = ACADEMY_LOCATION
        self._courses = courses_
        self._teachers = teachers_

    def see_courses(self):
        return f'Courses:\n{self._courses}'

    def see_teachers(self):
        return f'Teachers:\n{self._teachers}'

    def __str__(self):
        return f'Courses:\n{self._courses}\n\n\nTeachers:\n{self._teachers}'


Teachers_obj = ITeachers()
Courses_obj = ICourses('Courses_.json')
Academy_obj = Academy(Courses_obj, Teachers_obj)

T = Teacher("GGG", "H456")
T1 = Teacher("RYT", "546")
T2 = Teacher("FGJFG", "R5Y4EH")
T3 = Teacher("DFGHDFGHDFGH", "456456H")

G = Course('TEST', T.teacher_info_, 34, ('gJGFfh', 'fgh', 'fgh', 'fh'), 765, 42000)
# print(T)
# print(G)
# print(G.teacher_)
# K = LocalCourse('TESTLOCAL', T.teacher_info_, 56, ['34', '34'], "online", 233, 45555)
# J = LocalCourse('TTTTT', T.teacher_info_, 56, ['34', '34'], "online", 233, 45555)
# KEK = ICourses('Courses_.json', [K, J])

# print(KEK)
print(ITeachers('Teachers.json', [T, T1, T2, T3]))


# print(Academy_obj)




# оббертки а не наследование
# delete course, add course, view my courses, enroll course
# view all courses, view my courses, add teacher, delete teacher
# name, teacher, duration, program, type_, capacity, price):(self, name, teacher, duration, program, capacity, price):


# print(ICourses())
# A = Course('AAA', Teacher("A", "B"), 34, ('gfh', 'fgh', 'fgh', 'fh'), 765, 42000)
# B = Course('BBB', Teacher("C", "D"), 34, ('gfh', 'fgh', 'fgh', 'fh'), 765, 42000)
# C = Course('CCC', Teacher("E", "F"), 34, ('gfh', 'fgh', 'fgh', 'fh'), 765, 42000)
# D = Course('DDD', Teacher("G", "H"), 34, ('gJGFfh', 'fgh', 'fgh', 'fh'), 765, 42000)
# G = Course('TEST', Teacher("G", "H"), 34, ('gJGFfh', 'fgh', 'fgh', 'fh'), 765, 42000)
# E = Academy(A, B, C, D)
# # E = Academy([])
# print(E)

#
# K = LocalCourse('TESTLOCAL', Teacher("G_TEST", "H"), 56, ['34', '34'], "online", 233, 45555)
# F = ICourses()
# print(F)
# F.create_local_course(K)
# print(F)
# Course_1 = LocalCourse('PYTHON DEVELOPMENT', )
