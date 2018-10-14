from cassandra.cluster import Cluster


def export_hotels(session):
    hotels = session.execute("""SELECT * FROM hotel""")
    return hotels


def export_rooms(session):
    rooms = session.execute("""SELECT * FROM room_by_hotel""")
    return rooms
