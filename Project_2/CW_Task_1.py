"""Task 1
 Create a class Rectangle with attributes length and width,
 each of which defaults to 1. Provide methods that calculate the perimeter and
 the area of the rectangle. Also, provide setter and getter for the length and width attributes.
 The setter should verify that length and width are each floating-point numbers larger than 0.0 and less than 20.0."""


class Rectangle:
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

    def set_data(self, length, width):
        if 0.0 <= length <= 20.0 and 0.0 <= width <= 20.0:
            self.length = length
            self.width = width
        else:
            print('invalid input')

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def get_area(self):
        return self.width * self.length

    def get_perimeter(self):
        return 2 * (self.width + self.length)

    def __str__(self):
        return "length: %.2f, width: %.2f, area: %.3f, perimeter: %.3f" % \
               (self.length, self.width, self.get_area(), self.get_perimeter())


def main():
    rectangle = Rectangle(2.2, 5.1)
    print(rectangle)
    try:
        obj_length = float(input('length: '))
        obj_width = float(input('width: '))
        if rectangle.set_data(obj_length, obj_width):
            print(rectangle)
        print(rectangle)
    except(ValueError, SyntaxError, TypeError, UnboundLocalError):
        print('invalid input')


main()

