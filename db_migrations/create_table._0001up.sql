-- create_tips_table.sql

DROP TABLE IF EXISTS tips;

CREATE TABLE tips (
    user_id TEXT,
    business_id TEXT,
    review_text TEXT,
    review_date TIMESTAMP,
    compliment_count INTEGER
);

