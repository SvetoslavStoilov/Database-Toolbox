# CREATING
CREATE TABLE
IF NOT EXISTS articles
(
    heading VARCHAR
(255) NOT NULL,
    sub_heading VARCHAR
(500),
    author VARCHAR
(255),
    pub_date DATE NOT NULL,
    url VARCHAR
(255) NOT NULL,
    website VARCHAR
(255) NOT NULL,
    PRIMARY KEY
(url)
);
CREATE TABLE
IF NOT EXISTS websites_meta
(
    website VARCHAR
(255) NOT NULL,
    region VARCHAR
(255) NOT NULL,
    about VARCHAR
(255) NOT NULL,
    PRIMARY KEY
(website)
);