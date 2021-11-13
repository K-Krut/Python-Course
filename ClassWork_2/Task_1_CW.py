class Rectangle:
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

    def set_length(self, length):
        self.length = length if 0.0 <= length <= 20.0 else print('invalid input')

    def set_width(self, width):
        self.width = width if 0.0 <= width <= 20.0 else print('invalid input')

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def get_area(self):
        return self.width * self.length

    def get_perimeter(self):
        return 2 * (self.width + self.length)


def main():
    rectangle = Rectangle(2.2, 5.1)
    print("width: ", rectangle.get_width(),"length: ", rectangle.get_length())
    print("area: ", rectangle.get_area(), "perimeter: ", rectangle.get_perimeter())

    try:
        obj_length = float(input("length: "))
        obj_width = float(input("width: "))
    except(ValueError, SyntaxError, TypeError):
        print('invalid input')

    rectangle.set_length(obj_length)
    rectangle.set_width(obj_width)
    print("area: ", rectangle.get_area(), "perimeter: ", rectangle.get_perimeter())

main()
