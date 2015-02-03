
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    firstname TEXT,
    lastname TEXT,
    email TEXT,
    username TEXT UNIQUE NOT NULL,
    passhash TEXT UNIQUE NOT NULL,
    created DATE DEFAULT (datetime('now','localtime'))
);

CREATE TABLE posts (
    id INTEGER PRIMARY KEY,
    userid INTEGER NOT NULL,
    title TEXT,
    message TEXT,
    created DATE DEFAULT (datetime('now','localtime')),
    FOREIGN KEY(userid) REFERENCES users(id)
);

