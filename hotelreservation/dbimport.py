def import_hotels(connection, hotels_with_rooms):
    with connection.cursor() as cursor:
        for hotel_name, hotel_address, rooms in hotels_with_rooms:
            sql = """
                INSERT INTO hotel (hotel_name, hotel_address)
                VALUES (%(hotel_name)s, %(hotel_address)s)
            """
            cursor.execute(sql, {"hotel_name": hotel_name, "hotel_address": hotel_address})
            connection.commit()
    # for hotel_name, hotel_address, rooms in hotels_with_rooms:
    #     print("Hotel:", hotel_name, hotel_address)
    #     for _, room_number, room_description in rooms:
    #         print("Room:", room_number, room_description)
