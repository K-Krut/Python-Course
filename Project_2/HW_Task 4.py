"""Task 4.
Create a class BINARY TREE that contains background information of product prices
(product code, price of 1 product). The tree is sorted by product codes.
From the keyboard enter data on the number of products in the format:
product code, number of products. Using a tree, find the cost of products
(cost = quantity * price of one product).
"""


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


tree = Tree()
tree.insert((6, 3.12))
tree.insert((14, 20))
tree.insert((3, 45.75))
tree.insert((7, 3.2))
tree.insert((9, 125.89))
print(tree.search(14))
print(tree.get_cost(14, 56))
print_tree(tree)
print(get_products_cost(tree))



















# re.split('[-+#]', s_marks)
















"""Class for creating tree

    This class provides creating tree that consists with data about products

"""

"""Constructor of the main class Tree

:param value: consists code and 
"""
