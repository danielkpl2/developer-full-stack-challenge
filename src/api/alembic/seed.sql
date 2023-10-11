INSERT INTO author (id, name) VALUES
    (1, 'Author 1'),
    (2, 'Author 2'),
    (3, 'Author 3'),
    (4, 'Author 4'),
    (5, 'Author 5'),
    (6, 'Author 6'),
    (7, 'Author 7'),
    (8, 'Author 8'),
    (9, 'Author 9'),
    (10, 'Author 10'),
    (11, 'Author 11'),
    (12, 'Author 12'),
    (13, 'Author 13'),
    (14, 'Author 14'),
    (15, 'Author 15'),
    (16, 'Author 16'),
    (17, 'Author 17'),
    (18, 'Author 18'),
    (19, 'Author 19'),
    (20, 'Author 20');

SELECT setval('author_id_seq', 21, false);

INSERT INTO book (id, name, number_pages, author_id) VALUES
    (1, 'Book A1', 200, 1),
    (2, 'Book A2', 250, 1),
    (3, 'Book A3', 300, 1);

INSERT INTO book (id, name, number_pages, author_id) VALUES
    (4, 'Book B1', 180, 2),
    (5, 'Book B2', 220, 2);

INSERT INTO book (id, name, number_pages, author_id) VALUES
    (6, 'Book C1', 280, 3);

INSERT INTO book (id, name, number_pages, author_id) VALUES
    (7, 'Book D1', 150, 4),
    (8, 'Book D2', 270, 4),
    (9, 'Book D3', 320, 4),
    (10, 'Book D4', 200, 4);

INSERT INTO book (id, name, number_pages, author_id) VALUES
    (11, 'Book E1', 230, 5),
    (12, 'Book E2', 260, 5);

INSERT INTO book (id, name, number_pages, author_id) VALUES
    (13, 'Book F1', 190, 6);

INSERT INTO book (id, name, number_pages, author_id) VALUES
    (14, 'Book G1', 310, 7);

INSERT INTO book (id, name, number_pages, author_id) VALUES
    (15, 'Book H1', 180, 8);

INSERT INTO book (id, name, number_pages, author_id) VALUES
    (16, 'Book I1', 240, 9);

INSERT INTO book (id, name, number_pages, author_id) VALUES
    (17, 'Book J1', 280, 10),
    (18, 'Book J2', 320, 10),
    (19, 'Book J3', 260, 10);


INSERT INTO book (id, name, number_pages, author_id) VALUES
    (20, 'Book K1', 200, 11),
    (21, 'Book K2', 250, 11),
    (22, 'Book K3', 300, 11);

INSERT INTO book (id, name, number_pages, author_id) VALUES
    (23, 'Book L1', 180, 12),
    (24, 'Book L2', 220, 12);

INSERT INTO book (id, name, number_pages, author_id) VALUES
    (25, 'Book M1', 280, 13);

INSERT INTO book (id, name, number_pages, author_id) VALUES
    (26, 'Book N1', 150, 14),
    (27, 'Book N2', 270, 14),
    (28, 'Book N3', 320, 14),
    (29, 'Book N4', 200, 14);

INSERT INTO book (id, name, number_pages, author_id) VALUES
    (30, 'Book O1', 230, 15),
    (31, 'Book O2', 260, 15);

INSERT INTO book (id, name, number_pages, author_id) VALUES
    (32, 'Book P1', 190, 16);

INSERT INTO book (id, name, number_pages, author_id) VALUES
    (33, 'Book Q1', 310, 17);

INSERT INTO book (id, name, number_pages, author_id) VALUES
    (34, 'Book R1', 180, 18);

INSERT INTO book (id, name, number_pages, author_id) VALUES
    (35, 'Book S1', 240, 19);

INSERT INTO book (id, name, number_pages, author_id) VALUES
    (36, 'Book T1', 280, 20),
    (37, 'Book T2', 320, 20),
    (38, 'Book T3', 260, 20);

SELECT setval('book_id_seq', 39, false);

INSERT INTO dcuser (id, username, password) VALUES 
    (1, 'user1', '$2b$12$iFGW/xuxs.KQIMrnHCaCwONbLBcHbvQzim8bqXvliDx4LiKsYhqZK'),
    (2, 'user2', '$2b$12$WJxqMocIPNknqrffMCxAT.2QaT2HROFVqyBd2R.FIqjGOaeI2Ceqa');

SELECT setval('dcuser_id_seq', 3, false);
