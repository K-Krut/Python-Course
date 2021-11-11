"""

Task 1.
Write a program for selling tickets to IT-events.
Each ticket has a unique number and a price.
There are four types of tickets: regular ticket, advance ticket
(purchased  60 or more days before the event),
late ticket (purchased fewer than 10 days before the event) and student ticket.


Additional information:
-advance ticket - discount 40% of the regular ticket price;
-student ticket - discount 50% of the regular ticket price;
-late ticket - additional 10% to the regular ticket price.

All tickets must have the following properties:
-the ability to construct a ticket by number;
-the ability to ask for a ticket’s price;
-the ability to print a ticket as a String.

"""

# дата время
# сколько может попасть
# стоимость и когда начинаеться продажа лейт
#
# сериализация и десериализация
# дампы памяти
# разные классы билетов

from datetime import datetime, date
import uuid
import json


class Ticket:
    def __init__(self, price):
        self._price = price
        self._id = uuid.uuid1()

    @property
    def get_ticket_price(self):
        return self._price

    @property
    def get_ticket_info(self):
        return self._price, self._id

    def __str__(self):
        return f'Price: {self._price}$\nTicket id: {self._id}\n'


class AdvanceTicket(Ticket):
    def __init__(self, price_):
        super(price_)
        self._price = round(self._price * 0.6)


class StudentTicket(Ticket):
    def __init__(self, price_):
        super(price_)
        self._price = round(self._price * 0.5)


class LateTicket(Ticket):
    def __init__(self, price_):
        super(price_)
        self._price = round(self._price * 0.9)

# ttmap = {
#     'advanced': AdvanceTicket,
#     'student': StudentTicket,
#     'standard': Ticket
# }
#


class TicketService:
    def __init__(self):
        self._event_chosen = None
        self._ticket = None

    def choose_event(self):
        with open('Task_1.json') as file:
            events_data = json.load(file)
        choice = input('Input event name\n')
        print(events_data['Events'][2])
        for i in events_data['Events']:
            if choice == i['name']:
                if i['tickets'] <= 0:
                    print('tickets sold')
                i['tickets'] -= 1
                json.dump(events_data, open('Task_1.json', 'w'), indent=4)
                self._event_chosen = i.copy()
            else:
                raise ValueError('invalid input')

    @staticmethod
    def getting_date_difference(event_date):
        data = datetime.now()
        current_date = (data.year, data.month, data.day)
        event_date = tuple(int(i) for i in reversed(event_date.split('.')))
        if current_date > event_date:
            raise TimeoutError('event ended')
        return (date(data.year, data.month, data.day) - date(event_date[0], event_date[1], event_date[2])).days

    def make_order(self):
        ticket_type = input('\nEnter ticket type: advanced/student/standard/late\n')
        days_difference = abs(TicketService.getting_date_difference(self._event_chosen['date']))

        if not (ticket_type in ('advanced', 'student', 'standard', 'late')):
            raise ValueError('invalid type input')
        if ticket_type == 'advanced':
            if days_difference >= 60:
                self._ticket = AdvanceTicket(int(self._event_chosen['price']))
            else:
                print('advance tickets is`nt available')
                TicketService.make_order(self)
        elif ticket_type == 'student':
            # check student card's code xxxx xxxx xxxx

            self._ticket = StudentTicket(self._event_chosen['price'])
        elif ticket_type == 'standard':
            self._ticket = Ticket(self._event_chosen['price'])
        elif ticket_type == 'late':
            if 0 <= days_difference < 10:
                self._ticket = LateTicket(self._event_chosen['price'])
            else:
                print(f'late tickets will be available in {days_difference - 10}')
                TicketService.make_order(self)

        with open('Tickets_data.json') as file:
            database = json.load(file)
        if "Data" not in database:
            database["Data"] = {}
        ticket_id = str(self._ticket.get_ticket_info[1])
        if not (ticket_id in database['Data']):
            database['Data'][ticket_id] = {
                'event': self._event_chosen['name'],
                'place': self._event_chosen['place'],
                'time': self._event_chosen['date'] + ' ' + self._event_chosen['time'],
                'ticket_type': ticket_type,
                'price': self._ticket.get_ticket_price,
                'purchase_date': str(datetime.now())
            }
            json.dump(database, open('Tickets_data.json', 'w'), indent=4)

    @staticmethod
    def search_ticket(ticket_id):
        with open('Tickets_data.json') as file:
            database = json.load(file)
        if 'Data' not in database:
            raise KeyError('There is no events in database')
        if not ticket_id or not isinstance(ticket_id, str):
            raise TypeError('Ticket id extinct')
        if ticket_id not in database['Data']:
            raise KeyError('Ticket extinct')
        # return '\n'.join(f'{}')
        return f'Ticket {ticket_id} info:\n' + '\n'.join([f'{i}: {database["Data"][ticket_id][i]}' for i in database['Data'][ticket_id]])

    @property
    def get_events(self):
        events_data = json.load(open('Task_1.json'))
        return '\n'.join([f'           {event["name"]}\nPlace: {event["place"]}\nDate: {event["date"]} '
                          f'Time: {event["time"]}\nPrice: {event["price"]}\n' for event in events_data['Events']])

    @property
    def get_price(self):
        return self._ticket.get_ticket_price

    def __str__(self):
        return f'{self._event_chosen["name"]}\nPlace: {self._event_chosen["place"]}\tDate: {self._event_chosen["date"]}\t' \
               f'{self._event_chosen["time"]}\nTicket:\n{self._ticket}\n'


A = TicketService()
print(A.get_events)
A.choose_event()
A.make_order()
print(A)
print(A.search_ticket('92171a4c-4241-11ec-bf51-5405dbc1cc23'))
