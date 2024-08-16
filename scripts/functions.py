import json
from decimal import Decimal
from configuration import *

def load_json_file(path):
    """ Reads a specific json file """

    with open(path) as json_file:
        json_data = json.load(json_file)
    return json_data

def get_the_cheapest_price(json_string):
    """ Finds the cheapest price from given json (without using min function) """

    shown_price = json_string[ASSIGNMENT_RESULTS][0][SHOWN_PRICE]
    min_price = shown_price[next(iter(shown_price))]

    for price in shown_price:
        if Decimal(min_price) > Decimal(shown_price[price]):
            min_price = shown_price[price]

    return min_price

def get_number_of_guests(json_string):
    """ Returns the number of guests """
    # the number of guests does not depend on a price we give
    return json_string[ASSIGNMENT_RESULTS][0][NUMBER_OF_GUESTS]

def get_room_type_by_price(json_string, given_price):
    """ Returns room types by price based on the price """

    shown_price = json_string[ASSIGNMENT_RESULTS][0][SHOWN_PRICE]
    rooms = [] # there might be several rooms with the same price
    for room_type, price in shown_price.items():
        if price == given_price:
            rooms.append(room_type)

    return rooms

def get_total_tax(json_string):
    """ Evaluates total tax price """

    taxes = json_string[ASSIGNMENT_RESULTS][0][EXT_DATA][TAXES]  # a string that contains .json
    taxes = json.loads(taxes)  # convert into .json
    sum_of_taxes = 0
    for tax in taxes:
        sum_of_taxes += Decimal(taxes[tax])

    return sum_of_taxes

def get_total_price_for_each_room(json_string):
    """ Returns total price (including tax price) for each room """

    net_price = json_string[ASSIGNMENT_RESULTS][0][NET_PRICE]
    total_tax = get_total_tax(json_string)
    for price in net_price:
        net_price[price] = str(Decimal(net_price[price]) + total_tax)

    return net_price