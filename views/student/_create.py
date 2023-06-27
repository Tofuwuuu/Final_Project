""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
import tkinter as tk
import models.resources as res
import models.datetimeformatter as dtf

class CreationFrame(ctk.CTkFrame):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # user data defined by the master
        self.user_data = self.master.user_data
        
        # Instance of the database inherit from the master application window
        self.db_instance = self.master.db_instance



        # load images with light and dark mode image
        """ File directory pathing for images """
        self.FacultyImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.faculty_dark), dark_image=res.fetch_image(res.images.nav_ico.faculty_light), size=(80, 80))
        self.CalendarImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.calendar_dark), dark_image=res.fetch_image(res.images.nav_ico.calendar_light), size=(80, 80))
        self.ConsultationImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.consultation_dark), dark_image=res.fetch_image(res.images.nav_ico.consultation_light), size=(80, 80))
        self.NotifImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.notif_dark), dark_image=res.fetch_image(res.images.nav_ico.notif_light), size=(20, 20))
        self.AlertNotifImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.alert_notif_dark), dark_image=res.fetch_image(res.images.nav_ico.alert_notif_light), size=(20, 20))
        """ End of resource pathing """

        # Styling as row-stretch
        self.grid_columnconfigure(0, weight=5)
        self.grid_rowconfigure(1, weight=1)

        # Theme design, because I can't setup json file for custom theme installation using set_default_theme.
        self.THEME_GREEN = self.master.THEME_GREEN
        self.THEME_YELLOW = self.master.THEME_YELLOW
        self.THEME_DARKGREEN = self.master.THEME_DARKGREEN
        self.DEFAULT = self.master.DEFAULT

        # TitleWrapper for grouping the title bars
        self.TitleWrapper = ctk.CTkFrame(master=self, fg_color=self.THEME_GREEN)
        self.TitleWrapper.grid(row=0, columnspan=1, padx=20, pady=10, ipady=10, sticky="nsew")
        self.TitleWrapper.grid_columnconfigure(0, weight=1)

        # TitleWrapper | TitleWrapper Welcome Message
        self.TitleLabel = ctk.CTkLabel(self.TitleWrapper, text=f"Create a Consultation Request", text_color="black", font=ctk.CTkFont(family="Poppins", size=24, weight='bold'))
        self.TitleLabel.grid(row=0, column=0, pady=20, padx=10, sticky="w")

        # TitleWrapper | Notifications
        self.NotifIcon = ctk.CTkButton(self.TitleWrapper, text=None, image=self.NotifImage, width=5, fg_color="transparent", hover_color="#Fdf0d5")
        self.NotifIcon.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # MainWrapper
        self.MainWrapper = ctk.CTkFrame(master=self, fg_color=self.THEME_GREEN)
        self.MainWrapper.grid(row=1, columnspan=1, padx=20, pady=10, sticky="nsew")
        self.MainWrapper.grid_columnconfigure(0, weight=1)

        # Teacher
        self.TeacherEntry = ctk.CTkOptionMenu(master=self.MainWrapper,command=lambda value: self.NextToName(value), values=['Choose a Teacher'])
        self.TeacherEntry.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        # Open Dates
        self.TeacherOpenDateMenu = ctk.CTkOptionMenu(master=self.MainWrapper, command=lambda value: self.NextToDate(value), values=['Pick a Date'], state='disabled')
        self.TeacherOpenDateMenu.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        # Open Dates
        self.TeacherOpenTimeMenu = ctk.CTkOptionMenu(master=self.MainWrapper, values=['Pick a Time'], state='disabled')
        self.TeacherOpenTimeMenu.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

        # Task Name
        self.RequestTitle = ctk.CTkEntry(master=self.MainWrapper, placeholder_text="Add a request title")
        self.RequestTitle.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

        # Open Dates
        self.RequestBody = ctk.CTkEntry(master=self.MainWrapper, placeholder_text="Add a request description")
        self.RequestBody.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

        # Open RequestButton
        self.RequestButton = ctk.CTkButton(master=self.MainWrapper, text="Place a request")
        self.RequestButton.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")
    
    def UpdateData(self):

        TeacherValue = [data['username'] for data in self.db_instance.FetchOpenFacultySchedules()]
        DateValue = [str(data['scheduled_on']) for data in self.db_instance.FetchOpenFacultySchedules()]
        TimeValue = [dtf.ConvertTime(data['open_at']) for data in self.db_instance.FetchOpenFacultySchedules()]

        self.TeacherEntry.configure(values=TeacherValue)
        self.TeacherOpenDateMenu.configure(values=DateValue)
        self.TeacherOpenTimeMenu.configure(values=TimeValue)
        
    
    def NextToName(self, name: str) -> None:
        if (isinstance(name, (str))) and name != "Choose a teacher":
            self.TeacherOpenDateMenu.configure(state="NORMAL")
    
    def NextToDate(self, date: str) -> None:
        if (isinstance(date, (str))) and date != "Pick a Date":
            self.TeacherOpenTimeMenu.configure(state="NORMAL")