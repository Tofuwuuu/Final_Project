""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
import datetime
from tkcalendar import DateEntry
import models.resources as res
import models.datetimeformatter as dtf

class CreationWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Instance of the database inherit from the master application window
        self.db_instance = self.master.db_instance
        # user data defined by the master
        self.user_data = self.master.user_data

        # Window Configurations
        self.geometry("500x600")
        self.title(f"CvSU Consult - Create a Consultation Request")
        self.iconbitmap(res.images.window_icon)

        # Styling as row-stretch
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # TitleWrapper for grouping the title bars
        self.TitleWrapper = ctk.CTkFrame(master=self, fg_color=res.constants.THEME_GREEN)
        self.TitleWrapper.grid(row=0, columnspan=1, padx=20, pady=10, ipady=10, sticky="nsew")
        self.TitleWrapper.grid_columnconfigure(0, weight=1)

        # TitleWrapper | TitleWrapper Welcome Message
        self.TitleLabel = ctk.CTkLabel(self.TitleWrapper, text=f"Open a Schedule", text_color="black", font=ctk.CTkFont(family=res.fonts.POPPINS, size=24, weight='bold'))
        self.TitleLabel.grid(row=0, column=0, pady=20, padx=10, sticky="w")

        # MainWrapper
        self.MainWrapper = ctk.CTkScrollableFrame(master=self, fg_color=res.constants.THEME_GREEN)
        self.MainWrapper.grid(row=5, columnspan=1, padx=20, pady=10, sticky="nsew")
        self.MainWrapper.grid_rowconfigure(3, weight=1)
        self.MainWrapper.grid_columnconfigure(4, weight=1)

        # Open Dates
        self.ScheduleDateLabel = ctk.CTkLabel(self.MainWrapper, text=f"{res.constants.PLACEHOLDER_DATE}: ", font=ctk.CTkFont(family=res.fonts.POPPINS, size=14))
        self.ScheduleDateLabel.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.ScheduleDate = DateEntry(master=self.MainWrapper, showothermonthdays=False, date_pattern='y-mm-dd', mindate=datetime.datetime.now())
        self.ScheduleDate.grid(row=0, column=1, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Open Dates
        self.ScheduleStartLabel = ctk.CTkLabel(self.MainWrapper, text=f"{res.constants.PLACEHOLDER_TIME_START}: ", font=ctk.CTkFont(family=res.fonts.POPPINS, size=14))
        self.ScheduleStartLabel.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.ScheduleStartHours = ctk.CTkOptionMenu(self.MainWrapper, values=res.constants.HOUR_VALUES)
        self.ScheduleStartHours.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        self.ScheduleStartSeparator = ctk.CTkLabel(self.MainWrapper, text=":", font=ctk.CTkFont(family=res.fonts.POPPINS, size=14))
        self.ScheduleStartSeparator.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
        self.ScheduleStartMinutes = ctk.CTkOptionMenu(self.MainWrapper, values=res.constants.MINUTE_VALUES)
        self.ScheduleStartMinutes.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

        # Open Dates
        self.ScheduleEndLabel = ctk.CTkLabel(self.MainWrapper, text=f"{res.constants.PLACEHOLDER_TIME_END}: ", font=ctk.CTkFont(family=res.fonts.POPPINS, size=14))
        self.ScheduleEndLabel.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        self.ScheduleEndHours = ctk.CTkOptionMenu(self.MainWrapper, values=res.constants.HOUR_VALUES)
        self.ScheduleEndHours.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
        self.ScheduleEndSeparator = ctk.CTkLabel(self.MainWrapper, text=":", font=ctk.CTkFont(family=res.fonts.POPPINS, size=14))
        self.ScheduleEndSeparator.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
        self.ScheduleEndMinutes = ctk.CTkOptionMenu(self.MainWrapper, values=res.constants.MINUTE_VALUES)
        self.ScheduleEndMinutes.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

        # Task Name
        self.ScheduleName = ctk.CTkEntry(master=self.MainWrapper, placeholder_text="Input schedule name")
        self.ScheduleName.grid(row=3, columnspan=3, padx=5, pady=5, sticky="nsew")

        # Open RequestButton
        self.FormHandlerStatus = ctk.CTkLabel(master=self.MainWrapper, text=None, text_color="Red", font=ctk.CTkFont(family=res.fonts.POPPINS, size=14))
        self.FormHandlerStatus.grid(row=4, columnspan=3, padx=5, pady=5, sticky="nsew")

        # Open RequestButton
        self.CreateButton = ctk.CTkButton(master=self.MainWrapper, text="Open a Schedule", command=self.CreateConsultation)
        self.CreateButton.grid(row=5, columnspan=3, padx=5, pady=5, sticky="nsew")

    def Getter(self) -> dict:
        legend = ['teacher_id', 'schedule_name', 'scheduled_on', 'open_at', 'close_at', 'status']
        _start = dtf.TimeBuilder(hours=int(self.ScheduleStartHours.get()), minutes=int(self.ScheduleStartMinutes.get()))
        _end = dtf.TimeBuilder(hours=int(self.ScheduleEndHours.get()), minutes=int(self.ScheduleEndMinutes.get()))

        data = [self.user_data['teacher_id'], self.ScheduleName.get(), self.ScheduleDate.get_date(), _start, _end, 'Open']
        return dict(zip(legend, data))

    def CreateConsultation(self) -> None:
        gathered_data = self.Getter()
        try:
            self.db_instance.InsertConsultationSchedule(gathered_data)
            self.FormHandlerStatus.configure(text="Successful!", text_color="green")
        except ValueError:
            print(f"{ValueError}")