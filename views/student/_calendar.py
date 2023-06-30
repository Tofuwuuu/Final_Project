""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
import tkinter as tk
import models.resources as res
from tkcalendar import Calendar
from views.student import _create

class CalendarFrame(ctk.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # user data defined by the master
        self.user_data = self.master.user_data

        # Instance of the database inherit from the master application window
        self.db_instance = self.master.db_instance

        # Styling as row-stretch
        self.grid_columnconfigure(0, weight=5)
        self.grid_rowconfigure(2, weight=1)

        # TitleWrapper for grouping the title bars
        self.TitleWrapper = ctk.CTkFrame(master=self, fg_color="transparent")
        self.TitleWrapper.grid(row=0, columnspan=1, padx=20, pady=10, ipady=10, sticky="nsew")
        self.TitleWrapper.grid_columnconfigure(0, weight=1)

        # CalendarUtilitiesWrapper
        self.CaledanrUtilitiesWrapper = ctk.CTkFrame(self, fg_color=res.constants.THEME_GREEN, height=50)
        self.CaledanrUtilitiesWrapper.grid(row=1, column=0, padx=20, pady=5, sticky="nsew")
        self.CaledanrUtilitiesWrapper.grid_columnconfigure(2, weight=1)

        # MainWrapper
        self.MainWrapper = ctk.CTkFrame(master=self, fg_color=res.constants.THEME_GREEN)
        self.MainWrapper.grid(row=2, columnspan=1, padx=20, pady=10, sticky="nsew")
        self.MainWrapper.grid_columnconfigure(0, weight=1)

        # TitleWrapper | TitleWrapper Welcome Message
        self.TitleLabel = ctk.CTkLabel(self.TitleWrapper, text=f"Calendar View", font=ctk.CTkFont(family=res.fonts.POPPINS, size=24, weight='bold'), text_color=res.constants.THEME_TEXT)
        self.TitleLabel.grid(row=0, column=0,  padx=20, pady=20, sticky="w")

        # TitleWrapper | Notifications
        self.NotifIcon = ctk.CTkButton(self.TitleWrapper, text=None, image=self.master.NotifImage, width=5, fg_color="transparent", hover_color="#Fdf0d5")
        self.NotifIcon.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # CalendarUtilitiesWrapper | Calendar Teacher Searching Utility
        self.FacultyText = ctk.CTkLabel(self.CaledanrUtilitiesWrapper, text="Choose a faculty member: ", font=ctk.CTkFont(family=res.fonts.POPPINS, size=15, weight='bold'))
        self.FacultyText.grid(row=0, column=0, padx=10, pady=5, ipady=5, ipadx=5, sticky="w")

        # CalendarUtilitiesWrapper | Calendar Teacher Searching Utility
        self.FacultyPicker = ctk.CTkOptionMenu(self.CaledanrUtilitiesWrapper, command=(lambda username: self.QuerySchedules(username)), values=self.FetchFacultyNames(), fg_color=res.constants.THEME_DEFAULT, dropdown_fg_color=res.constants.THEME_YELLOW, button_color=res.constants.THEME_YELLOW, button_hover_color=res.constants.THEME_GREEN, text_color=res.constants.THEME_BNW, width=90)
        self.FacultyPicker.grid(row=0, column=1, padx=10, pady=15, ipady=5, ipadx=5, sticky="w")

        # CalendarUtilitiesWrapper | Calendar Scheduling Creation Dialog
        self.ScheduleButton = ctk.CTkButton(self.CaledanrUtilitiesWrapper, command=self.CreateSchedule, image=self.master.SmallCalendarImage, text="Schedule a Consultation", font=ctk.CTkFont(family=res.fonts.POPPINS, size=14), fg_color=res.constants.THEME_YELLOW, text_color=res.constants.THEME_TEXT, hover=None)
        self.ScheduleButton.grid(row=0, column=2, padx=10, pady=5, ipady=5, ipadx=5, sticky="e")

        # MainWrapper | Add calendar widget
        self.calendar = Calendar(self.MainWrapper, font=ctk.CTkFont(family=res.fonts.POPPINS, size=16),showothermonthdays=False, selectbackground="#80B699", selectmode="none")
        self.calendar.pack(expand=True, fill=tk.BOTH)

    def FetchFacultyNames(self) -> list:
        db = self.db_instance.FetchOpenFacultySchedules()

        if db is not None:
            fetched_data = list({data['username'] for data in db})
            return fetched_data

    def QuerySchedules(self, username: str) -> None:

        self.calendar.calevent_remove(ev_ids='all')

        """ Reference
        Query data in faculty schedules matching the chosen faculty member's username """
        db = self.db_instance.FetchOpenFacultySchedules()

        if db is not None:
            fetched_data = [data for data in db if data['username'] == username]
        else:
            return None
        
        self.calendar.configure(mindate=(fetched_data[0]['scheduled_on']), maxdate=(fetched_data[-1]['scheduled_on']))

        # Generate calendar event on open status schedules
        for data in fetched_data:
            self.calendar.calevent_create(date=data['scheduled_on'], text=data['schedule_name'], tags=data['schedule_name'])

    def CreateSchedule(self):
        self.CreateSched = _create.CreationFrame()