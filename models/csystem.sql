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
task_name VARCHAR(60) NOT NULL, 
task_description VARCHAR(255) NOT NULL,
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
VALUES 
    (200000, 100002, 'Schedule 1 Open', '2023-07-28', '08:00:00', '10:00:00', 'Open'),
    (200001, 100002, 'Schedule 2 Reserved', '2023-07-15', '10:30:00', '12:30:00', 'Reserved'),
    (200002, 100003, 'Schedule 1 Open', '2023-07-27', '08:30:00', '10:30:00', 'Open'),
    (200003, 100003, 'Schedule 2 Reserved', '2023-07-13', '11:00:00', '13:00:00', 'Reserved'),
    (200004, 100004, 'Schedule 1 Open', '2023-07-28', '09:00:00', '11:00:00', 'Open'),
    (200005, 100004, 'Schedule 2 Reserved', '2023-07-18', '11:30:00', '13:30:00', 'Reserved'),
    (200006, 100005, 'Schedule 1 Open', '2023-07-20', '09:30:00', '11:30:00', 'Open'),
    (200007, 100005, 'Schedule 2 Reserved', '2023-07-15', '12:00:00', '14:00:00', 'Reserved'),
    (200008, 100006, 'Schedule 1 Open', '2023-07-22', '10:00:00', '12:00:00', 'Open'),
    (200009, 100006, 'Schedule 2 Reserved', '2023-07-08', '12:30:00', '14:30:00', 'Reserved'),
    (200010, 100007, 'Schedule 1 Open', '2023-07-23', '10:30:00', '12:30:00', 'Open'),
    (200011, 100007, 'Schedule 2 Reserved', '2023-07-03', '13:00:00', '15:00:00', 'Reserved'),
    (200012, 100008, 'Schedule 1 Open', '2023-07-09', '11:00:00', '13:00:00', 'Open'),
    (200013, 100008, 'Schedule 2 Reserved', '2023-06-14', '13:30:00', '15:30:00', 'Ended'),
    (200014, 100002, 'Schedule 3 Open', '2023-07-10', '08:00:00', '10:00:00', 'Open'),
    (200015, 100003, 'Schedule 3 Reserved', '2023-07-11', '10:30:00', '12:30:00', 'Reserved'),
    (200016, 100004, 'Schedule 3 Open', '2023-07-12', '08:30:00', '10:30:00', 'Open'),
    (200017, 100005, 'Schedule 3 Reserved', '2023-07-13', '11:00:00', '13:00:00', 'Reserved'),
    (200018, 100006, 'Schedule 3 Open', '2023-07-14', '09:00:00', '11:00:00', 'Open'),
    (200019, 100007, 'Schedule 3 Reserved', '2023-07-15', '11:30:00', '13:30:00', 'Reserved'),
    (200020, 100008, 'Schedule 3 Open', '2023-07-16', '09:30:00', '11:30:00', 'Open'),
    (200021, 100002, 'Schedule 4 Reserved', '2023-07-17', '12:00:00', '14:00:00', 'Reserved'),
    (200022, 100003, 'Schedule 4 Open', '2023-07-18', '10:00:00', '12:00:00', 'Open'),
    (200023, 100004, 'Schedule 4 Reserved', '2023-07-19', '12:30:00', '14:30:00', 'Reserved'),
    (200024, 100005, 'Schedule 4 Open', '2023-07-20', '10:30:00', '12:30:00', 'Open'),
    (200025, 100006, 'Schedule 4 Reserved', '2023-07-21', '13:00:00', '15:00:00', 'Reserved'),
    (200026, 100007, 'Schedule 4 Open', '2023-07-22', '11:00:00', '13:00:00', 'Open'),
    (200027, 100008, 'Schedule 4 Reserved', '2023-07-23', '13:30:00', '15:30:00', 'Reserved'),
    (200028, 100002, 'Schedule 5 Open', '2023-07-24', '08:00:00', '10:00:00', 'Open'),
    (200029, 100003, 'Schedule 5 Reserved', '2023-07-25', '10:30:00', '12:30:00', 'Reserved'),
    (200030, 100004, 'Schedule 5 Open', '2023-07-26', '08:30:00', '10:30:00', 'Open'),
    (200031, 100005, 'Schedule 5 Reserved', '2023-07-27', '11:00:00', '13:00:00', 'Reserved'),
    (200032, 100006, 'Schedule 5 Open', '2023-07-28', '09:00:00', '11:00:00', 'Open'),
    (200033, 100007, 'Schedule 5 Reserved', '2023-07-29', '11:30:00', '13:30:00', 'Reserved'),
    (200034, 100008, 'Schedule 5 Open', '2023-07-30', '09:30:00', '11:30:00', 'Open'),
    (200035, 100002, 'Schedule 6 Reserved', '2023-07-31', '12:00:00', '14:00:00', 'Reserved'),
    (200036, 100003, 'Schedule 6 Open', '2023-08-01', '10:00:00', '12:00:00', 'Open'),
    (200037, 100004, 'Schedule 6 Reserved', '2023-08-02', '12:30:00', '14:30:00', 'Reserved'),
    (200038, 100005, 'Schedule 6 Open', '2023-08-03', '10:30:00', '12:30:00', 'Open'),
    (200039, 100006, 'Schedule 6 Reserved', '2023-08-04', '13:00:00', '15:00:00', 'Reserved'),
    (200040, 100007, 'Schedule 6 Open', '2023-08-05', '11:00:00', '13:00:00', 'Open'),
    (200041, 100008, 'Schedule 6 Reserved', '2023-08-06', '13:30:00', '15:30:00', 'Reserved'),
    (200042, 100002, 'Schedule 7 Open', '2023-08-07', '08:00:00', '10:00:00', 'Open'),
    (200043, 100003, 'Schedule 7 Reserved', '2023-08-08', '10:30:00', '12:30:00', 'Reserved'),
    (200044, 100004, 'Schedule 7 Open', '2023-08-09', '08:30:00', '10:30:00', 'Open'),
    (200045, 100005, 'Schedule 7 Reserved', '2023-08-10', '11:00:00', '13:00:00', 'Reserved'),
    (200046, 100006, 'Schedule 7 Open', '2023-08-11', '09:00:00', '11:00:00', 'Open'),
    (200047, 100007, 'Schedule 7 Reserved', '2023-08-12', '11:30:00', '13:30:00', 'Reserved'),
    (200048, 100008, 'Schedule 7 Open', '2023-08-13', '09:30:00', '11:30:00', 'Open'),
    (200049, 100002, 'Schedule 8 Reserved', '2023-08-14', '12:00:00', '14:00:00', 'Reserved'),
    (200050, 100003, 'Schedule 8 Open', '2023-08-15', '10:00:00', '12:00:00', 'Open');


