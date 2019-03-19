
CREATE TABLE threads (
        id serial PRIMARY KEY,
        fourchan_thread_id VARCHAR(100) UNIQUE,
        name VARCHAR(500),
        board_name VARCHAR(50)
);

CREATE TABLE posts (
        id serial PRIMARY KEY,
        post_comment text,
        post_subject text,
        thread_id integer references threads(id)
);

CREATE TABLE thread_files (
        id serial PRIMARY KEY,
        file_url text,
        thread_id integer references threads(id)
);



