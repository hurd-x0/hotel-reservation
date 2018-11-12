from functools import wraps, partial
from pymysql import connect
from pymysql.cursors import DictCursor


MARIADB_HOST = "172.17.0.1"
MARIADB_PORT = 3306
MARIADB_USER = "vld"
MARIADB_PASSWORD = "Password1!"
MARIADB_DATABASE = "hotel_reservation"


def with_mariadb_connection(execute_statement):
    @wraps(execute_statement)
    def create_connection(*args, **kwargs):
        mariadb_config = {
            "host": MARIADB_HOST,
            "port": MARIADB_PORT,
            "user": MARIADB_USER,
            "password": MARIADB_PASSWORD,
            "db": MARIADB_DATABASE,
            "cursorclass": DictCursor
        }
        connection = connect(**mariadb_config)
        try:
            return execute_statement(connection, *args, **kwargs)
        finally:
            connection.close()
    return create_connection


def save_item(cursor, sql, item):
    cursor.execute(sql, dict(item))
    return cursor.lastrowid


@with_mariadb_connection
def import_hotels(connection, hotels):
    with connection.cursor() as cursor:
        sql = """
            INSERT INTO hotel (hotel_name, hotel_address)
            VALUES (%(hotel_name)s, %(hotel_address)s)
        """
        save_hotel = partial(save_item, cursor, sql)
        hotels["hotel_id"] = hotels.apply(save_hotel, axis=1)
    connection.commit()
    return hotels


@with_mariadb_connection
def import_rooms(connection, rooms):
    with connection.cursor() as cursor:
        sql = """
            INSERT INTO room (hotel_id, room_number, room_description)
            VALUES (%(hotel_id)s, %(room_number)s, %(room_description)s)
        """
        save_room = partial(save_item, cursor, sql)
        rooms["room_id"] = rooms.apply(save_room, axis=1)
    connection.commit()
    return rooms
