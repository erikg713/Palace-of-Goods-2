-- Insert sample products
INSERT INTO product (name, description, price) VALUES
('Laptop', 'High-performance laptop', 1200.99),
('Phone', 'Latest smartphone', 799.49),
('Headphones', 'Noise-cancelling headphones', 199.99),
('Monitor', '4K UHD Monitor', 329.99);

-- Insert sample users
INSERT INTO "user" (username, email, password_hash, is_admin) VALUES
('admin', 'admin@example.com', '$2b$12$3omNkwqO1khF/PbLZax.oOAcx7lPQgAPc67Q7GiKh4hpEGHzSR1Rm', TRUE), -- Password: admin123
('johndoe', 'johndoe@example.com', '$2b$12$w4OAVC2uHb1lfAXv6PuzbeHz32zRb.NsRsmldlwO7cNkH1g0lOJwe', FALSE); -- Password: johndoe123
