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

from datetime import datetime, date
import uuid
import json

"""Constants that means price of tickets with discount"""
ADVANCE_TICKET_PRICE = 0.6
STUDENT_TICKET_PRICE = 0.5
LATE_TICKET_PRICE = 0.9


class Ticket:
    """Class for creating tickets
        This class provides creating instance with information about a ticket
    """
    def __init__(self, price):
        """Constructor of the class Ticket
        :param price: price of the standard tickets for the chosen event
        """
        self._price = price
        self._id = uuid.uuid1()

    @property
    def get_ticket_price(self):
        """Getter of ticket price
        :return ticket price
        :rtype int
        """
        return self._price

    @property
    def get_ticket_info(self):
        """Getter of ticket information
        :return ticket price and id
        :rtype int, uuid
        """
        return self._price, self._id

    def __str__(self):
        """Return the string representation of the current ticket
               :return: String representation.
               :rtype: str
               **Example**:
               .. doctest::
                   # >>>print(Ticket())
                   Price: 345$
                   Ticket id: 3fb3234c-4478-11ec-b1c9-5405dbc1cc23
        """
        return f'Price: {self._price}$\nTicket id: {self._id}\n'


class AdvanceTicket(Ticket):
    """Class for creating advance tickets,
    that could be sold at least in 60 days before the event start
    This class provides creating instance of a ticket
    with discount 40% of the regular ticket price
    """
    def __init__(self, price_):
        """Constructor of the class AdvanceTicket
        :param price_: price of the standard tickets for the chosen event
        """
        super.__init__(price_)
        self._price = round(self._price * ADVANCE_TICKET_PRICE)


class StudentTicket(Ticket):
    """Class for creating tickets for students,
    that could be sold any time before the event start
    This class provides creating instance of a ticket
    with discount 50% of the regular ticket price
    """
    def __init__(self, price_):
        """Constructor of the class StudentTicket
        :param price_: price of the standard tickets for the chosen event
        """
        super.__init__(price_)
        self._price = round(self._price * STUDENT_TICKET_PRICE)


class LateTicket(Ticket):
    """Class for creating tickets for students,
    that could be sold less than 10 days before the event start
    This class provides creating instance of a ticket
    with discount 10% of the regular ticket price
    """
    def __init__(self, price_):
        """Constructor of the class LateTicket
        :param price_: price of the standard tickets for the chosen event
        """
        super.__init__(price_)
        self._price = round(self._price * LATE_TICKET_PRICE)


