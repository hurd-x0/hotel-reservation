from functools import wraps
from cassandra.cluster import Cluster
from cassandra.query import dict_factory


CASSANDRA_NODE="172.17.0.1"
CASSANDRA_PORT=9042
CASSANDRA_KEYSPACE="hotel_reservation"


def with_cassandra_session(execute_statement):
    @wraps(execute_statement)
    def create_session(*args, **kwargs):
        with Cluster([CASSANDRA_NODE], port=CASSANDRA_PORT) as cluster:
            with cluster.connect(CASSANDRA_KEYSPACE) as session:
                session.row_factory = dict_factory
                return execute_statement(session, *args, **kwargs)
    return create_session


@with_cassandra_session
def export_hotels(session):
    cql = """SELECT hotel_name, hotel_address FROM hotel"""
    hotels = session.execute(cql)
    hotels = [dict(hotel) for hotel in hotels]
    return hotels


@with_cassandra_session
def export_rooms(session):
    cql = """SELECT hotel_name, room_number, room_description FROM room_by_hotel"""
    rooms = session.execute(cql)
    rooms = [dict(room) for room in rooms]
    return rooms
