# # Task 3.
# # The class GROUP contains a sequence of instances of the class STUDENT.
# # The class STUDENT contains the students name, surname, record book number and grades.
# # Determine the required attributes-data and attributes-methods in classes GROUP and STUDENT.
# # Find the average score of each student. Output to the standard output stream
# # the five students with the highest average score.
# # Assume that there can be no more than 20 students in a group, as well as students with the same name and surname.
# from itertools import islice
#
#
# class Student:
#     """Class for creating students
#
#         This class provides creating instance with information about a student
#
#     """
#
#     def __init__(self, name, surname, number, *grades):
#         """Constructor of the main class Student
#
#         :param name: name of the student, must be a string
#         :param surname: surname of the student, must be a string
#         :param number: mobile phone number of the student, must be a string
#         :param grades: contains grades of the student, must be a tuple with ints
#
#         :raise ValueError: in cases of trying to add a student with the same Name and Surname as the existent one has
#         and the grades of the student isn't int of is less then 60 or bigger than 100
#
#         """
#         self._name = name
#         self._surname = surname
#         self._number = number
#         for i in grades:
#             if not 59 < i < 101:
#                 raise ValueError('Grades invalid input')
#         self._grades = grades
#         self._average_score = None
#
#     @property
#     def grades(self):
#         return self._grades
#
#     @grades.setter
#     def grades(self, marks):
#         for i in marks:
#             if not 59 < i < 101:
#                 raise ValueError('Grades invalid input')
#         self._grades = marks
#         self._average_score = None
#
#     @property
#     def get_average(self):
#         if self._average_score is None:
#             return sum(self._grades) / len(self._grades)
#         return self._average_score
#
#     @property
#     def data(self):
#         return self._name, self._surname
#
#     def class_visiting(self):
#         pass
#
#     def __str__(self):
#         """Return the string representation of the current student
#         :return: String representation.
#         :rtype: str
#
#         **Example**:
#
#         .. doctest::
#
#             ">>>print(Student)"
#             Alex, Smith, +380448168725, (86, 99, 100, 77, 81)
#
#         """
#         return f'{self._name}, {self._surname}, {self._number}, {self._grades}\n'
#
#
# class Group:
#     """Class that represents a group
#
#         This class provides methods and properties for creating a group of students
#
#     """
#
#     def __init__(self, faculty, course, name, *students):
#         """Constructor of the Group class
#
#         :param faculty: contains the name of the faculty | string
#         :param course: course of the group, (must be int in range [1; 6])
#         :param name: name of the group | string
#         :param students: contains all students should be added to the group | tuple of instances of the "Student class"
#
#         :raise  ValueError: If len of the faculty name isn't 3 or 4,
#          course isn't int and isn't in range [1, 6],
#          len of the group name isn't 5, should be like this "TI-01",
#          number of students is bigger than 20
#
#         """
#         if not 2 < len(faculty) < 5:
#             raise ValueError('invalid input')
#         self._faculty = faculty
#         if course not in [1, 2, 3, 4, 5, 6]:
#             raise TypeError('Invalid input')
#         self._course = course
#         if not len(name) == 5:
#             raise ValueError('invalid input')
#         self._name = name
#         if len(students) > 20:
#             raise ValueError('group cant be > 20')
#         # arr = []
#         # """List for saving data about already exciting students
#         #
#         #     The list contains tuples like this (name, surname),
#         #     where name is the name of a student and
#         #     surname id the surname of a student
#         #
#         #     The list is used for checking the correction of input data about students,
#         #     so there can't be students with the same Name and Surname
#         #
#         # """
#         #
#         # for i, j in zip(students, tuple(i + 1 for i in range(len(students)))):
#         #     if not any(i.data == x.data for x in tuple(islice(students, j, len(students)))):
#         #         arr.append(i)
#         #     else:
#         #         raise ValueError('not unique')
#         self._group = Group.check(students)
#
#     def __str__(self):
#         """Return the string representation of the current group
#                :return: String representation.
#                :rtype: str
#
#                **Example**:
#
#                .. doctest::
#
#                    # >>>print(Group)
#                    Group info:
#                    TEF, 4, TP-02
#                    Alex, Smith, +380448168725, (86, 99, 100, 77, 81)
#                    John, Carman, +3804356855, (60, 60, 98, 63, 61)
#                    Andrew, Asquid, +380868168425, (86, 99, 88, 77, 81)
#
#         """
#         return f'Group info:\n{self._faculty}, {self._course}, {self._name}\n' + ''.join([str(i) for i in self._group])
#
#     @staticmethod
#     def check(students):
#         """Function is used for checking the correction of the current group
#         so in a group can't be students with the same Name and Surname
#         :param students:
#         :return: arr | array of the Student class instances
#
#         """
#         arr = []
#         for i, j in zip(students, tuple(i + 1 for i in range(len(students)))):
#             if not any(i.data == x.data for x in tuple(islice(students, j, len(students)))):
#                 arr.append(i)
#             else:
#                 raise ValueError('not unique')
#         return arr
#
#     @classmethod
#     def best_students(self):
#         """Return the string representation of the best 5 students of the group
#
#             The function at first sort the group by avarage score in
#                 :return: Array representation.
#                 :rtype: array of Student class instances
#
#                 """
#         return sorted(self._group, key=lambda x: x.get_average,  reverse=True)[:5]
#         # return '\n'.join([f'{x._name} {x._surname} {x.get_average}'
#         #                   for x in sorted(self._group, key=lambda x: x.get_average,  reverse=True)[:5]])
#
#
# St1 = Student("Alex", "Smith", "+380448168725", 86, 99, 100, 77, 81)
# St2 = Student("John", "Carman", "+3804356855", 60, 60, 98, 63, 61)
# St3 = Student("Andrew", "Asquid", "+380868168425", 86, 99, 88, 77, 81)
# St4 = Student("Julia", "Ianon", "+3804649955", 78, 78, 65, 63, 61)
# St5 = Student("Julia", "Ivanova", "+3804649855", 60, 60, 65, 63, 61)
# St6 = Student("Mikola", "Matskevich", "+3804346565", 99, 98, 90, 88, 79)
# St7 = Student("Michail", "Stefanovich", "+3804645655", 60, 98, 65, 63, 61)
# St8 = Student("Michail", "Stefanovich", "+38046465455", 60, 98, 65, 63, 61)
#
# group_ = Group("TEF", 4, "TP-02", St1, St2, St3, St4, St5, St6, St7)
#
# print(group_)
# print('\n'.join([f'{x._name} {x._surname} {x.get_average}' for x in group_.best_students()]))
# # St1.grades = tuple(int(input()) for i in range(5))
# # print(St1.grades)
#


