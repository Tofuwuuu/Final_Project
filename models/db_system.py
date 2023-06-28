""" Reference:
Querying Module for database design of the system.
"""
import mysql.connector
from mysql.connector import Error
from .setup.init_db import *

class DBConnect:

    def __init__(self):
        # Database connection protocol
        self.db = mysql.connector.connect(
            host = sql_dbconfig.g_host,
            port = sql_dbconfig.g_port,
            user = sql_dbconfig.g_user,
            password = sql_dbconfig.g_password,
            database = sql_dbconfig.g_defaultdb
        )



# Implementation class for database design
class DBSystem(DBConnect):
    def __init__(self) -> None:
        super().__init__()

    def SearchUser(self, ctx:str) -> dict | None:
        """  Get existing user information from argument table filter -> email, if any.
        return list | None
        """

        try:
            student_findings = list(filter(lambda x: ctx in x.values(), self.FetchStudentAccounts()))
            teacher_findings = list(filter(lambda x: ctx in x.values(), self.FetchTeacherAccounts()))

            if student_findings:
                return student_findings[0]
            elif teacher_findings:
                return teacher_findings[0]

            return None
        except Error as err:
            print(f"{err}")
            return None
    
    def GetPassHash(self, pass_id: int) -> str:
        """ Return password hash """
        with self.db.cursor() as cursor:
            try:
                # SQL Query
                query_script = f"SELECT password_hash FROM password_hashes WHERE pass_id = {pass_id}"
                cursor.execute(query_script)
                findings = cursor.fetchall()
                return str(findings[0][0])
            except:
                return None

        

    def FetchStudentAccounts(self) -> list | None:
        """ Reference:
        Fetch all user data for account_student"""
        
        try:
            with self.db.cursor() as cursor:
                # SQL Query
                query_script = "SELECT * FROM account_students"
                cursor.execute(query_script)
                findings = cursor.fetchall()

                #  Get the column names
                legend = [column[0] for column in cursor.description]

            # Making a list of dictionaries to represent data
            return [dict(zip(legend, idx)) for idx in findings]
        except Error as err:
            print(f"{err}")
            return None
        
    def FetchTeacherAccounts(self) -> list | None:
        """ Reference:
        Fetch all user data for account_student"""
        
        with self.db.cursor() as cursor:
            # SQL Query
            query_script = "SELECT * FROM account_teachers"
            cursor.execute(query_script)
            findings = cursor.fetchall()

            #  Get the column names
            legend = [column[0] for column in cursor.description]

            # Making a list of dictionaries to represent data
            return [dict(zip(legend, idx)) for idx in findings]
        
    def RegisterStudent(self, fname: str, lname: str, username:str, email: str, password: str) -> None:
        """ Reference:
            Inserting validated student information into the database. """
        
        with self.db.cursor() as cursor:

            # SQL Query
            query_script = f"INSERT INTO account_students (first_name, last_name, username, email, pass_id) VALUES ('{fname}', '{lname}', '{username}', '{email}', '{self.PasswordSetter(password)}')"
            cursor.execute(query_script)
            self.db.commit()

    def PasswordSetter(self, password: str) -> int:
        """ Insert a password hash as a reference to an account id. Return int """
        with self.db.cursor() as cursor:
            try:
                # SQL Query
                insert_script = f"INSERT INTO password_hashes (password_hash) VALUES ('{password}')"
                cursor.execute(insert_script)
                self.db.commit()

                # Fetch id
                query_id = "SELECT @@identity"
                cursor.execute(query_id)
                pid = cursor.fetchone()
                
                return pid[0]
            except:
                return 0

    def FetchUpcomingTeacherConsultation(self, account_id: int) -> list | None:
        """ ## Reference
        #### returns upcoming consultation request for students"""
         
        with self.db.cursor() as cursor:
            try:
                # SQL query
                fetch_script = f"SELECT con.history_id, con.task_name, con.task_description, student.username AS student, teacher.username AS teacher, con.status, sched.scheduled_on, sched.open_at, sched.close_at FROM consultation_histories AS con LEFT JOIN account_students AS student ON student.student_id = con.student_id LEFT JOIN faculty_schedules AS sched ON sched.schedule_id = con.schedule_id LEFT JOIN account_teachers AS teacher ON teacher.teacher_id = sched.teacher_id WHERE student.student_id = {account_id} AND CONVERT(sched.scheduled_on, DATE) >= CURDATE()"
                cursor.execute(fetch_script)
                data = cursor.fetchall()
                #Get the column names
                legend = [column[0] for column in cursor.description]

                # Making a list of dictionaries to represent data
                return [dict(zip(legend, idx)) for idx in data]
            except:
                return None
            
    def FetchOpenFacultySchedules(self) -> list | None:
        
        """ ## Reference
        #### returns [{username, email, first_name, last_name, tbl_faculty.*}] | status = 'Open' | ORDER BY faculty.scheduled_on ASC"""
        
        with self.db.cursor() as cursor:
            try:
            # SQL query
                fetch_script = f"SELECT teacher.username, teacher.email, teacher.first_name, teacher.last_name, sched.* FROM account_teachers AS teacher RIGHT JOIN faculty_schedules as sched ON teacher.teacher_id = sched.teacher_id WHERE sched.status = 'Open' AND CONVERT(sched.scheduled_on, DATE) >= CURDATE() ORDER BY sched.scheduled_on ASC"
                cursor.execute(fetch_script)
                data = cursor.fetchall()

                #Get the column names
                legend = [column[0] for column in cursor.description]

                # Making a list of dictionaries to represent data
                return [dict(zip(legend, idx)) for idx in data]
            except:
                return None
            
    def FetchStudentHistory(self, account_id: int) -> list | None:
        """ ## Reference
        #### Fetching all of the account related consultation schedules
        #### returns [{history_id, task_name, task_description, student.student, teacher.teacher, status, schedule_id, scheduled_on, open_at, close_at, status}]"""
         
        with self.db.cursor() as cursor:
            
            try:
                # SQL query
                fetch_script = f"SELECT con.history_id, con.task_name, con.task_description, student.username AS student, teacher.username AS teacher, teacher.email AS teacher_email, con.status, sched.schedule_id, sched.schedule_name, sched.scheduled_on, sched.open_at, sched.close_at FROM consultation_histories AS con LEFT JOIN account_students AS student ON student.student_id = con.student_id LEFT JOIN faculty_schedules AS sched ON sched.schedule_id = con.schedule_id LEFT JOIN account_teachers AS teacher ON teacher.teacher_id = sched.teacher_id WHERE student.student_id = {account_id} ORDER BY sched.scheduled_on DESC"
                cursor.execute(fetch_script)
                data = cursor.fetchall()
                #Get the column names
                legend = [column[0] for column in cursor.description]

                # Making a list of dictionaries to represent data
                return [dict(zip(legend, idx)) for idx in data]
            except:
                return None

    def FetchTeacherHistory(self, account_id: int) -> list | None:
        """ ## Reference
        #### Fetching all of the account related consultation schedules
        #### returns [{history_id, task_name, task_description, student.student, teacher.teacher, status, schedule_id, scheduled_on, open_at, close_at, status}]"""
         
        with self.db.cursor() as cursor:
            
            try:
                # SQL query
                fetch_script = f"SELECT con.history_id, con.task_name, con.task_description, student.username AS student, teacher.username AS teacher, teacher.email AS teacher_email, con.status, sched.schedule_id, sched.schedule_name, sched.scheduled_on, sched.open_at, sched.close_at FROM consultation_histories AS con LEFT JOIN account_students AS student ON student.student_id = con.student_id LEFT JOIN faculty_schedules AS sched ON sched.schedule_id = con.schedule_id LEFT JOIN account_teachers AS teacher ON teacher.teacher_id = sched.teacher_id WHERE teacher.teacher_id = {account_id} ORDER BY sched.scheduled_on DESC"
                cursor.execute(fetch_script)
                data = cursor.fetchall()
                #Get the column names
                legend = [column[0] for column in cursor.description]

                # Making a list of dictionaries to represent data
                return [dict(zip(legend, idx)) for idx in data]
            except:
                return None



    def FetchStudentRequest(self, account_id: int) -> list | None:
        """ ## Reference
        #### returns same as FetchUpcomingConsultations: For teacher module"""
            
        with self.db.cursor() as cursor:
            
            try:
                # SQL query
                query_script = f"SELECT con.history_id, sched.schedule_id, teacher.teacher_id, con.task_name, con.task_description, sched.schedule_name, student.username AS student, teacher.username AS teacher, con.status AS request_status, sched.scheduled_on, sched.open_at, sched.close_at, sched.status AS schedule_status FROM consultation_histories AS con LEFT JOIN account_students AS student ON student.student_id = con.student_id LEFT JOIN faculty_schedules AS sched ON sched.schedule_id = con.schedule_id LEFT JOIN account_teachers AS teacher ON teacher.teacher_id = sched.teacher_id WHERE sched.teacher_id = {account_id} AND CONVERT(sched.scheduled_on, DATE) >= CURDATE()"
                cursor.execute(query_script)
                data = cursor.fetchall()
                #Get the column names
                legend = [column[0] for column in cursor.description]

                # Making a list of dictionaries to represent data
                return [dict(zip(legend, idx)) for idx in data]
            except:
                return None
            

    def FetchRequestHistory(self, account_id: int) -> list | None:
        """ ## Reference
        #### returns all request history referencing the account_id"""
            
        with self.db.cursor() as cursor:
            
            # SQL query
            query_script = f"SELECT con.history_id, sched.schedule_id, teacher.teacher_id, con.task_name, con.task_description, sched.schedule_name, student.username AS student, teacher.username AS teacher, con.status AS request_status, sched.scheduled_on, sched.open_at, sched.close_at, sched.status AS schedule_status FROM consultation_histories AS con LEFT JOIN account_students AS student ON student.student_id = con.student_id LEFT JOIN faculty_schedules AS sched ON sched.schedule_id = con.schedule_id LEFT JOIN account_teachers AS teacher ON teacher.teacher_id = sched.teacher_id WHERE sched.teacher_id = {account_id}"
            cursor.execute(query_script)
            data = cursor.fetchall()
            #Get the column names
            legend = [column[0] for column in cursor.description]

            # Making a list of dictionaries to represent data
            return [dict(zip(legend, idx)) for idx in data]


    def InsertConsultationRequest(self, request_data: dict) -> bool:
        """ Inserting requested_data into the consultation table """

        try:

            with self.db.cursor() as cursor:              
                # SQL query
                query_script = f"INSERT INTO tbl_consultations (task_name, task_description, created_by, schedule_id, status) VALUES ('{request_data['task_name']}', '{request_data['task_desc']}', '{request_data['student']}', '{request_data['schedule_id']}', '{request_data['status']}')"
                cursor.execute(query_script)
                self.db.commit()
                return True
        
        except ValueError:
            return False
        
    def InsertConsultationSchedule(self, request_data: dict) -> bool:
        
        try:

            with self.db.cursor() as cursor:              
                # SQL query
                query_script = f"INSERT INTO faculty_schedules (teacher_id, schedule_name, schedule_on, open_at, close_at, status) VALUES ('{request_data['teacher_id']}', '{request_data['schedule_name']}', '{request_data['schedule_on']}', '{request_data['open_at']}', '{request_data['close_at']}', '{request_data['status']}')"
                cursor.execute(query_script)
                self.db.commit()
                return True
        
        except ValueError:
            return False
        
    def AcceptRequestOnDB(self, schedule_id: int, history_id: int) -> bool:
        """ Update existing faculty and consultation request status for specific schedule_id and history_Id """
        
        try:
            with self.db.cursor() as cursor:
                # SQL query
                schedule_script = f"UPDATE faculty_schedules SET status = 'Reserved' WHERE schedule_id = {schedule_id}"
                consultation_script = f"UPDATE consultation_histories SET status = 'Accepted' WHERE history_id = {history_id}"
                cursor.execute(schedule_script)
                cursor.execute(consultation_script)
                self.db.commit()
                return True
        
        except ValueError:
            return False
        
    def DenyRequestOnDB(self, history_id: int) -> bool:
        """ Update existing faculty and consultation request status for specific schedule_id and history_Id """
        
        try:

            with self.db.cursor() as cursor:              
                # SQL query
                query_script = f"""UPDATE consultation_histories SET status = 'Rejected' WHERE history_id = {history_id};"""
                cursor.execute(query_script)
                self.db.commit()
                return True
        
        except ValueError:
            return False
        
if __name__ == "__main__":
    print(DBSystem().PasswordSetter('test'))