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
        self._name = name
        self._teacher = teacher
        self._duration = duration
        self._program = program
        self._capacity = capacity
        self._price = price
        self._course_id = uuid.uuid1()
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
    def __init__(self, filename='Courses.json'):
        self._file = filename
        self.x = None

    @staticmethod
    def get_teacher(teacher):
        with open('Teachers.json') as file:
            teachers_data = json.load(file)
        for i in teachers_data:
            if teacher == teachers_data[i]['name'] + ' ' + teachers_data[i]['surname']:
                return i
        return "None"

    def create_local_course(self, name, teacher, duration, program, type_course, capacity, price):
        with open(self._file) as file:
            database = json.load(file)
        if "Local" not in database:
            database["Local"] = {}
            course_id = uuid.uuid1()
            if not (course_id in database['Local']):
                database['Local'][course_id] = {
                    'name': name,
                    'duration': duration,
                    'program': program,
                    'capacity': capacity,
                    'price': price,
                    'type': type_course,
                    'teacher_id': self.get_teacher(teacher)
                }
                json.dump(database, open('Tickets_data.json', 'w'), indent=4)
            else:
                return self.create_local_course(name, teacher, duration, program, type_course, capacity, price)

    def create_offset_course(self, name, teacher, duration, program, place, capacity, price):
        with open(self._file) as file:
            database = json.load(file)
        if "Local" not in database:
            database["Local"] = {}
            course_id = uuid.uuid1()
            if not (course_id in database['Local']):
                database['Local'][course_id] = {
                    'name': name,
                    'duration': duration,
                    'program': program,
                    'capacity': capacity,
                    'price': price,
                    'place': place,
                    'teacher_id': self.get_teacher(teacher)
                }
                json.dump(database, open('Tickets_data.json', 'w'), indent=4)
            else:
                return self.create_offset_course(name, teacher, duration, program, place, capacity, price)

    def delete_course(self, id_course):
        with open(self._file) as file:
            data = json.load(file)
        if id_course in data["Local"]:
            data["Local"].pop(id_course)
        elif id_course in data["OffSet"]:
            data["OffSet"].pop(id_course)
        else:
            raise ValueError('Invalid input')

    # удаление из джейсона

    def __str__(self):
        return '\n'.join([f'{i.name}' for i in self.x])
        # return '\n'.join([f'{i._name}\nProgram: {i._program}\nTime:{i._duration}'
        #                   f'Pleces left: {i._capaity}'] for i in self.x)


class Teacher:
    def __init__(self, name, surname, course):
        self._name = name
        self._surname = surname
        self._course = course
        self._id = uuid.uuid1()

    @property
    def _teacher_name(self):
        return self._name

    @property
    def _teacher_surname(self):
        return self._surname

    @property
    def _course(self):
        return self._course

    @property
    def _teacher(self):
        return self._name, self._surname

    @property
    def get_teacher_info(self):
        return self._name, self._surname, self._course

    @property
    def get_teacher_id(self):
        return self._id

    @_teacher_name.setter
    def _teacher_name(self, name):
        self._teacher_name = name

    @_teacher_surname.setter
    def _teacher_surname(self, surname):
        self._teacher_surname = surname

    @_course.setter
    def _course(self, new_course):
        self._course = new_course

    @_teacher.setter
    def _teacher(self, info):
        self._name = info[0]
        self._surname = info[1]

    @get_teacher_info.setter
    def get_teacher_info(self, info):
        self._name = info.get[0]
        self._surname = info.get[1]
        self._course = info.get[2]

    def __str__(self):
        return f'{self._name} {self._surname} -- {self._course}'


class Teachers:
    def __init__(self, filename):
        self._file = filename

    def add_teacher(self):
        pass

    def delete_teacher(self):
        pass

    def see_teachers(self):
        pass


class Academy:
    # ICourseFactory
    def __init__(self, location=ACADEMY_LOCATION):
        self._location = location

# оббертки а не наследование

# delete course, add course, view my courses, enroll course
# view all courses, view my courses, add teacher, delete teacher
