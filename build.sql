
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    firstname TEXT,
    lastname TEXT,
    email TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    passhash TEXT UNIQUE NOT NULL,
    created DATE DEFAULT (datetime('now','localtime'))
);

