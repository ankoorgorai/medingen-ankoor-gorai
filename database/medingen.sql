CREATE TABLE product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    description TEXT
);

INSERT INTO product (name, price, description) VALUES
('Tablet A', 10.0, 'Description of Tablet A'),
('Tablet B', 15.0, 'Description of Tablet B');
