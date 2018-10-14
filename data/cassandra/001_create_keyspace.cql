CREATE KEYSPACE IF NOT EXISTS hotel_reservation
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
