# Task 2.
# Pizzeria offers pizza-of-the-day for business lunch.
# The type of pizza-of-the-day depends on the day of week.
# Having a pizza-of-the-day simplifies ordering for customers.
# They don't have to be experts on specific types of pizza.
# Also, customers can add extra ingredients to the pizza-of-the-day.
# Write a program that will form orders from customers.

# в файле храняться ингридиены для пиццы,
# дабы можно было добавлять что-то в пиццу, что есть в файле


from datetime import datetime
import itertools
import uuid
import json


class Products:
    """Class for creating types of dishes
        This class provides creating instance with
        information about chosen dish
    """
    def __init__(self, file_name, string_name):
        """Constructor of the class Ticket
        :param file_name: name of the json file with data about dishes
        :param string_name: name of the dictionary in json file
        """
        with open(file_name) as file:
            self._products_data = json.load(file)
        self._string_name = string_name

    @property
    def get_info(self):
        """Getter of dishes info
        :return info about available dishes
        :rtype dict_items
        """
        return f'{self._products_data.items()}'

    def __str__(self):
        """Return the string representation of the dishes available
               :return: String representation.
               :rtype: str
               **Example**:
               .. doctest::
                   # >>>print(Sauces())
                    {'name': 'Pesto', 'ingredients': ['olive oil', 'garlic', 'parmesan', 'basil', 'lemon'], 'weight': 50, 'price': 40}
                    {'name': 'Garlic', 'ingredients': ['butter', 'garlic', 'flour', 'oregano', 'milk', 'parmesan'], 'weight': 50, 'price': 35}
                    {'name': 'Classic', 'ingredients': ['tomato paste', 'oregano', 'garlic', 'paprika'], 'weight': 50, 'price': 25}
        """
        return '\n'.join(f'{i}' for i in self._products_data[self._string_name])


class Sauces(Products):
    """Class for creating sauces for pizza
        This class provides creating instance with information about sauces
    """
    def __init__(self, file_name='Sauces.json', string_name="Sauces"):
        """Constructor of the class Sauces
        :param file_name: name of the json file with data about dishes,
        by default `Sauces.json`
        :param string_name: name of the dictionary in json file,
        by default `Sauces`
        """
        super().__init__(file_name, string_name)
        self._string_name = string_name


class Supplements(Products):
    """Class for creating supplements for pizza
        This class provides creating instance
        with information about sauces
    """
    def __init__(self, file_name='Supplements.json', string_name="Supplements"):
        """Constructor of the class Sauces
        :param file_name: name of the json file with data about dishes,
        by default `Supplements.json`
        :param string_name: name of the dictionary in json file,
        by default `Supplements`
        """
        super().__init__(file_name, string_name)
        self._string_name = string_name


class Pizza:
    """Class for creating for creating pizza
    This class provides creating instance
    with information about the pizza that generates
    regardless of the current day
    """
    def __init__(self):
        """Constructor of the Pizza class"""
        self._today = datetime.today().strftime('%A')
        with open('Task_2.json') as file:
            pizza_database = json.load(file)
        date = self._today
        for i in pizza_database['Pizza']:
            if date == i['day']:
                self.__dict__ = i.copy()

    @property
    def get_info(self):
        """Getter of dishes info
        :return info about available dishes
        :rtype dict_items
        """
        return dict(itertools.islice(self.__dict__.items(), 4))

    def add_supplement(self, product):
        """Function for adding supplements to the pizza
        :argument product dictionary with info about chosen supplement
        """
        self.__dict__['ingredients'].append(product['name'])
        self.__dict__['weight'] += product['weight']
        self.__dict__['price'] += product['price']

    def __str__(self):
        """Return the string representation of the pizza of the day
               :return: String representation.
               :rtype: str
               **Example**:
               .. doctest::
                   # >>>print(Pizza())
                    name: Jugliano
                    ingredients: ['tomatoes', 'chicken fillet', 'cream', 'basil', 'bell pepper', 'feta']
                    weight: 470
                    price: 225
        """
        return str.join('\n', [f'{i}: {self.__dict__[i]}' for i in self.__dict__.keys() if i != 'day'])


class Order:
    """Class for creating order
    This class provides possibility of
    buying pizza of the day with supplements or no
    """
    def __init__(self):
        """Constructor of the class Order
        """
        self._order_id = uuid.uuid1()
        with open('Task_2.json') as file:
            self._pizza_menu = json.load(file)
        self._extra = None
        self._order = Pizza()

    @property
    def get_menu(self):
        """Getter of supplements info
        :return info about available supplements
        :rtype str
        """
        return '\n'.join([f'{i}' for i in self._extra._products_data[self._extra._string_name]])

    def change_pizza(self, product):
        """Function that is used for adding supplement or sauce to the pizza
        :raise ValueError when product name isn't available
        """
        if not any(product == i['name'] for i in self._extra._products_data[self._extra._string_name]):
            raise ValueError('invalid input')
        for i in self._extra._products_data[self._extra._string_name]:
            if product == i['name']:
                self._order.add_supplement(i)

    def add_to_order(self, type_):
        """Function that is used for choosing what to add:
        supplement or sauce
        :raise ValueError when name of the type of a dish isn't available
        """
        if type_ == "supplement":
            self._extra = Supplements()
        elif type_ == "sauce":
            self._extra = Sauces()
        else:
            raise ValueError('invalid input')

    def make_order(self):
        """Function that is used for adding info about
        ordered pizza, time of the ordering, total weight
        and price to the json file
        """
        with open('Order.json') as file:
            database = json.load(file)
        if "Data" not in database:
            database["Data"] = {}
        order_id = str(self._order_id)
        if not (order_id in database['Data']):
            info = self._order.get_info
            database["Data"][order_id] = {
                'name': info['name'],
                'weight': info['weight'],
                'price': info['price'],
                'purchase_date': str(datetime.now())
            }
            json.dump(database, open('Order.json', 'w'), indent=4)

    @property
    def get_order_info(self):
        """Getter of order's info
        :return info about order
        :rtype str
        **Example**:
            .. doctest::
                # >>>print(Order().get_order_info)
                Jugliano
                ingredients: tomatoes, chicken fillet, cream, basil, bell pepper, feta
                weight: 470 price: 225
        """
        info = self._order.get_info
        return f'{info["name"]}\ningredients: ' + ', '.join([f'{i}' for i in info["ingredients"]]) +\
               f'\nweight: {info["weight"]} price: {info["price"]}'

    def __str__(self):
        """Return the string representation of the pizza of the day
               :return: String representation.
               :rtype: str
               **Example**:
               .. doctest::
                   # >>>print(Order())
                    816b1343-4866-11ec-8dcd-5405dbc1cc23
                    name: Jugliano
                    ingredients: ['tomatoes', 'chicken fillet', 'cream', 'basil', 'bell pepper', 'feta']
                    weight: 470
                    price: 225
        """
        return f'{self._order_id}\n{self._order}'


your_order = Order()
print(your_order.get_order_info)
result = input("Do u wanna add any supplements to your pizza? yes/no\n")
if result == "yes":
    your_order.add_to_order(input('sauce/supplement\n'))
    print('what to add?')
    print(your_order.get_menu)
    your_order.change_pizza(input())
elif result != "no":
    raise IOError('invalid input')

your_order.make_order()
print(your_order)
print(Pizza())