class TicketService:
    """Class for creating tickets
    This class provides possibility of
    buying tickets for the one of the available event
    """
    def __init__(self):
        self._event_chosen = None
        self._ticket = None

    def choose_event(self):
        """Function is used for choosing event and decreasing tickets amount when
        the correct event is chosen, than rewriting event information in json file
        with the correct tickets amount
                :raise ValueError when event input by user extinct in the json file
                or there are not available tickets for the event, tickets amount <= 0
        """
        with open('Task_1.json') as file:
            events_data = json.load(file)
        choice = input('Input event name\n')
        if not any(x['name'] == choice for x in events_data['Events']):
            raise ValueError('invalid input')
        for i in events_data['Events']:
            if choice == i['name']:
                if i['tickets'] <= 0:
                    raise ValueError('tickets sold')
                i['tickets'] -= 1
                json.dump(events_data, open('Task_1.json', 'w'), indent=4)
                self._event_chosen = i.copy()

    @staticmethod
    def getting_date_difference(event_date):
        """Function is used for getting difference with the current date and the event start date
                :type: staticmethod
                :param event_date
                :return difference with the dates
                :rtype: int
                :raise TimeoutError when current date is bigger than the event date
        """
        data = datetime.now()
        current_date = (data.year, data.month, data.day)
        event_date = tuple(int(i) for i in reversed(event_date.split('.')))
        if current_date > event_date:
            raise TimeoutError('event ended')
        return (date(data.year, data.month, data.day) - date(event_date[0], event_date[1], event_date[2])).days

    def make_order(self):
        """The most important function of the class, it is used for making order.
        There is caring out the user's request for the ticket type:
        'advanced', 'student', 'standard' or 'late';
        checking the input for the correction and creating
        instance of one of the class responsible for ticket creation according
        to the chosen ticket type. When ticket is `bought` the information about
        is written to the json file in the form of the dictioany with the ticket id as its name
                :raise TimeoutError when chosen ticket type is `advance`
                and there left less than 60 days before the event start
                :raise TimeoutError when chosen ticket type is `late`
                and there is more than 9 days before the event start
        """
        ticket_type = input('\nEnter ticket type: advanced/student/standard/late\n')
        days_difference = abs(TicketService.getting_date_difference(self._event_chosen['date']))

        if not (ticket_type in ('advanced', 'student', 'standard', 'late')):
            TicketService.make_order(self)
        if ticket_type == 'advanced':
            if days_difference >= 60:
                self._ticket = AdvanceTicket(int(self._event_chosen['price']))
            else:
                raise TimeoutError('advance tickets is`nt available')
        elif ticket_type == 'student':
            # check student card's code xxxx xxxx xxxx
            self._ticket = StudentTicket(self._event_chosen['price'])
        elif ticket_type == 'standard':
            self._ticket = Ticket(self._event_chosen['price'])
        elif ticket_type == 'late':
            if 0 <= days_difference < 10:
                self._ticket = LateTicket(self._event_chosen['price'])
            else:
                # print(f'late tickets will be available in {days_difference - 10}')
                raise TimeoutError('advance tickets is`nt available')

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
        """Function is used for searching the ticket by its id
        :type: staticmethod
        :param ticket_id
        :return: string representation
        :rtype: str
        :raise: KeyError, TypeError, ValueError, when there isn`t dictionary in json file or
        ticket_id wasn`t given or if ticket with the ticket_id is extinct in the file
        **Example**:
               .. doctest::
                   # >>>print(TicketService())
                   Ticket 92171a4c-4241-11ec-bf51-5405dbc1cc23 info:
                   event: Azerbaijan iGaming Affiliate Conference
                   place: Baku
                   time: 1.12.2021 12:00
                   ticket_type: standard
                   price: 4000
                   purchase_date: 2021-11-10 18:16:33.297780
        """
        with open('Tickets_data.json') as file:
            database = json.load(file)
        if 'Data' not in database:
            raise KeyError('There is no events in database')
        if not ticket_id or not isinstance(ticket_id, str):
            raise TypeError('Ticket id extinct')
        if ticket_id not in database['Data']:
            raise ValueError('Ticket extinct')
        return f'Ticket {ticket_id} info:\n' + \
               '\n'.join([f'{i}: {database["Data"][ticket_id][i]}' for i in database['Data'][ticket_id]])

    @property
    def get_events(self):
        """Getter for the available events
               :return: String representation
               :rtype: str
               **Example**:
               .. doctest::
                   # >>>print(TicketService())
                              SMM Day 2021
                        Place: Online
                        Date: 28.1.2022 Time: 10:00
                        Price: 450

                            AWS Tech Conference
                        Place: Online
                        Date: 19.12.2021 Time: 10:00
                        Price: 500

                            Azerbaijan iGaming Affiliate Conference
                        Place: Baku
                        Date: 1.12.2021 Time: 12:00
                        Price: 4000

                            Head of Digital Day
                        Place: Online
                        Date: 25.11.2021 Time: 10:00
                        Price: 700
        """
        events_data = json.load(open('Task_1.json'))
        return '\n'.join([f'           {event["name"]}\nPlace: {event["place"]}\nDate: {event["date"]} '
                          f'Time: {event["time"]}\nPrice: {event["price"]}\n' for event in events_data['Events']])

    @property
    def get_price(self):
        """Getter for the available events
               :return: Integer representation
               :rtype: int
               **Example**:
               .. doctest::
                   # >>>print(TicketObject.get_price)
                   700
        """
        return self._ticket.get_ticket_price

    def __str__(self):
        """Return the string representation of the current ticket
               :return: String representation.
               :rtype: str
               **Example**:
               .. doctest::
                   # >>>print(TicketService())
                   Head of Digital Day
                   Place: Online	Date: 25.11.2021	10:00
                   Ticket:
                   Price: 700$
                   Ticket id: 4ae439e5-447a-11ec-941c-5405dbc1cc23
        """
        return f'{self._event_chosen["name"]}\nPlace: {self._event_chosen["place"]}\t' \
               f'Date: {self._event_chosen["date"]}\t' \
               f'{self._event_chosen["time"]}\nTicket:\n{self._ticket}\n'


TicketObject = TicketService()
print(TicketObject.get_events)
TicketObject.choose_event()
TicketObject.make_order()
print(TicketObject)
print(TicketObject.search_ticket('92171a4c-4241-11ec-bf51-5405dbc1cc23'))