-- Test values for tbl_consultations
INSERT INTO tbl_consultations
VALUES
    (300000, 'Brainstorming Session', 'Need help with creative ideas for a project', 100000, 200007, 'Accepted' ),
    (300001, 'Resume Review', 'Looking for feedback and suggestions on my resume', 100000, 200006, 'Pending'),
    (300002, 'Study Plan Assistance', 'Need guidance in creating an effective study plan', 100000, 200009, 'Accepted'),
    (300003, 'Website Design Feedback', 'Seeking input on the design of my website', 100000, 200004, 'Pending'),
    (300004, 'Career Advice', 'Looking for advice on career paths and opportunities', 100001, 200003, 'Accepted'),
    (300005, 'Interview Preparation', 'Need help preparing for upcoming interviews', 100001, 200010, 'Pending'),
    (300006, 'Presentation Practice', 'Seeking assistance in improving my presentation skills', 100001, 200012, 'Pending'),
    (300007, 'Research Paper Review', 'Need feedback and suggestions on my research paper', 100001, 200013, 'Ended'),
	(300008, 'Coding Challenge Help', 'Need assistance with solving a coding challenge', 100000, 200007, 'Accepted' ),
    (300009, 'Project Proposal Review', 'Looking for feedback on my project proposal', 100000, 200006, 'Pending'),
    (300010, 'Study Group Formation', 'Interested in joining or forming a study group', 100000, 200009, 'Accepted'),
    (300011, 'Essay Proofreading', 'Need proofreading and editing for my essay', 100000, 200004, 'Pending'),
    (300012, 'Course Selection Advice', 'Seeking recommendations for course selection', 100001, 200005, 'Accepted'),
    (300013, 'Exam Preparation Tips', 'Looking for tips and strategies to excel in exams', 100001, 200010, 'Pending'),
    (300014, 'Homework Help', 'Need assistance with homework assignments', 100001, 200012, 'Pending'),
    (300015, 'Career Change Guidance', 'Seeking guidance on transitioning to a new career', 100001, 200013, 'Ended'),
    (300016, 'Professional Networking', 'Interested in expanding professional network', 100002, 200005, 'Accepted' ),
    (300017, 'Cover Letter Writing', 'Looking for assistance in writing a compelling cover letter', 100002, 200011, 'Pending'),
    (300018, 'Exam Study Group', 'Forming a study group for exam preparation', 100003, 200006, 'Accepted'),
    (300019, 'Coursework Help', 'Need help understanding and completing coursework', 100003, 200009, 'Pending'),
    (300020, 'Essay Writing Assistance', 'Seeking guidance in writing an effective essay', 100003, 200003, 'Accepted'),
    (300021, 'Thesis Proposal Review', 'Looking for feedback on my thesis proposal', 100003, 200012, 'Pending'),
    (300022, 'Coding Project Collaboration', 'Seeking collaborators for a coding project', 100004, 200010, 'Accepted'),
    (300023, 'Technical Interview Practice', 'Need practice and feedback for technical interviews', 100004, 200008, 'Pending'),
    (300024, 'Data Analysis Help', 'Need assistance with data analysis for my research', 100004, 200013, 'Pending'),
    (300025, 'Job Search Strategies', 'Looking for effective job search strategies and tips', 100004, 200007, 'Ended'),
    (300026, 'Presentation Feedback', 'Seeking feedback on my presentation delivery', 100000, 200005, 'Accepted'),
    (300027, 'Language Learning Advice', 'Looking for tips and resources to improve language skills', 100000, 200011, 'Pending'),
    (300028, 'Scholarship Application Review', 'Seeking review and suggestions for my scholarship application', 100000, 200043, 'Accepted'),
    (300029, 'Internship Search Assistance', 'Need guidance in finding suitable internship opportunities', 100000, 200012, 'Pending'),
    (300030, 'Programming Assignment Help', 'Seeking help with programming assignments', 100001, 200013, 'Ended'),
    (300031, 'Study Abroad Information', 'Looking for information and guidance on studying abroad', 100001, 200009, 'Pending'),
    (300032, 'Research Proposal Review', 'Seeking feedback on my research proposal', 100001, 200010, 'Accepted'),
    (300033, 'Career Development Workshop', 'Interested in attending a career development workshop', 100001, 200007, 'Pending'),
    (300034, 'Academic Advising', 'Need advice on course selection and academic planning', 100002, 200004, 'Accepted'),
    (300035, 'Job Interview Coaching', 'Looking for coaching and practice for job interviews', 100002, 200006, 'Pending'),
    (300036, 'Graduate School Application Help', 'Need assistance with graduate school applications', 100002, 200009, 'Accepted'),
    (300037, 'Portfolio Review', 'Seeking feedback on my portfolio for creative work', 100002, 200023, 'Pending'),
    (300038, 'Entrepreneurship Advice', 'Looking for advice and guidance on starting a business', 100003, 200012, 'Accepted'),
    (300039, 'Networking Event Information', 'Interested in information about upcoming networking events', 100003, 200013, 'Pending'),
    (300040, 'Financial Planning Consultation', 'Seeking advice on financial planning and budgeting', 100003, 200005, 'Accepted'),
    (300041, 'Writing Workshop Registration', 'Interested in registering for a writing workshop', 100003, 200011, 'Pending'),
    (300042, 'Study Space Recommendations', 'Looking for recommendations for quiet study spaces', 100004, 200016, 'Accepted'),
    (300043, 'Career Fair Preparation', 'Need guidance on preparing for career fairs', 100004, 2000027, 'Pending'),
    (300044, 'Graduation Requirements Review', 'Seeking clarification on graduation requirements', 100004, 200003, 'Accepted'),
    (300045, 'Time Management Strategies', 'Looking for strategies to improve time management skills', 100000, 200011, 'Pending'),
    (300046, 'Group Project Collaboration', 'Seeking group members for a collaborative project', 100000, 200013, 'Accepted'),
    (300047, 'Course Recommendation', 'Need recommendations for elective courses', 100000, 200027, 'Pending'),
    (300048, 'Research Assistance', 'Looking for assistance in conducting research', 100001, 200046, 'Accepted'),
    (300049, 'Exam Proctoring', 'Need a proctor for an upcoming exam', 100001, 200029, 'Pending');
