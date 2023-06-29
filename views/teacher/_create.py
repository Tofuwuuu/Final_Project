""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
import datetime
from tktimepicker import AnalogPicker
from tkcalendar import DateEntry
import models.resources as res
import models.datetimeformatter as dtf

class CreationFrame(ctk.CTkFrame):

    PLACEHOLDER_DATE = 'Pick a date'
    PLACEHOLDER_TIME_START = 'Pick a starting time'
    PLACEHOLDER_TIME_END = 'Input session time'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # user data defined by the master
        self.user_data = self.master.user_data
        
        # Instance of the database inherit from the master application window
        self.db_instance = self.master.db_instance

        # Styling as row-stretch
        self.grid_columnconfigure(0, weight=5)
        self.grid_rowconfigure(1, weight=1)

        # TitleWrapper for grouping the title bars
        self.TitleWrapper = ctk.CTkFrame(master=self, fg_color=res.constants.THEME_GREEN)
        self.TitleWrapper.grid(row=0, columnspan=1, padx=20, pady=10, ipady=10, sticky="nsew")
        self.TitleWrapper.grid_columnconfigure(0, weight=1)

        # TitleWrapper | TitleWrapper Welcome Message
        self.TitleLabel = ctk.CTkLabel(self.TitleWrapper, text=f"Create a Consultation Request", text_color="black", font=ctk.CTkFont(family=res.fonts.POPPINS, size=24, weight='bold'))
        self.TitleLabel.grid(row=0, column=0, pady=20, padx=10, sticky="w")

        # TitleWrapper | Notifications
        self.NotifIcon = ctk.CTkButton(self.TitleWrapper, text=None, image=self.master.NotifImage, width=5, fg_color="transparent", hover_color="#Fdf0d5")
        self.NotifIcon.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # MainWrapper
        self.MainWrapper = ctk.CTkScrollableFrame(master=self, fg_color=res.constants.THEME_GREEN)
        self.MainWrapper.grid(row=1, columnspan=1, padx=20, pady=10, sticky="nsew")
        self.MainWrapper.grid_columnconfigure(0, weight=1)

        # Open Dates
        self.ScheduleDate = DateEntry(master=self.MainWrapper, showothermonthdays=False, date_pattern='y-mm-dd', mindate=datetime.datetime.now())
        self.ScheduleDate.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Open Dates
        self.ScheduleStart = AnalogPicker(self.MainWrapper, type=1)
        self.ScheduleStart.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        # Open Dates
        self.ScheduleEnd = AnalogPicker(self.MainWrapper, type=1)
        self.ScheduleEnd.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

        # Task Name
        self.ScheduleName = ctk.CTkEntry(master=self.MainWrapper, placeholder_text="Input schedule name")
        self.ScheduleName.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

        # Open RequestButton
        self.FormHandlerStatus = ctk.CTkLabel(master=self.MainWrapper, text=None, text_color="Red", font=ctk.CTkFont(family=res.fonts.POPPINS, size=14))
        self.FormHandlerStatus.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

        # Open RequestButton
        self.CreateButton = ctk.CTkButton(master=self.MainWrapper, text="Open a Schedule", command=self.CreateConsultation)
        self.CreateButton.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

    def Getter(self) -> dict:
        legend = ['teacher_id', 'schedule_name', 'schedule_on', 'open_at', 'close_at', 'status']
        _start = dtf.TimeBuilder(hours=self.ScheduleStart.hours(), minutes=self.ScheduleStart.minutes())
        _end = dtf.TimeBuilder(hours=self.ScheduleEnd.hours(), minutes=self.ScheduleEnd.minutes())

        data = [self.user_data['teacher_id'], self.ScheduleName.get(), self.ScheduleDate.get_date(), _start, _end, self.ScheduleName.get(), 'Open']
        return dict(zip(legend, data))

    def CreateConsultation(self) -> None:
        gathered_data = self.Getter()
        try:
            self.db_instance.InsertConsultationSchedule(gathered_data)
            self.FormHandlerStatus.configure(text="Successful!", text_color="green")
        except ValueError:
            print(f"{ValueError}")