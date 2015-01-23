
CREATE TABLE users (
    id INTEGER PRIMARY KEY NOT NULL,
    firstname TEXT,
    lastname TEXT,
    email TEXT UNIQUE NOT NULL,
    username TEXT UNIQUE NOT NULL,
    passhash TEXT UNIQUE NOT NULL,
    created DATE DEFAULT (datetime('now','localtime'))
);

CREATE TABLE user_songs (
song_id INTEGER NOT NULL,
user_id varchar(60) NOT NULL,
PRIMARY KEY (song_id, user_id)
)
