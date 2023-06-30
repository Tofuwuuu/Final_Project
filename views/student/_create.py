""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
import models.resources as res
import models.datetimeformatter as dtf

class CreationFrame(ctk.CTkToplevel):

    PLACEHOLDER_TEACHER = "Choose a teacher"
    PLACEHOLDER_DATE = 'Pick a date'
    PLACEHOLDER_TIME = 'Pick a time'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # user data defined by the master
        self.user_data = self.master.user_data

        # Window Configurations
        self.geometry("500x600")
        self.title(f"CvSU Consult - Create a Consultation Request")
        self.iconbitmap(res.images.window_icon)

        # Styling as row-stretch
        self.grid_columnconfigure(0, weight=5)
        self.grid_rowconfigure(1, weight=1)

        # TitleWrapper for grouping the title bars
        self.TitleWrapper = ctk.CTkFrame(master=self, fg_color="transparent")
        self.TitleWrapper.grid(row=0, columnspan=1, padx=20, pady=10, ipady=10, sticky="nsew")
        self.TitleWrapper.grid_columnconfigure(0, weight=1)

        # TitleWrapper | TitleWrapper Welcome Message
        self.TitleLabel = ctk.CTkLabel(self.TitleWrapper, text=f"Create a Consultation Request", text_color=res.constants.THEME_TEXT, font=ctk.CTkFont(family=res.fonts.POPPINS, size=20, weight='bold'))
        self.TitleLabel.grid(row=0, column=0, pady=20, padx=20, sticky="w")

        # MainWrapper
        self.MainWrapper = ctk.CTkFrame(master=self, fg_color=res.constants.THEME_GREEN)
        self.MainWrapper.grid(row=1, columnspan=1, padx=20, pady=10, sticky="nsew")
        self.MainWrapper.grid_columnconfigure(0, weight=1)

        # Teacher
        self.TeacherEntry = ctk.CTkOptionMenu(master=self.MainWrapper, command=lambda value: self.UpdateOpenDate(value), values=[self.PLACEHOLDER_TEACHER])
        self.TeacherEntry.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        # Open Dates
        self.TeacherOpenDateMenu = ctk.CTkOptionMenu(master=self.MainWrapper, command=lambda value: self.UpdateOpenTime(value), values=[self.PLACEHOLDER_DATE], state='disabled')
        self.TeacherOpenDateMenu.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        # Open Dates
        self.TeacherOpenTimeMenu = ctk.CTkOptionMenu(master=self.MainWrapper, values=[self.PLACEHOLDER_TIME], state='disabled')
        self.TeacherOpenTimeMenu.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

        # Task Name
        self.RequestTitle = ctk.CTkEntry(master=self.MainWrapper, placeholder_text="Add a request title")
        self.RequestTitle.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

        # Open Dates
        self.RequestBody = ctk.CTkEntry(master=self.MainWrapper, placeholder_text="Add a request description")
        self.RequestBody.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

        # Open RequestButton
        self.FormHandlerStatus = ctk.CTkLabel(master=self.MainWrapper, text=None, text_color="Red", font=ctk.CTkFont(family=res.fonts.POPPINS, size=14))
        self.FormHandlerStatus.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

        # Open RequestButton
        self.RequestButton = ctk.CTkButton(master=self.MainWrapper, command=self.FormHandler, text="Place a request")
        self.RequestButton.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")
    
    def UpdateOpenFaculty(self) -> None:
        open_data = self.db_instance.FetchOpenFacultySchedules()
        teacher_names = {data['username'] for data in open_data}
        self.TeacherEntry.configure(values=list(teacher_names))

    def UpdateOpenDate(self, value: str) -> None:
        open_data = self.db_instance.FetchOpenFacultySchedules()
        teacher_entry = value

        if isinstance(teacher_entry, (str)) and teacher_entry != self.PLACEHOLDER_TEACHER:

            date_data = [str(data['scheduled_on']) for data in open_data if data['username'] == teacher_entry]
            self.TeacherOpenDateMenu.configure(values=date_data, state="NORMAL")
    
    def UpdateOpenTime(self, value: str) -> None:
        open_data = self.db_instance.FetchOpenFacultySchedules()
        teacher_entry = self.TeacherEntry.get()
        date_entry = value

        if isinstance(date_entry, (str)) and date_entry != self.PLACEHOLDER_DATE:
            time_data = [dtf.ConvertTime(data['open_at']) for data in open_data if data['username'] == teacher_entry and str(data['scheduled_on']) == date_entry]
            self.TeacherOpenTimeMenu.configure(values=time_data, state="NORMAL")

    def Getter(self) -> dict:
        legend = ['teacher', 'date', 'time', 'title', 'body']
        data = [self.TeacherEntry.get(), self.TeacherOpenDateMenu.get(), self.TeacherOpenTimeMenu.get(), self.RequestTitle.get(), self.RequestBody.get()]
        return dict(zip(legend, data))
    
    def CheckIfExistingRequest(self) -> bool:
        form_data = self.Getter()
        user_generated_consultation_data = self.db_instance.FetchStudentHistory(self.user_data['student_id'])
        form_schedule_ids = [data['schedule_id'] for data in user_generated_consultation_data]
        teacher_data = [data for data in self.db_instance.FetchOpenFacultySchedules() if data['username'] == form_data['teacher'] and str(data['scheduled_on']) == form_data['date'] and dtf.ConvertTime(data['open_at']) == form_data['time']]
        if teacher_data and teacher_data[0]['schedule_id'] in form_schedule_ids:
            return False
        else:
            return True
        
    
    def FormHandler(self) -> None:
        self.FormHandlerStatus.configure(text_color='red')
        form_data = self.Getter()

        if form_data['teacher'] == self.PLACEHOLDER_TEACHER:
            pass
        elif form_data['date'] == self.PLACEHOLDER_DATE:
            self.FormHandlerStatus.configure(text="Error: you have not yet selected a date.")
        elif form_data['time'] == self.PLACEHOLDER_TIME:
            self.FormHandlerStatus.configure(text="Error: you have not yet selected a time.")
        elif form_data['title'] == '':
            self.FormHandlerStatus.configure(text="Error: no title.")
        elif form_data['body'] == '':
            self.FormHandlerStatus.configure(text="Error: no description.")
        elif self.CheckIfExistingRequest():
            self.FormHandlerStatus.configure(text="Error: no duplicating request.")
        else:
            if self.PlaceRequest():
                self.FormHandlerStatus.configure(text="Successfully placed a request!", text_color="Green")
        
    # Inserting request to the database
    def PlaceRequest(self) -> bool:

        # Get informations
        form_data = self.Getter()
        
        account_data = self.user_data
        teacher_data = [data for data in self.db_instance.FetchOpenFacultySchedules() if data['username'] == form_data['teacher'] and str(data['scheduled_on']) == form_data['date'] and dtf.ConvertTime(data['open_at']) == form_data['time']]

        gathered_data = {
            "student": account_data["student_id"],
            "schedule_id": teacher_data[0]["schedule_id"],
            "task_name": self.RequestTitle.get(),
            "task_desc": self.RequestBody.get(),
            "status": "Pending"
        }

        return self.db_instance.InsertConsultationRequest(gathered_data)

def _dangerouslyInit(user_data: list) -> None:
    app = CreationFrame(user_data=user_data)
    app.mainloop()