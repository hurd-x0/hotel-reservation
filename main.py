from cassandra.cluster import Cluster
from hotelreservation.export import export_hotels, export_rooms
from hotelreservation.transform import merge_rooms_with_hotels


def main():
    with Cluster(["172.17.0.1"], port=9042) as cluster:
        with cluster.connect("hotel_reservation") as session:
            hotels = export_hotels(session)
            rooms = export_rooms(session)
            hotels_with_rooms = merge_rooms_with_hotels(hotels, rooms)


if __name__ == "__main__":
    main()
