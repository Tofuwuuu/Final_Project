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
         
        """ Reference:
        For querying faculty members and their usernames

        Return(s):
            list: A list of usernames stored in the database.
            None: None 
        """

        with self.db.cursor() as cursor:
            
            # SQL query
            query_script = f"SELECT tbl_accounts.username FROM tbl_accounts WHERE role = 'T'"
            cursor.execute(query_script)
            names_data = [data[0] for data in cursor.fetchall()] 

            if asc:
                return sorted(names_data)
            else:
                return names_data
        
    def FetchFacultySchedules(self) -> list | None:
        
        """Reference:
        For querying faculty members schedule, joined table values for tbl_accounts and tbl_faculty
        """
        
        with self.db.cursor() as cursor:
            
            # SQL query
            query_script = f"SELECT tbl_accounts.username, tbl_faculty.* FROM tbl_accounts RIGHT JOIN tbl_faculty ON tbl_accounts.account_id = tbl_faculty.teacher_id ORDER BY tbl_faculty.scheduled_on ASC"
            cursor.execute(query_script)
            data = cursor.fetchall()

            #Get the column names
            legend = [column[0] for column in cursor.description]

            # Making a list of dictionaries to represent data
            return [dict(zip(legend, idx)) for idx in data]

    def FetchUserHistory(self, account_id: int) -> list:
        """ Reference
        Fetching the account related consultation schedules """
         
        with self.db.cursor() as cursor:
            
            # SQL query
            query_script = f"SELECT con.history_id, con.task_description, student.username AS student, teacher.username AS teacher, con.status, sched.scheduled_on, sched.open_at, sched.close_at FROM tbl_consultations AS con LEFT JOIN tbl_accounts AS teacher ON teacher.account_id = con.requested_to LEFT JOIN tbl_faculty AS sched ON sched.teacher_id = con.requested_to LEFT JOIN tbl_accounts AS student ON student.account_id = con.created_by WHERE student.account_id = {account_id}"
            cursor.execute(query_script)
            data = cursor.fetchall()

            #Get the column names
            legend = [column[0] for column in cursor.description]

            # Making a list of dictionaries to represent data
            return [dict(zip(legend, idx)) for idx in data]
