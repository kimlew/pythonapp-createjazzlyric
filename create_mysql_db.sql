CREATE DATABASE IF NOT EXISTS lyric_db;

USE lyric_db;

CREATE TABLE IF NOT EXISTS lyric (
    lyric_id INT unsigned NOT NULL AUTO_INCREMENT,
    lyric VARCHAR(50) NOT NULL,
    date_created DATETIME NOT NULL,
    date_deactivated DATETIME NULL,
    PRIMARY KEY(lyric_id)
);
