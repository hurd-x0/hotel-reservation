DROP TABLE IF EXISTS room_by_hotel;
DROP TABLE IF EXISTS hotel;

CREATE TABLE hotel (
    hotel_name TEXT,
    hotel_address TEXT,
    PRIMARY KEY ((hotel_name))
);

CREATE TABLE room_by_hotel (
    hotel_name TEXT,
    room_number TEXT,
    room_description TEXT,
    PRIMARY KEY ((hotel_name), room_number)
);
