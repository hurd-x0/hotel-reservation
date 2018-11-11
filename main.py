from hotelreservation.dbexport import export_hotels, export_rooms
from hotelreservation.transform import merge_rooms_with_hotels
from hotelreservation.dbimport import import_hotels, import_rooms


def main():
    exported_hotels = export_hotels()
    imported_hotels = import_hotels(exported_hotels)
    exported_rooms_by_hotel = export_rooms()
    merged_rooms_with_hotels = merge_rooms_with_hotels(exported_rooms_by_hotel, imported_hotels)
    imported_rooms = import_rooms(merged_rooms_with_hotels)
    print(imported_rooms)


if __name__ == "__main__":
    main()
