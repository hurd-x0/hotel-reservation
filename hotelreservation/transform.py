from collections import namedtuple
import operator
import itertools


Hotel = namedtuple("Hotel", "hotel_name hotel_address rooms")


def merge_rooms_with_hotels(hotels, rooms):
    rooms_by_hotel = {}
    for hotel_name, hotel_rooms in itertools.groupby(rooms, operator.attrgetter('hotel_name')):
        rooms_by_hotel[hotel_name] = list(hotel_rooms)
    hotels_with_rooms = (Hotel(hotel_name=hotel_name, hotel_address=hotel_address, rooms=rooms_by_hotel[hotel_name])
                         for hotel_name, hotel_address in hotels)
    return hotels_with_rooms
