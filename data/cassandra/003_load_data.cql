-- hotel
INSERT INTO hotel (hotel_name, hotel_address)
VALUES ('NH Hotels', 'NH Address');
INSERT INTO hotel (hotel_name, hotel_address)
VALUES ('AC Hotels', 'AC Address');

-- room_by_hotel
INSERT INTO room_by_hotel (hotel_name, room_number, room_description)
VALUES ('NH Hotels', 'NH-R1', 'Standard');
INSERT INTO room_by_hotel (hotel_name, room_number, room_description)
VALUES ('NH Hotels', 'NH-R2', 'Luxury');
INSERT INTO room_by_hotel (hotel_name, room_number, room_description)
VALUES ('AC Hotels', 'AC-R1', 'Standard');
