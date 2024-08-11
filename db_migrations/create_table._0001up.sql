-- create_tips_table.sql

DROP TABLE IF EXISTS tips;
DROP TABLE IF EXISTS users;

CREATE TABLE tips (
    user_id TEXT,
    business_id TEXT,
    review_text TEXT,
    review_date TIMESTAMP,
    compliment_count INTEGER
);

CREATE TABLE users (
    user_id TEXT,
    name VARCHAR(255),
    review_count INTEGER,
    yelping_since TIMESTAMP,
    useful INTEGER, 
    funny INTEGER, 
    cool INTEGER, 
    elite TEXT,
    friends TEXT,
    fans INTEGER,
    average_stars INTEGER,
    compliment_hot INTEGER, 
    compliment_more INTEGER, 
    compliment_profile INTEGER,
    compliment_cute INTEGER,
    compliment_list INTEGER,
    compliment_note INTEGER,
    compliment_plain INTEGER,
    compliment_cool INTEGER, 
    compliment_funny INTEGER,
    compliment_writer INTEGER,
    compliment_photos INTEGER
)