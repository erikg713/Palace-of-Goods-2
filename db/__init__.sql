CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    description TEXT,
    price FLOAT NOT NULL
);
