from functions import *
from configuration import *

json_string = load_json_file(JSON_FILENAME)

cheapest_price = get_the_cheapest_price(json_string)
number_of_guests = get_number_of_guests(json_string)
room_type = get_room_type_by_price(json_string, cheapest_price)
total_price_for_each_room = get_total_price_for_each_room(json_string)

print("The cheapest price:", cheapest_price)
print("Number of guests for the cheapest price:", number_of_guests)
print("Room type for the cheapest price:", room_type)
print("Total price for each room:", total_price_for_each_room)

json_object = json.dumps({"cheapest_price": [cheapest_price,
                                             {"number_of_guests": number_of_guests,
                                              "room_type": room_type}],
                         "total_price": total_price_for_each_room}
                         )
with open("../json/output.json", "w") as outfile:
    outfile.write(json_object)