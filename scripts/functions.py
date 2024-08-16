import json
from decimal import Decimal

def load_json_file(path):
    with open(path) as json_file:
        json_data = json.load(json_file)
    return json_data

def get_the_cheapest_price(json_string):
    shown_price = json_string['assignment_results'][0]['shown_price']
    min_price = shown_price[next(iter(shown_price))]

    # an implementation how to find min without using min()
    for price in shown_price:
        if Decimal(min_price) > Decimal(shown_price[price]):
            min_price = shown_price[price]

    return min_price

def get_number_of_guests(json_string):
    # the number of guests does not depend on a price we give
    return json_string['assignment_results'][0]['number_of_guests']

def get_room_type_by_price(json_string, given_price):
    shown_price = json_string['assignment_results'][0]['shown_price']
    rooms = [] # there might be several rooms with the same price
    for room_type, price in shown_price.items():
        if price == given_price:
            rooms.append(room_type)

    return rooms

def get_total_tax(json_string):
    taxes = json_string['assignment_results'][0]['ext_data']['taxes']  # a string that contains .json
    taxes = json.loads(taxes)  # convert into .json
    sum_of_taxes = 0
    for tax in taxes:
        sum_of_taxes += Decimal(taxes[tax])

    return sum_of_taxes

def get_total_price_for_each_room(json_string):
    net_price = json_string['assignment_results'][0]['net_price']
    total_tax = get_total_tax(json_string)
    for price in net_price:
        net_price[price] = str(Decimal(net_price[price]) + total_tax)

    return net_price