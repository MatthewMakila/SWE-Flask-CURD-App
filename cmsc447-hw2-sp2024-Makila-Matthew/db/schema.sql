DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_name TEXT NOT NULL,
    id INTEGER PRIMARY KEY,
    points INTEGER NOT NULL
);