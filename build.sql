
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    firstname TEXT,
    lastname TEXT,
    email TEXT,
    username TEXT UNIQUE NOT NULL,
    passhash TEXT UNIQUE NOT NULL,
    created DATE DEFAULT (datetime('now','localtime'))
);

