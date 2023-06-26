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
    role ENUM('S', 'T')
);

CREATE TABLE tbl_faculty(
history_id INT NOT NULL PRIMARY KEY auto_increment,
teacher_id INT REFERENCES tbl_accounts(account_id),
schedule_name VARCHAR(30) NOT NULL, 
scheduled_on DATE NOT NULL,
open_at TIME NOT NULL,
close_at TIME NOT NULL,
status ENUM("Open", "Reserved", "Ended")
);

CREATE TABLE tbl_consultations(
history_id INT NOT NULL PRIMARY KEY auto_increment, 
task_name VARCHAR(60) NOT NULL, 
task_description VARCHAR(60) NOT NULL,
created_by INT REFERENCES tbl_accounts(account_id),
requested_to INT REFERENCES tbl_accounts(account_id),
status ENUM("Accepted", "Rejected", "Pending", "Ended") NOT NULL
);

ALTER TABLE tbl_accounts AUTO_INCREMENT = 100000;
ALTER TABLE tbl_faculty AUTO_INCREMENT = 200000;
ALTER TABLE tbl_consultations AUTO_INCREMENT = 300000;

-- Test values for tbl_accounts
INSERT INTO tbl_accounts (first_name, last_name, username, email, password, role)
VALUES ('John', 'Doe', 'John Doe', 'johndoe@gmail.com', 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ==', 'S'),
       ('Juan', 'Dela Cruz', 'Juan Dela Cruz', 'juandelacruz@gmail.com', 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ==', 'S'),
       ('Teacher', 'Doe', 'Teacher Doe', 'teacherdoe@gmail.com', 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ==', 'T'),
       ('Nortz', 'Alingod', 'Nortz Alingod', 'nortzalingod@gmail.com', 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ==', 'T'),
       ('Jackie', 'Murallon', 'Jackie Murallon', 'jackiemurallon@gmail.com', 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ==', 'T'),
       ('Antonio', 'Gaspar', 'Antonio Gaspar', 'antoniogaspar@gmail.com', 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ==', 'T'),
       ('Kenver', 'Maliyan', 'Kenver Maliyan', 'Kenver Maliyan@gmail.com', 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ==', 'T'),
       ('Aliyana', 'Samonte', 'Aliyana Samonte', 'aliyanasamonte@gmail.com', 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ==', 'T'),
       ('Samson', 'Miguel', 'Samson Miguel', 'samsonmiguel@gmail.com', 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ==', 'T');
       
-- Test values for tbl_faculty
INSERT INTO tbl_faculty (teacher_id, schedule_name, scheduled_on, open_at, close_at, status)
VALUES (100002, "Schedule 1 Open", '2023-07-28', '10:00:00', '12:00:00', "Open"),
       (100002, "Schedule 2 Reserved",'2023-06-29', '13:00:00', '16:00:00', "Reserved"), 
       (100003, "Schedule 1 Open", '2023-07-27', '12:00:00', '14:00:00', "Open"),
       (100003, "Schedule 2 Reserved", '2023-06-29', '9:00:00', '11:30:00', "Reserved"),
       (100004, "Schedule 1 Open", '2023-07-28', '12:00:00', '14:00:00', "Open"),
       (100004, "Schedule 2 Reserved", '2023-06-25', '9:00:00', '11:30:00', "Reserved"),
       (100005, "Schedule 1 Open", '2023-07-20', '12:00:00', '14:00:00', "Open"),
       (100005, "Schedule 2 Reserved", '2023-06-17', '9:00:00', '11:30:00', "Reserved"),
       (100006, "Schedule 1 Open", '2023-07-21', '12:00:00', '14:00:00', "Open"),
       (100006, "Schedule 2 Reserved", '2023-06-06', '9:00:00', '11:30:00', "Reserved"),
       (100007, "Schedule 1 Open", '2023-07-23', '12:00:00', '14:00:00', "Open"),
       (100007, "Schedule 2 Reserved", '2023-06-03', '9:00:00', '11:30:00', "Reserved"),
       (100008, "Schedule 1 Open", '2023-07-09', '12:00:00', '14:00:00', "Open"),
       (100008, "Schedule 2 Reserved", '2023-06-14', '9:00:00', '11:30:00', "Reserved");

-- Test values for tbl_consultations
INSERT INTO tbl_consultations (task_name, task_description, created_by, requested_to, status)
VALUES
    ('Task 1', 'Description 1', 100000, 100002, 'Accepted' ),
    ('Task 2', 'Description 2', 100000, 100003, 'Pending'),
    ('Task 1', 'Description 1', 100000, 100007, 'Accepted'),
    ('Task 2', 'Description 2', 100000, 100003, 'Pending'),
    ('Task 1', 'Description 1', 100001, 100004, 'Accepted'),
    ('Task 2', 'Description 2', 100001, 100005, 'Pending'),
    ('Task 3', 'Description 3', 100001, 100004, 'Pending'),
    ('Task 4', 'Description 3', 100001, 100008, 'Ended');
    
    
