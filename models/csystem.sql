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
schedule_id INT NOT NULL PRIMARY KEY auto_increment,
teacher_id INT REFERENCES tbl_accounts(account_id),
schedule_name VARCHAR(30) NOT NULL, 
scheduled_on DATE NOT NULL,
open_at TIME NOT NULL,
close_at TIME NOT NULL,
status ENUM("Open", "Reserved", "Ended")
);

CREATE TABLE tbl_consultations(
history_id INT NOT NULL PRIMARY KEY auto_increment, 
task_name VARCHAR(30) NOT NULL, 
task_description VARCHAR(60) NOT NULL,
created_by INT REFERENCES tbl_accounts(account_id),
schedule_id INT REFERENCES tbl_faculty(schedule_id),
status ENUM("Accepted", "Rejected", "Pending", "Ended") NOT NULL
);

ALTER TABLE tbl_accounts AUTO_INCREMENT = 100000;
ALTER TABLE tbl_faculty AUTO_INCREMENT = 200000;
ALTER TABLE tbl_consultations AUTO_INCREMENT = 300000;

-- Test values for tbl_accounts
INSERT INTO tbl_accounts
VALUES (100000, 'John', 'Doe', 'John Doe', 'johndoe@gmail.com', 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ==', 'S'),
       (100001, 'Juan', 'Dela Cruz', 'Juan Dela Cruz', 'juandelacruz@gmail.com', 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ==', 'S'),
       (100002, 'Teacher', 'Doe', 'Teacher Doe', 'teacherdoe@gmail.com', 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ==', 'T'),
       (100003, 'Nortz', 'Alingod', 'Nortz Alingod', 'nortzalingod@gmail.com', 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ==', 'T'),
       (100004, 'Jackie', 'Murallon', 'Jackie Murallon', 'jackiemurallon@gmail.com', 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ==', 'T'),
       (100005, 'Antonio', 'Gaspar', 'Antonio Gaspar', 'antoniogaspar@gmail.com', 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ==', 'T'),
       (100006, 'Kenver', 'Maliyan', 'Kenver Maliyan', 'Kenver Maliyan@gmail.com', 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ==', 'T'),
       (100007, 'Aliyana', 'Samonte', 'Aliyana Samonte', 'aliyanasamonte@gmail.com', 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ==', 'T'),
       (100008, 'Samson', 'Miguel', 'Samson Miguel', 'samsonmiguel@gmail.com', 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ==', 'T');
       
-- Test values for tbl_faculty
INSERT INTO tbl_faculty
VALUES (200000, 100002, "Schedule 1 Open", '2023-07-28', '10:00:00', '12:00:00', "Open"),
       (200001, 100002, "Schedule 2 Reserved",'2023-07-15', '13:00:00', '16:00:00', "Reserved"), 
       (200002, 100003, "Schedule 1 Open", '2023-07-27', '12:00:00', '14:00:00', "Open"),
       (200003, 100003, "Schedule 2 Reserved", '2023-07-13', '9:00:00', '11:30:00', "Reserved"),
       (200004, 100004, "Schedule 1 Open", '2023-07-28', '12:00:00', '14:00:00', "Open"),
       (200005, 100004, "Schedule 2 Reserved", '2023-07-18', '9:00:00', '11:30:00', "Reserved"),
       (200006, 100005, "Schedule 1 Open", '2023-07-20', '12:00:00', '14:00:00', "Open"),
       (200007, 100005, "Schedule 2 Reserved", '2023-07-15', '9:00:00', '11:30:00', "Reserved"),
       (200008, 100006, "Schedule 1 Open", '2023-07-22', '12:00:00', '14:00:00', "Open"),
       (200009, 100006, "Schedule 2 Reserved", '2023-07-08', '9:00:00', '11:30:00', "Reserved"),
       (200010, 100007, "Schedule 1 Open", '2023-07-23', '12:00:00', '14:00:00', "Open"),
       (200011, 100007, "Schedule 2 Reserved", '2023-07-03', '9:00:00', '11:30:00', "Reserved"),
       (200012, 100008, "Schedule 1 Open", '2023-07-09', '12:00:00', '14:00:00', "Open"),
       (200013, 100008, "Schedule 2 Reserved", '2023-06-14', '9:00:00', '11:30:00', "Ended");

-- Test values for tbl_consultations
INSERT INTO tbl_consultations
VALUES
    (300000, 'Task 1', 'Description 1', 100000, 200007, 'Accepted' ),
    (300001, 'Task 2', 'Description 2', 100000, 200006, 'Pending'),
    (300002, 'Task 1', 'Description 1', 100000, 200009, 'Accepted'),
    (300003, 'Task 2', 'Description 2', 100000, 200004, 'Pending'),
    (300004, 'Task 1', 'Description 1', 100001, 200003, 'Accepted'),
    (300005, 'Task 2', 'Description 2', 100001, 200010, 'Pending'),
    (300006, 'Task 3', 'Description 3', 100001, 200012, 'Pending'),
    (300007, 'Task 4', 'Description 3', 100001, 200013, 'Ended');
    