from functools import wraps
from cassandra.cluster import Cluster
from cassandra.query import dict_factory
import pandas as pd


CASSANDRA_NODE = "172.17.0.1"
CASSANDRA_PORT = 9042
CASSANDRA_KEYSPACE = "hotel_reservation"


def with_cassandra_session(execute_statement):
    @wraps(execute_statement)
    def create_session(*args, **kwargs):
        with Cluster([CASSANDRA_NODE], port=CASSANDRA_PORT) as cluster:
            with cluster.connect(CASSANDRA_KEYSPACE) as session:
                session.row_factory = dict_factory
                return execute_statement(session, *args, **kwargs)
    return create_session


def read_items(session, cql):
    items = session.execute(cql)
    items = [dict(item) for item in items]
    items = pd.DataFrame(items)
    return items


@with_cassandra_session
def export_hotels(session):
    cql = """SELECT hotel_name, hotel_address FROM hotel"""
    hotels = read_items(session, cql)
    return hotels


@with_cassandra_session
def export_rooms(session):
    cql = """SELECT hotel_name, room_number, room_description FROM room_by_hotel"""
    rooms = read_items(session, cql)
    return rooms
