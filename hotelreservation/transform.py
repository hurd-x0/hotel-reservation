def merge_rooms_with_hotels(rooms, hotels):
    rooms_with_hotels = rooms.merge(hotels, on="hotel_name")
    return rooms_with_hotels
