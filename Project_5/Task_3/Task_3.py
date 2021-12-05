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

ACADEMY_LOCATION = 'Lviv'


class Course:
    def __init__(self, name, teacher, duration, program, capacity, price):
        self._name = name
        self._teacher = teacher
        self._duration = duration
        self._program = program
        self._capacity = capacity
        self._price = price
        # self._description = description

    @property
    def _name_course(self):
        return self._name

    @property
    def _teacher(self):
        return self._teacher

    @property
    def _duration(self):
        return self._duration

    @property
    def _program(self):
        return self._program

    @property
    def _capacity(self):
        return self._capaity

    @_name_course.setter
    def _name_course(self, name):
        self._name_course = name

    @_teacher.setter
    def _teacher(self, teacher):
        self._teacher = teacher

    @_duration.setter
    def _duration(self, time):
        self._duration = time

    @_program.setter
    def _program(self, prog):
        self._program = prog

    @_capacity.setter
    def _capacity(self, num):
        self._capacity = num

    def __str__(self):
        return f'{self._name}\nProgram:{self._program}\nTeacher: {self._teacher}\n' \
               f'Time:{self._duration}\tPlaces: {self._capacity}'


class LocalCourse(Course):
    def __init__(self, name, teacher, duration, program, type, capacity, price):
        super.__init__(name, teacher, duration, program, capacity, price)
        self._type = type
        # self._place = place

    @property
    def _type(self):
        return self._type

    @_type.setter
    def _type(self, new_type):
        self._type = new_type

    def __str__(self):
        return f'{self._name}\nProgram:{self._program}\nTeacher: {self._teacher}\n' \
               f'Time:{self._duration}\tType: {self._type}'


class OffSetCourse(Course):
    def __init__(self, name, teacher, duration, program, capacity, price, place):
        super.__init__(name, teacher, duration, program, capacity, price)
        self._place = place

    @property
    def _place(self):
        return self._place

    @_place.setter
    def _place(self, town):
        self._place = town

    def __str__(self):
        return f'{self._name}\nProgram:{self._program}\nTeacher: {self._teacher}\n' \
               f'Time:{self._duration}\tPlace: {self._place}'


class ILocalCourse:
    def __init__(self, filename, x):
        self._file = filename
        self.x = x

    def create_course(self, type):
        if type == 'local':
            pass
            #запись в джейсон
        elif type == 'offset':
            pass
            # Запись в джейсон
        else:
            raise IOError('Invalid input')

    def delete_course(self, Course):
        pass
    # удаление из джейсона

    def __str__(self):
        return '\n'.join([f'{self._name}\nProgram: {self._program}\nTime:{self._duration}'
                          f'Pleces left: {self._capaity}'] for i in self.x)


class Teacher:
    def __init__(self, name, surname, course):
        self._name = name
        self._surname = surname
        self._course = course

    @property
    def _teacher_name(self):
        return self._name

    @property
    def _teacher_surname(self):
        return self._surname

    @property
    def _course(self):
        return self._course

    @_teacher_name.setter
    def _teacher_name(self, name):
        self._teacher_name = name

    @_teacher_surname.setter
    def _teacher_surname(self, surname):
        self._teacher_surname = surname

    @_course.setter
    def _course(self, new_course):
        self._course = new_course

    @property
    def get_teacher_info(self):
        return self._name, self._surname, self._course

    @get_teacher_info.setter
    def get_teacher_info(self, info):
        self._name = info.get[0]
        self._surname = info.get[1]
        self._course = info.get[2]

    def __str__(self):
        return f'{self._name} {self._surname} -- {self._course}'


class Teachers:
    def __init__(self):
        pass


class Academy:
    # ICourseFactory
    def __init__(self, location=ACADEMY_LOCATION):
        self._location = location

# оббертки а не наследование

# delete course, add course, view my courses, enroll course
# view all courses, view my courses, add teacher, delete teacher