from itertools import islice


class Student:
    """Class for creating students
        This class provides creating instance with information about a student
    """

    def __init__(self, name, surname, number, *grades):
        """Constructor of the main class Student
        :param name: name of the student, must be a string
        :param surname: surname of the student, must be a string
        :param number: mobile phone number of the student, must be a string
        :param grades: contains grades of the student, must be a tuple with ints
        :raise ValueError: in cases of trying to add a student with the same Name and Surname as the existent one has
        and the grades of the student isn't int of is less then 60 or bigger than 100
        """
        self._name = name
        self._surname = surname
        self._number = number
        if not len(grades) == 5:
            raise ValueError('Grades invalid input')
        for i in grades:
            if not 59 < i < 101:
                raise ValueError('Grades invalid input')
        self._grades = grades
        self._average_score = None

    @property
    def grades(self):
        return self._grades

    @grades.setter
    def grades(self, marks):
        for i in marks:
            if not 59 < i < 101:
                raise ValueError('Grades invalid input')
        self._grades = marks
        self._average_score = None

    @property
    def get_average(self):
        if self._average_score is None:
            return sum(self._grades) / len(self._grades)
        return self._average_score

    @property
    def data(self):
        return self._name, self._surname

    @data.setter
    def data(self, info):
        self._name = info[0]
        self._surname = info[1]

    def class_visiting(self):
        pass

    def __str__(self):
        """Return the string representation of the current student
        :return: String representation.
        :rtype: str
        **Example**:
        .. doctest::
            ">>>print(Student)"
            Alex, Smith, +380448168725, (86, 99, 100, 77, 81)
        """
        return f'{self._name}, {self._surname}, {self._number}, {self._grades}\n'


