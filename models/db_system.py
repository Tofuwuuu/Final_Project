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

    # Searching User in the csystem.sql tbl_account
    def SearchUserByEmail(self, email:str) -> list | None:
        """  Get existing user information if any.
        returns {grouped_data: dict, None: None} 
        """
        grouped_data = self.QueryAccountData()
        for idx in range(len(grouped_data)):
                if grouped_data[idx]["email"] == email:
                    return grouped_data[idx]
                
    # Self-explanatory method for searching user
    def SearchUserByUsername(self, username:str) -> list | None:
        # Get existing user information if any.
        # returns {grouped_data: dict, None: None}
        grouped_data = self.QueryAccountData()
        for idx in range(len(grouped_data)):
                if grouped_data[idx]["username"] == username:
                    return grouped_data[idx]



    def QueryAccountData(self) -> list | None:
        """ Reference:
         Query data on tbl_accounts """
        
        with self.db.cursor() as cursor:
            # SQL Query
            query_script = "SELECT * FROM tbl_accounts"
            cursor.execute(query_script)
            findings = cursor.fetchall()

            #  Get the column names
            legend = [column[0] for column in cursor.description]

            # Making a list of dictionaries to represent data
            return [dict(zip(legend, idx)) for idx in findings]
        
    def RegisterUserAccount(self, fname: str, lname: str, username:str, email: str, password: str, role: str) -> None:
            """ Reference:
             Inserting validated user information to the database. """
            
            with self.db.cursor() as cursor:

                # SQL Query
                query_script = f"INSERT INTO tbl_accounts (first_name, last_name, username, email, password, role) VALUES ('{fname}', '{lname}', '{username}', '{email}', '{password}', '{role}')"

                cursor.execute(query_script)
                self.db.commit()


    def FetchFacultyNames(self, asc: bool = True) -> list | None:
         
        """ ## Reference
        #### returns [username] | role = 'T'"""

        with self.db.cursor() as cursor:
            
            # SQL query
            query_script = f"SELECT acc.username FROM tbl_accounts AS acc WHERE role = 'T'"
            cursor.execute(query_script)
            names_data = [data[0] for data in cursor.fetchall()] 

            if asc:
                return sorted(names_data)
            else:
                return names_data
            
    def FetchOpenFacultySchedules(self) -> list | None:
        
        """ ## Reference
        #### returns UNIQUE [{username, email, first_name, last_name, tbl_faculty.*}] | status = 'Open' | ORDER BY faculty.scheduled_on ASC"""
        
        with self.db.cursor() as cursor:
            
            # SQL query
            query_script = f"SELECT acc.username, acc.email, acc.first_name, acc.last_name, fac.* FROM tbl_accounts AS acc RIGHT JOIN tbl_faculty as fac ON acc.account_id = fac.teacher_id WHERE fac.status = 'Open' ORDER BY fac.scheduled_on ASC"
            cursor.execute(query_script)
            data = cursor.fetchall()

            #Get the column names
            legend = [column[0] for column in cursor.description]

            # Making a list of dictionaries to represent data
            return [dict(zip(legend, idx)) for idx in data]
        
        
        
    def FetchClosestOpenSchedules(self) -> list | None:
        
        """ ## Reference
        #### returns UNIQUE [{username, tbl_faculty.*}] | status = 'Open'"""
        
        with self.db.cursor() as cursor:
            
            # SQL query
            query_script = f"SELECT DISTINCT acc.username, fac.* FROM tbl_accounts AS acc RIGHT JOIN tbl_faculty as fac ON acc.account_id = fac.teacher_id WHERE status = 'Open' ORDER BY fac.scheduled_on ASC"
            cursor.execute(query_script)
            data = cursor.fetchall()

            #Get the column names
            legend = [column[0] for column in cursor.description]

            # Making a list of dictionaries to represent data
            return [dict(zip(legend, idx)) for idx in data]

    def FetchUpcomingConsultations(self, account_id: int) -> list | None:
        """ ## Reference
        #### returns same as FetchAccountConsultationHistory: scheduled_on >= sql.CURDATE()"""
         
        with self.db.cursor() as cursor:
            
            # SQL query
            query_script = f"SELECT con.history_id, con.task_name, con.task_description, student.username AS student, teacher.username AS teacher, con.status, sched.scheduled_on, sched.open_at, sched.close_at FROM tbl_consultations AS con LEFT JOIN tbl_accounts AS student ON student.account_id = con.created_by LEFT JOIN tbl_faculty AS sched ON sched.schedule_id = con.schedule_id LEFT JOIN tbl_accounts AS teacher ON teacher.account_id = sched.teacher_id WHERE student.account_id = {account_id} AND CONVERT(sched.scheduled_on, DATE) >= CURDATE()"
            cursor.execute(query_script)
            data = cursor.fetchall()
            #Get the column names
            legend = [column[0] for column in cursor.description]

            # Making a list of dictionaries to represent data
            return [dict(zip(legend, idx)) for idx in data]
        
    def FetchUpcomingRequest(self, account_id: int) -> list | None:
        """ ## Reference
        #### returns same as FetchUpcomingConsultations: For teacher module"""
            
        with self.db.cursor() as cursor:
            
            # SQL query
            query_script = f"SELECT con.history_id, con.task_name, con.task_description, student.username AS student, teacher.username AS teacher, con.status, sched.scheduled_on, sched.open_at, sched.close_at FROM tbl_consultations AS con LEFT JOIN tbl_accounts AS student ON student.account_id = con.created_by LEFT JOIN tbl_faculty AS sched ON sched.schedule_id = con.schedule_id LEFT JOIN tbl_accounts AS teacher ON teacher.account_id = sched.teacher_id WHERE sched.teacher_id = {account_id} AND CONVERT(sched.scheduled_on, DATE) >= CURDATE()"
            cursor.execute(query_script)
            data = cursor.fetchall()
            #Get the column names
            legend = [column[0] for column in cursor.description]

            # Making a list of dictionaries to represent data
            return [dict(zip(legend, idx)) for idx in data]

    def FetchAccountConsultationHistory(self, account_id: int) -> list | None:
        """ ## Reference
        #### Fetching all of the account related consultation schedules
        #### returns [{history_id, task_name, task_description, student.student, teacher.teacher, status, schedule_id, scheduled_on, open_at, close_at, status}]"""
         
        with self.db.cursor() as cursor:
            
            # SQL query
            query_script = f"SELECT con.history_id, con.task_name, con.task_description, student.username AS student, teacher.username AS teacher, con.status, sched.schedule_id, sched.schedule_name, sched.scheduled_on, sched.open_at, sched.close_at, sched.status FROM tbl_consultations AS con LEFT JOIN tbl_accounts AS student ON student.account_id = con.created_by LEFT JOIN tbl_faculty AS sched ON sched.schedule_id = con.schedule_id LEFT JOIN tbl_accounts AS teacher ON teacher.account_id = sched.teacher_id WHERE student.account_id = {account_id} ORDER BY sched.scheduled_on DESC"
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
                query_script = f"INSERT INTO tbl_faculty (teacher_id, schedule_name, schedule_on, open_at, close_at, status) VALUES ('{request_data['teacher_id']}', '{request_data['schedule_name']}', '{request_data['schedule_on']}', '{request_data['open_at']}', '{request_data['close_at']}', '{request_data['status']}')"
                cursor.execute(query_script)
                self.db.commit()
                return True
        
        except ValueError:
            return False