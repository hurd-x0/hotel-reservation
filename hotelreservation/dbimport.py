def import_hotels(connection, hotels_with_rooms):
    for hotel_name, hotel_address, rooms in hotels_with_rooms:
        print("Hotel:", hotel_name, hotel_address)
        for _, room_number, room_description in rooms:
            print("Room:", room_number, room_description)
