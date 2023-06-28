/* MySQL code for database implementation, for actual production. */

DROP DATABASE IF EXISTS db_csystem;
CREATE DATABASE db_csystem;
USE db_csystem;

-- Table for accounts, account_id = 100.
CREATE TABLE account_students (
    student_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    username VARCHAR(60) NOT NULL,
    email VARCHAR(255) NOT NULL,
    pass_id INT NOT NULL REFERENCES password_hashes(pass_id)
);

CREATE TABLE account_teachers (
    teacher_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    prefix ENUM('Mr', 'Ms', 'Mrs') NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    username VARCHAR(60) NOT NULL,
    email VARCHAR(255) NOT NULL,
    pass_id INT NOT NULL REFERENCES password_hashes(pass_id)
);

CREATE TABLE password_hashes (
	pass_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    password_hash VARCHAR(255) NOT NULL
    );

CREATE TABLE faculty_schedules(
schedule_id INT NOT NULL PRIMARY KEY auto_increment,
teacher_id INT REFERENCES tbl_teachers(teacher_id),
schedule_name VARCHAR(30) NOT NULL, 
scheduled_on DATE NOT NULL,
open_at TIME NOT NULL,
close_at TIME NOT NULL,
status ENUM("Open", "Reserved", "Ended")
);

CREATE TABLE consultation_histories(
history_id INT NOT NULL PRIMARY KEY auto_increment, 
task_name VARCHAR(60) NOT NULL, 
task_description VARCHAR(255) NOT NULL,
student_id INT REFERENCES tbl_students(student_id),
schedule_id INT REFERENCES faculty_schedules(schedule_id),
status ENUM("Accepted", "Rejected", "Pending", "Ended") NOT NULL
);

ALTER TABLE account_students AUTO_INCREMENT = 100000;
ALTER TABLE account_teachers AUTO_INCREMENT = 200000;
ALTER TABLE password_hashes AUTO_INCREMENT = 300000;
ALTER TABLE faculty_schedules AUTO_INCREMENT = 1000000;
ALTER TABLE consultation_histories AUTO_INCREMENT = 2000000;

-- Test values for account_students
INSERT INTO account_students
VALUES (100000, 'John', 'Doe', 'John Doe', 'johndoe@gmail.com', 300000),
       (100001, 'Juan', 'Dela Cruz', 'Juan Dela Cruz', 'juandelacruz@gmail.com', 300001);

-- Test values for account_teachers
INSERT INTO account_teachers
VALUES (200000, 'Mr','John', 'Moe', 'John Moe', 'johnmoe@gmail.com', 300002),
       (200001, 'Mr', 'Nortz', 'Alingod', 'Nortz Alingod', 'nortzalingod@gmail.com', 300003),
       (200002, 'Ms', 'Jackie', 'Murallon', 'Jackie Murallon', 'jackiemurallon@gmail.com', 300004),
       (200003, 'Mr', 'Antonio', 'Gaspar', 'Antonio Gaspar', 'antoniogaspar@gmail.com', 300005),
       (200004, 'Mr', 'Kenver', 'Maliyan', 'Kenver Maliyan', 'Kenver Maliyan@gmail.com', 300006),
       (200005, 'Mrs', 'Aliyana', 'Samonte', 'Aliyana Samonte', 'aliyanasamonte@gmail.com', 300007),
       (200006, 'Mr', 'Samson', 'Miguel', 'Samson Miguel', 'samsonmiguel@gmail.com', 300008);

