-- Insert 10 authors
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
    (10, 'Author 10');

-- Insert books for each author
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

INSERT INTO dcuser (id, username, password) VALUES 
    (1, 'user1', '$2b$12$iFGW/xuxs.KQIMrnHCaCwONbLBcHbvQzim8bqXvliDx4LiKsYhqZK'),
    (2, 'user2', '$2b$12$WJxqMocIPNknqrffMCxAT.2QaT2HROFVqyBd2R.FIqjGOaeI2Ceqa');