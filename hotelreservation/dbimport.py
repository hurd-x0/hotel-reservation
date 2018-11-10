from functools import wraps
from pymysql import connect
from pymysql.cursors import DictCursor


MARIADB_HOST="172.17.0.1"
MARIADB_PORT=3306
MARIADB_USER="vld"
MARIADB_PASSWORD="Password1!"
MARIADB_DATABASE="hotel_reservation"


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


@with_mariadb_connection
def import_hotels(connection, hotels):
    with connection.cursor() as cursor:
        sql = """INSERT INTO hotel (hotel_name, hotel_address) VALUES (%(hotel_name)s, %(hotel_address)s)"""
        for hotel in hotels:
            cursor.execute(sql, hotel)
            hotel["hotel_id"] = cursor.lastrowid
    connection.commit()
    return hotels
