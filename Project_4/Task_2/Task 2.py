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


class Pizza:
    def __init__(self):
        self._today = datetime.today().strftime('%A')
        with open('Task_2.json') as file:
            pizza_database = json.load(file)
        date = self._today
        for i in pizza_database['Pizza']:
            if date == i['day']:
                self.__dict__ = i.copy()

    @property
    def get_pizza_info(self):
        return dict(itertools.islice(self.__dict__.items(), 4))
    # return self.__dict__

    def add_supplement(self, product):
        self.__dict__['ingredients'].append(product['name'])
        self.__dict__['weight'] += product['weight']
        self.__dict__['price'] += product['price']

    def __str__(self):
        return str.join('\n', [f'{i}: {self.__dict__[i]}' for i in self.__dict__.keys() if i != 'day'])


class Order:
    def __init__(self):
        self._order_id = uuid.uuid1()
        with open('Task_2.json') as file:
            self._pizza_menu = json.load(file)
        with open('Supplements.json') as file:
            self._supplements = json.load(file)
        self._order = Pizza()

    @property
    def get_menu(self):
        return '\n'.join([f'{i}' for i in self._supplements['Supplements']])
        # return f"Pizza:" + "\n".join([f'{i}' for i in self._pizza_menu]) + \
        #        "\n".join([f'{j}' for j in self._supplements])

    def change_pizza(self):
        # while
        product = input('what to add?\n')
        if any(product == i['name'] for i in self._supplements['Supplements']):
            for i in self._supplements['Supplements']:
                if product == i['name']:
                    self._order.add_supplement(i)
        else:
            raise ValueError('invalid input')

    def make_order(self):
        with open('Order.json') as file:
            database = json.load(file)
        if "Data" not in database:
            database["Data"] = {}
        order_id = str(self._order_id)
        if not (order_id in database['Data']):
            info = self._order.get_pizza_info
            database["Data"][order_id] = {
                'name': info['name'],
                'weight': info['weight'],
                'price': info['price'],
                'purchase_date': str(datetime.now())
            }
            json.dump(database, open('Order.json', 'w'), indent=4)

    @property
    def get_order_info(self):
        info = self._order.get_pizza_info
        return f'{info["name"]}\ningredients: ' + ', '.join([f'{i}' for i in info["ingredients"]]) +\
               f'\nweight: {info["weight"]} price: {info["price"]}'

    def __str__(self):
        return f'{self._order_id}\n{self._order}'


your_order = Order()
print(your_order.get_order_info)
result = input("Do u wanna add any supplements to your pizza? yes/no\n")
if result == "yes":
    print(your_order.get_menu)
    your_order.change_pizza()
elif result != "no":
    raise IOError('invalid input')

your_order.make_order()
print(your_order)









# @property
# def pizza_price(self):
#     return self.__dict__['price']
#
# @pizza_price.setter
# def pizza_price(self, price_):
#     self.__dict__['price'] = price_
#
# @property
# def pizza_weight(self):
#     return self.__dict__['weight']
#
# @pizza_weight.setter
# def pizza_weight(self, weight_):
#     self.__dict__['weight'] = weight_
#
# @property
# def pizza_ingredients(self):
#     return self.__dict__['ingredients']
#
# @pizza_ingredients.setter
# def pizza_ingredients(self):
#     pass