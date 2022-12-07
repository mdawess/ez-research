
DROP SCHEMA IF EXISTS tldr cascade;  
CREATE SCHEMA tldr;  
SET search_path TO tldr; 

-- A user of the system
-- Use salt when adding into the database
CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
);

-- A tag that a user has
CREATE TABLE Tags (
    tag_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES Users,
    name VARCHAR(255) NOT NULL,
);

-- A piece of knowledge that a user has
CREATE TABLE Tldr (
    tldr_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES Users,
    tag_id INTEGER NOT NULL REFERENCES tags,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    weight INTEGER NOT NULL DEFAULT 0,
);

-- A connection between two pieces of knowledge
CREATE TABLE Connections (
    connection_id SERIAL PRIMARY KEY,
    tldr_id INTEGER NOT NULL REFERENCES Tldr,
    connected_tldr_id INTEGER NOT NULL REFERENCES Tldr,
    weight INTEGER NOT NULL DEFAULT 0,
);



