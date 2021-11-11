
#
class Tree:

    def __init__(self, value=None):
        self.left = None
        self.right = None
        self._value = value

    def insert(self, value):
        if not (isinstance(value[0], int) or isinstance(value[1], (float, int))) or (value[1] < 0 or value[0] < 0):
            raise ValueError('Invalid input')
        if self._value is None:
            self._value = value
        else:
            if value[0] < self._value[0]:
                if self.left is None:
                    self.left = Tree(value)
                else:
                    self.left.insert(value)
            elif value[0] > self._value[0]:
                if self.right is None:
                    self.right = Tree(value)
                else:
                    self.right.insert(value)

    def search(self, code):
        if not (isinstance(code, int) or code < 0):
            raise ValueError('Invalid input')
        if code == self._value[0]:
            return self._value
        elif code < self._value[0]:
            return self.left.search(code) if self.left is not None else False
        elif code > self._value[0]:
            return self.right.search(code) if self.right is not None else False

    def get_cost(self, code, quantity):
        try:
            return quantity * self.search(code)[1]
        except TypeError:
            print('product doesnt exist')

    @property
    def get_value(self):
        return self._value


def tree_size(tree):
    return 0 if tree is None else tree_size(tree.left) + 1 + tree_size(tree.right)


def add_products(tree):
    try:
        for i in range(int(input('Num of products: ')) - 1):
            tree.insert(tuple(map(int, input('code:quantity: ').split(':'))))
    except ValueError:
        exit()


def get_products_cost(tree):
    total = 0
    max_size = tree_size(tree)
    size = int(input(f'Num of products to get cost (max = {max_size}): '))
    if not (isinstance(size, int) or 0 < size <= max_size):
        raise ValueError('Invalid input')
    for i in range(size):
        a = tuple(map(int, input('Code:Quantity: ').split(':')))
        total += tree.get_cost(a[0], a[1])
    return total


def print_tree(root):
    if root:
        print_tree(root.left)
        print_tree(root.right)
        print(root._value)


from itertools import islice


class Book:
    def __init__(self, name, author, year, publisher):
        self._name = name
        self._author = author
        # if not isinstance(int, year):
        if not isinstance(year, int) or len(str(year)) != 4:
            raise ValueError('invalid input')
        self._year = year
        self._publisher = publisher

    @property
    def get_name(self):
        return self._name

    @get_name.setter
    def get_name(self, value):
        self._name = value

    @property
    def get_author(self):
        return self._author

    @get_author.setter
    def get_name(self, value):
        self._author = value

    @property
    def get_year(self):
        return self._year

    @get_year.setter
    def get_year(self, year):
        if len(year) != 4 or not isinstance(int, year):
            raise ValueError('invalid input')
        self._year = year

    @property
    def get_publisher(self):
        return self._publisher

    @get_publisher.setter
    def get_publisher(self, value):
        self._publisher = value

    def __str__(self):
        return f'{self._name} by {self._author}, published by {self._publisher} in {self._year}'


class Library:
    def __init__(self, *books):
        self._arr = []
        for i, j in zip(books, tuple(i + 1 for i in range(len(books)))):
            if not any(i == x for x in tuple(islice(books, j, len(books)))):
                self._arr.append(i)
            else:
                raise ValueError('not unique')

    def search(self, data):
        return (True, str(data)) if data in self._arr else False

    def search_name(self, data):
        return (True, str(data)) if any(data._name == i._name for i in self._arr) else False
        # return (True, str(data)) if any(data._name == i._name for i in self._arr) else False

    def __str__(self):
        return f'Library:\n   ' + '\n   '.join(str(i) for i in self._arr)


A = Book('A', 'AUTHOR', 1876, 'CHMO')
B = Book('B', 'AUTHOR', 4576, 'GDDG')
C = Book('C', 'AUTHOR', 2345, 'FGHD')
D = Book('D', 'AUTHOR', 8536, 'HDSE')
E = Book('E', 'AUTHOR', 1245, 'HBFE')
F = Book('E', 'AUTHOR', 1245, 'HBFE')

books = Library(A, B, C, D, E, F)
print(books)
print(books.search_name(F))
