DROP TABLE IF EXISTS room;
DROP TABLE IF EXISTS hotel;

CREATE TABLE hotel (
    hotel_id BIGINT NOT NULL AUTO_INCREMENT,
    hotel_name TEXT NOT NULL,
    hotel_address TEXT NOT NULL,
    PRIMARY KEY (hotel_id)
);

CREATE TABLE room (
    room_id BIGINT NOT NULL AUTO_INCREMENT,
    hotel_id BIGINT NOT NULL,
    room_number TEXT NOT NULL,
    room_description TEXT NOT NULL,
    PRIMARY KEY (room_id),
    FOREIGN KEY (hotel_id) REFERENCES hotel(hotel_id)
);
