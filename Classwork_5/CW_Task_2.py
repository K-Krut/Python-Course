def add_field(cls):
    def adder(*args, **kwargs):
        new_instance = cls(*args, **kwargs)
        new_instance.count = 1
        return new_instance
    return adder


@add_field
class Student:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname

    def __str__(self):
        return f'{self._name} {self._surname}'


x = Student('Petro', 'Petrov')
print(x.__dict__)
