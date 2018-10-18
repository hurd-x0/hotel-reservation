from cassandra.cluster import Cluster
import pymysql
from hotelreservation.dbexport import export_hotels, export_rooms
from hotelreservation.transform import merge_rooms_with_hotels
from hotelreservation.dbimport import import_hotels


def main():
    with Cluster(["172.17.0.1"], port=9042) as cluster:
        with cluster.connect("hotel_reservation") as session:
            hotels = export_hotels(session)
            rooms = export_rooms(session)
            hotels_with_rooms = merge_rooms_with_hotels(hotels, rooms)
            connection = pymysql.connect(host="172.17.0.1", port=3306, user="vld", password="Password1!",
                                         db="hotel_reservation")
            try:
                import_hotels(connection, hotels_with_rooms)
            finally:
                connection.close()


if __name__ == "__main__":
    main()
