from hotelreservation.dbexport import export_hotels, export_rooms
from hotelreservation.transform import merge_rooms_with_hotels
from hotelreservation.dbimport import import_hotels


def main():
    hotels = export_hotels()
    # print(hotels)
    rooms = export_rooms()
    # print(rooms)
    hotels = import_hotels(hotels)
    print(hotels)


if __name__ == "__main__":
    main()