class Group:
    """Class that represents a group
        This class provides methods and properties for creating a group of students
    """
    def __init__(self, faculty, course, name, *students):
        """Constructor of the Group class
        :param faculty: contains the name of the faculty | string
        :param course: course of the group, (must be int in range [1; 6])
        :param name: name of the group | string
        :param students: contains all students should be added to the group | tuple of instances of the "Student class"
        :raise  ValueError: If len of the faculty name isn't 3 or 4,
         course isn't int and isn't in range [1, 6],
         len of the group name isn't 5, should be like this "TI-01",
         number of students is bigger than 20
        """
        if not 2 < len(faculty) < 5:
            raise ValueError('invalid input')
        self._faculty = faculty
        if course not in [1, 2, 3, 4, 5, 6]:
            raise TypeError('Invalid input')
        self._course = course
        if not len(name) == 5:
            raise ValueError('invalid input')
        self._name = name
        if len(students) > 20:
            raise ValueError('group cant be > 20')
        # arr = []
        # """List for saving data about already exciting students
        #
        #     The list contains tuples like this (name, surname),
        #     where name is the name of a student and
        #     surname id the surname of a student
        #
        #     The list is used for checking the correction of input data about students,
        #     so there can't be students with the same Name and Surname
        #
        # """
        #
        # for i, j in zip(students, tuple(i + 1 for i in range(len(students)))):
        #     if not any(i.data == x.data for x in tuple(islice(students, j, len(students)))):
        #         arr.append(i)
        #     else:
        #         raise ValueError('not unique')
        self._group = Group.check(students)

    def __str__(self):
        """Return the string representation of the current group
               :return: String representation.
               :rtype: str
               **Example**:
               .. doctest::
                   # >>>print(Group)
                   Group info:
                   TEF, 4, TP-02
                   Alex, Smith, +380448168725, (86, 99, 100, 77, 81)
                   John, Carman, +3804356855, (60, 60, 98, 63, 61)
                   Andrew, Asquid, +380868168425, (86, 99, 88, 77, 81)
        """
        return f'Group info:\n{self._faculty}, {self._course}, {self._name}\n' + ''.join([str(i) for i in self._group])

    @staticmethod
    def check(students):
        """Function is used for checking the correction of the current group
        so in a group can't be students with the same Name and Surname
        :param students:
        :return: arr | array of the Student class instances
        """
        arr = []
        for i, j in zip(students, tuple(i + 1 for i in range(len(students)))):
            if not any(i.data == x.data for x in tuple(islice(students, j, len(students)))):
                arr.append(i)
            else:
                raise ValueError('not unique')
        return arr

    def best_students(self):
        """Return the string representation of the best 5 students of the group
            The function at first sort the group by average score in
                :return: Array representation.
                :rtype: array of Student class instances
        """
        # return '\n'.join([f'{x._name} {x._surname} {x.get_average}'
        #               for x in sorted(self._group, key=lambda x: x.get_average,  reverse=True)[:5]])
        return sorted(self._group, key=lambda x: x.get_average,  reverse=True)[:5]


St1 = Student("Alex", "Smith", "+380448168725", 86, 99, 100, 77, 81)
St2 = Student("John", "Carman", "+3804356855", 60, 60, 98, 63, 61)
St3 = Student("Andrew", "Asquid", "+380868168425", 86, 99, 88, 77, 81)
St4 = Student("Julia", "Ianon", "+3804649955", 78, 78, 65, 63, 61)
St5 = Student("Julia", "Ivanova", "+3804649855", 60, 60, 65, 63, 61)
St6 = Student("Mikola", "Matskevich", "+3804346565", 99, 98, 90, 88, 79)
St7 = Student("Michail", "Stefanovich", "+3804645655", 60, 98, 65, 63, 61)
St8 = Student("Michail", "Stefanovich", "+38046465455", 60, 98, 65, 63, 61)

group_ = Group("TEF", 4, "TP-02", St1, St2, St3, St4, St5, St6, St7)

print(group_)
print(''.join(str(i) for i in group_.best_students()))


# St1.grades = tuple(int(input()) for i in range(5))
# print(St1.grades)
