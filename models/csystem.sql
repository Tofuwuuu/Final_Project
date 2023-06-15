/* Actual MySQL code for database implementation, for use testing use cases. */

DROP DATABASE IF EXISTS db_csystem;
CREATE DATABASE db_csystem;
USE db_csystem;

-- Table for accounts, account_id = 100.
CREATE TABLE tbl_accounts (
    account_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    username VARCHAR(60) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    category CHAR(1)
);

ALTER TABLE tbl_accounts AUTO_INCREMENT = 100000;

CREATE TABLE tbl_history(
history_id INT NOT NULL PRIMARY KEY auto_increment, 
task_name VARCHAR(60) NOT NULL, 
task_description VARCHAR(60) NOT NULL,
created_by INT REFERENCES tbl_accounts(account_id),
requested_to INT REFERENCES tbl_accounts(account_id),
created_on DATETIME, 
status ENUM("Accepted", "Pending", "Ended") NOT NULL, 
ended_on DATETIME);


-- Test values for tbl_accounts
INSERT INTO tbl_accounts (first_name, last_name, username, email, password, category)
VALUES ('John', 'Doe', 'John Doe', 'johndoe@gmail.com', 'gAAAAABkiu7KLSH2YDUY_iRwx_NwyfhyWpdVFwSd2FNvmqpZJDuSpNsBh6HLrKLn-1uRjVDHtljQxWK1McSITP4mieqNI3jvNA==', 'S'),
       ('Teacher', 'Doe', 'Teacher Doe', 'teacherdoe@gmail.com', 'gAAAAABkiu7KLSH2YDUY_iRwx_NwyfhyWpdVFwSd2FNvmqpZJDuSpNsBh6HLrKLn-1uRjVDHtljQxWK1McSITP4mieqNI3jvNA==', 'T');
       
-- Test values for tbl_history
INSERT INTO tbl_history (task_name, task_description, created_by, requested_to, created_on, status, ended_on)
VALUES
    ('Task 1', 'Description 1', 100001, 100002, '2023-06-12 10:00:00', 'Accepted', '2023-06-13 15:30:00'),
    ('Task 2', 'Description 2', 100001, 100002, '2023-06-13 14:00:00', 'Pending', NULL),
    ('Task 3', 'Description 3', 100001, 100001, '2023-06-14 12:30:00', 'Ended', '2023-06-15 09:45:00');