-- Test values for account_teachers
INSERT INTO password_hashes
VALUES (300000, 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ=='),
	   (300001, 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ=='),
       (300002, 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ=='),
       (300003, 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ=='),
       (300004, 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ=='),
       (300005, 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ=='),
       (300006, 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ=='),
       (300007, 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ=='),
       (300008, 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ==');

-- Test values for faculty_schedules
INSERT INTO faculty_schedules
VALUES 
    (1000000, 200002, 'Schedule 1 Open', '2023-07-28', '08:00:00', '10:00:00', 'Open'),
    (1000001, 200002, 'Schedule 2 Reserved', '2023-07-15', '10:30:00', '12:30:00', 'Reserved'),
    (1000002, 200003, 'Schedule 1 Open', '2023-07-27', '08:30:00', '10:30:00', 'Open'),
    (1000003, 200003, 'Schedule 2 Reserved', '2023-07-13', '11:00:00', '13:00:00', 'Reserved'),
    (1000004, 200004, 'Schedule 1 Open', '2023-07-28', '09:00:00', '11:00:00', 'Open'),
    (1000005, 200004, 'Schedule 2 Reserved', '2023-07-18', '11:30:00', '13:30:00', 'Reserved'),
    (1000006, 200005, 'Schedule 1 Open', '2023-07-20', '09:30:00', '11:30:00', 'Open'),
    (1000007, 200005, 'Schedule 2 Reserved', '2023-07-15', '12:00:00', '14:00:00', 'Reserved'),
    (1000008, 200006, 'Schedule 1 Open', '2023-07-22', '10:00:00', '12:00:00', 'Open'),
    (1000009, 200006, 'Schedule 2 Reserved', '2023-07-08', '12:30:00', '14:30:00', 'Reserved'),
    (1000010, 200004, 'Schedule 1 Open', '2023-07-23', '10:30:00', '12:30:00', 'Open'),
    (1000011, 200005, 'Schedule 2 Reserved', '2023-07-03', '13:00:00', '15:00:00', 'Reserved'),
    (1000012, 200006, 'Schedule 1 Open', '2023-07-09', '11:00:00', '13:00:00', 'Open'),
    (1000013, 200001, 'Schedule 2 Reserved', '2023-06-14', '13:30:00', '15:30:00', 'Ended'),
    (1000014, 200002, 'Schedule 3 Open', '2023-07-10', '08:00:00', '10:00:00', 'Open'),
    (1000015, 200003, 'Schedule 3 Reserved', '2023-07-11', '10:30:00', '12:30:00', 'Reserved'),
    (1000016, 200004, 'Schedule 3 Open', '2023-07-12', '08:30:00', '10:30:00', 'Open'),
    (1000017, 200005, 'Schedule 3 Reserved', '2023-07-13', '11:00:00', '13:00:00', 'Reserved'),
    (1000018, 200006, 'Schedule 3 Open', '2023-07-14', '09:00:00', '11:00:00', 'Open'),
    (1000019, 200002, 'Schedule 3 Reserved', '2023-07-15', '11:30:00', '13:30:00', 'Reserved'),
    (1000020, 200003, 'Schedule 3 Open', '2023-07-16', '09:30:00', '11:30:00', 'Open'),
    (1000021, 200002, 'Schedule 4 Reserved', '2023-07-17', '12:00:00', '14:00:00', 'Reserved'),
    (1000022, 200003, 'Schedule 4 Open', '2023-07-18', '10:00:00', '12:00:00', 'Open'),
    (1000023, 200004, 'Schedule 4 Reserved', '2023-07-19', '12:30:00', '14:30:00', 'Reserved'),
    (1000024, 200000, 'Schedule 4 Open', '2023-07-20', '10:30:00', '12:30:00', 'Open'),
    (1000025, 200006, 'Schedule 4 Reserved', '2023-07-21', '13:00:00', '15:00:00', 'Reserved'),
    (1000026, 200001, 'Schedule 4 Open', '2023-07-22', '11:00:00', '13:00:00', 'Open'),
    (1000027, 200001, 'Schedule 4 Reserved', '2023-07-23', '13:30:00', '15:30:00', 'Reserved'),
    (1000028, 200002, 'Schedule 5 Open', '2023-07-24', '08:00:00', '10:00:00', 'Open'),
    (1000029, 200003, 'Schedule 5 Reserved', '2023-07-25', '10:30:00', '12:30:00', 'Reserved'),
    (1000030, 200004, 'Schedule 5 Open', '2023-07-26', '08:30:00', '10:30:00', 'Open'),
    (1000031, 200005, 'Schedule 5 Reserved', '2023-07-27', '11:00:00', '13:00:00', 'Reserved'),
    (1000032, 200006, 'Schedule 5 Open', '2023-07-28', '09:00:00', '11:00:00', 'Open'),
    (1000033, 200005, 'Schedule 5 Reserved', '2023-07-29', '11:30:00', '13:30:00', 'Reserved'),
    (1000034, 200001, 'Schedule 5 Open', '2023-07-30', '09:30:00', '11:30:00', 'Open'),
    (1000035, 200002, 'Schedule 6 Reserved', '2023-07-31', '12:00:00', '14:00:00', 'Reserved'),
    (1000036, 200003, 'Schedule 6 Open', '2023-08-01', '10:00:00', '12:00:00', 'Open'),
    (1000037, 200004, 'Schedule 6 Reserved', '2023-08-02', '12:30:00', '14:30:00', 'Reserved'),
    (1000038, 200005, 'Schedule 6 Open', '2023-08-03', '10:30:00', '12:30:00', 'Open'),
    (1000039, 200006, 'Schedule 6 Reserved', '2023-08-04', '13:00:00', '15:00:00', 'Reserved'),
    (1000040, 200000, 'Schedule 6 Open', '2023-08-05', '11:00:00', '13:00:00', 'Open'),
    (1000041, 200001, 'Schedule 6 Reserved', '2023-08-06', '13:30:00', '15:30:00', 'Reserved'),
    (1000042, 200000, 'Schedule 7 Open', '2023-08-07', '08:00:00', '10:00:00', 'Open'),
    (1000043, 200003, 'Schedule 7 Reserved', '2023-08-08', '10:30:00', '12:30:00', 'Reserved'),
    (1000044, 200004, 'Schedule 7 Open', '2023-08-09', '08:30:00', '10:30:00', 'Open'),
    (1000045, 200005, 'Schedule 7 Reserved', '2023-08-10', '11:00:00', '13:00:00', 'Reserved'),
    (1000046, 200006, 'Schedule 7 Open', '2023-08-11', '09:00:00', '11:00:00', 'Open'),
    (1000047, 200003, 'Schedule 7 Reserved', '2023-08-12', '11:30:00', '13:30:00', 'Reserved'),
    (1000048, 200004, 'Schedule 7 Open', '2023-08-13', '09:30:00', '11:30:00', 'Open'),
    (1000049, 200000, 'Schedule 8 Reserved', '2023-08-14', '12:00:00', '14:00:00', 'Reserved'),
    (1000050, 200003, 'Schedule 8 Open', '2023-08-15', '10:00:00', '12:00:00', 'Open');


-- Test values for consultation_histories
INSERT INTO consultation_histories
VALUES
    (2000000, 'Brainstorming Session', 'Need help with creative ideas for a project', 100000, 1000004, 'Pending' ),
    (2000001, 'Resume Review', 'Looking for feedback and suggestions on my resume', 100000, 1000006, 'Pending'),
    (2000002, 'Study Plan Assistance', 'Need guidance in creating an effective study plan', 100000, 1000034, 'Pending'),
    (2000003, 'Website Design Feedback', 'Seeking input on the design of my website', 100000, 1000016, 'Pending'),
    (2000004, 'Career Advice', 'Looking for advice on career paths and opportunities', 100001, 1000049, 'Accepted'),
    (2000005, 'Interview Preparation', 'Need help preparing for upcoming interviews', 100001, 1000024, 'Pending'),
    (2000006, 'Presentation Practice', 'Seeking assistance in improving my presentation skills', 100001, 1000011, 'Accepted'),
    (2000007, 'Research Paper Review', 'Need feedback and suggestions on my research paper', 100001, 1000006, 'Ended'),
	(2000008, 'Coding Challenge Help', 'Need assistance with solving a coding challenge', 100000, 1000007, 'Accepted' ),
    (2000009, 'Project Proposal Review', 'Looking for feedback on my project proposal', 100000, 1000008, 'Pending'),
    (2000010, 'Study Group Formation', 'Interested in joining or forming a study group', 100000, 1000009, 'Accepted'),
    (2000011, 'Essay Proofreading', 'Need proofreading and editing for my essay', 100000, 1000003, 'Accepted'),
    (2000012, 'Course Selection Advice', 'Seeking recommendations for course selection', 100001, 1000004, 'Pending'),
    (2000013, 'Exam Preparation Tips', 'Looking for tips and strategies to excel in exams', 100001, 1000005, 'Accepted'),
    (2000014, 'Homework Help', 'Need assistance with homework assignments', 100001, 1000009, 'Accepted'),
    (2000015, 'Career Change Guidance', 'Seeking guidance on transitioning to a new career', 100001, 1000002, 'Ended'),
    (2000016, 'Professional Networking', 'Interested in expanding professional network', 100001, 1000027, 'Accepted' ),
    (2000017, 'Cover Letter Writing', 'Looking for assistance in writing a compelling cover letter', 100002, 1000037, 'Accepted'),
    (2000018, 'Exam Study Group', 'Forming a study group for exam preparation', 100001, 1000038, 'Pending'),
    (2000019, 'Coursework Help', 'Need help understanding and completing coursework', 100001, 1000018, 'Pending'),
    (2000020, 'Essay Writing Assistance', 'Seeking guidance in writing an effective essay', 100003, 1000029, 'Accepted'),
    (2000021, 'Thesis Proposal Review', 'Looking for feedback on my thesis proposal', 100001, 1000031, 'Accepted'),
    (2000022, 'Coding Project Collaboration', 'Seeking collaborators for a coding project', 100001, 1000099, 'Accepted'),
    (2000023, 'Technical Interview Practice', 'Need practice and feedback for technical interviews', 100000, 1000006, 'Pending'),
    (2000024, 'Data Analysis Help', 'Need assistance with data analysis for my research', 100000, 10000041, 'Pending'),
    (2000025, 'Job Search Strategies', 'Looking for effective job search strategies and tips', 100000, 1000047, 'Ended'),
    (2000026, 'Presentation Feedback', 'Seeking feedback on my presentation delivery', 100001, 1000048, 'Pending'),
    (2000027, 'Language Learning Advice', 'Looking for tips and resources to improve language skills', 100000, 1000039, 'Accepted'),
    (2000028, 'Scholarship Application Review', 'Seeking review and suggestions for my scholarship application', 100000, 1000029, 'Accepted'),
    (2000029, 'Internship Search Assistance', 'Need guidance in finding suitable internship opportunities', 100000, 1000036, 'Pending'),
    (2000030, 'Programming Assignment Help', 'Seeking help with programming assignments', 100001, 1000024, 'Ended'),
    (2000031, 'Study Abroad Information', 'Looking for information and guidance on studying abroad', 100001, 1000016, 'Pending'),
    (2000032, 'Research Proposal Review', 'Seeking feedback on my research proposal', 100001, 1000046, 'Pending'),
    (2000033, 'Career Development Workshop', 'Interested in attending a career development workshop', 100001, 1000015, 'Accepted'),
    (2000034, 'Academic Advising', 'Need advice on course selection and academic planning', 100001, 1000028, 'Pending'),
    (2000035, 'Job Interview Coaching', 'Looking for coaching and practice for job interviews', 100001, 1000015, 'Accepted'),
    (2000036, 'Graduate School Application Help', 'Need assistance with graduate school applications', 100000, 1000020, 'Pending'),
    (2000037, 'Portfolio Review', 'Seeking feedback on my portfolio for creative work', 100001, 1000030, 'Pending'),
    (2000038, 'Entrepreneurship Advice', 'Looking for advice and guidance on starting a business', 100001, 1000040, 'Pending'),
    (2000039, 'Networking Event Information', 'Interested in information about upcoming networking events', 100001, 1000000, 'Pending'),
    (2000040, 'Financial Planning Consultation', 'Seeking advice on financial planning and budgeting', 100001, 1000001, 'Accepted'),
    (2000041, 'Writing Workshop Registration', 'Interested in registering for a writing workshop', 100001, 1000006, 'Pending'),
    (2000042, 'Study Space Recommendations', 'Looking for recommendations for quiet study spaces', 100000, 1000032, 'Pending'),
    (2000043, 'Career Fair Preparation', 'Need guidance on preparing for career fairs', 100001, 1000043, 'Accepted'),
    (2000044, 'Graduation Requirements Review', 'Seeking clarification on graduation requirements', 100000, 1000036, 'Pending'),
    (2000045, 'Time Management Strategies', 'Looking for strategies to improve time management skills', 100000, 1000024, 'Pending'),
    (2000046, 'Group Project Collaboration', 'Seeking group members for a collaborative project', 100000, 1000025, 'Accepted'),
    (2000047, 'Course Recommendation', 'Need recommendations for elective courses', 100001, 1000047, 'Accepted'),
    (2000048, 'Research Assistance', 'Looking for assistance in conducting research', 100001, 1000045, 'Accepted'),
    (2000049, 'Exam Proctoring', 'Need a proctor for an upcoming exam', 100001, 1000041, 'Accepted');
    
    

