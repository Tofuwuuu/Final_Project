""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
import tkinter as tk
import models.resources as res
import models.datetimeformatter as dtf

class ConsultationFrame(ctk.CTkFrame):

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
        self.SearchImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.search_light), dark_image=res.fetch_image(res.images.nav_ico.search_dark), size=(20, 20))
        self.SortImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.sort_light), dark_image=res.fetch_image(res.images.nav_ico.sort_dark), size=(20, 20))
        self.FilterImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.filter_light), dark_image=res.fetch_image(res.images.nav_ico.filter_dark), size=(20, 20))
        self.GoNextImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.go_next_dark), dark_image=res.fetch_image(res.images.nav_ico.go_next_light), size=(20, 20))
        self.SmallCalendarImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.calendar_dark), dark_image=res.fetch_image(res.images.nav_ico.calendar_light), size=(20, 20))
        self.UserProfileImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.user_profile_dark), dark_image=res.fetch_image(res.images.nav_ico.user_profile_light), size=(50, 50))
        """ End of resource pathing """

        # Styling as row-stretch
        self.grid_columnconfigure(0, weight=5)
        self.grid_rowconfigure(1, weight=1)

        # Theme design, because I can't setup json file for custom theme installation using set_default_theme.
        self.THEME_GREEN = self.master.THEME_GREEN
        self.THEME_YELLOW = self.master.THEME_YELLOW
        self.THEME_BLUE = self.master.THEME_BLUE
        self.THEME_DARKGREEN = self.master.THEME_DARKGREEN
        self.DEFAULT = self.master.DEFAULT

        # TitleWrapper for grouping the title bars
        self.TitleWrapper = ctk.CTkFrame(master=self, fg_color=self.THEME_GREEN)
        self.TitleWrapper.grid(row=0, columnspan=1, padx=20, pady=10, ipady=10, sticky="nsew")
        self.TitleWrapper.grid_columnconfigure(0, weight=1)

        # TitleWrapper | TitleWrapper Welcome Message
        self.TitleLabel = ctk.CTkLabel(self.TitleWrapper, text=f"Consultation History", text_color="black", font=ctk.CTkFont(family="Poppins", size=24, weight='bold'))
        self.TitleLabel.grid(row=0, column=0, pady=20, padx=10, sticky="w")

        # TitleWrapper | Notifications
        self.NotifIcon = ctk.CTkButton(self.TitleWrapper, text=None, image=self.NotifImage, width=5, fg_color="transparent", hover_color="#Fdf0d5")
        self.NotifIcon.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # MainWrapper
        self.MainWrapper = ctk.CTkFrame(master=self, fg_color=self.THEME_GREEN)
        self.MainWrapper.grid(row=1, columnspan=1, padx=20, pady=10, sticky="nsew")
        self.MainWrapper.grid_columnconfigure(0, weight=1)
        self.MainWrapper.grid_rowconfigure(0, weight=1)

        # ConsultationWrapper | For Consultation member schedules
        self.ConsultationWrapper = ctk.CTkFrame(master=self.MainWrapper, fg_color=self.THEME_DARKGREEN)
        self.ConsultationWrapper.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="nsew")
        self.ConsultationWrapper.grid_columnconfigure(0, weight=1)
        self.ConsultationWrapper.grid_rowconfigure(1, weight=1)

        # SearchUtilityWrapper | For Searching Utilities
        self.SearchUtilityWrapper = ctk.CTkFrame(master=self.ConsultationWrapper, fg_color="transparent")
        self.SearchUtilityWrapper.grid(row=0, column=0, columnspan=1, padx=5, pady=5, sticky="nsew")

        #SearchUtilityWrapper | Search Entry
        self.SearchEntry = ctk.CTkEntry(master=self.SearchUtilityWrapper, fg_color="transparent", placeholder_text="Search", text_color=("#242424", 'white'), corner_radius=5, height=35, width=345, font=ctk.CTkFont(family="Poppins", size=13))
        self.SearchEntry.grid(row=0, column=0, sticky="w")

        #SearchUtilityWrapper | Search Button
        self.SearchButton = ctk.CTkButton(master=self.SearchUtilityWrapper, width=90, height=33, text="Search", image=self.SearchImage, compound="right", text_color=self.THEME_YELLOW, font=ctk.CTkFont(family="Poppins", size=13), fg_color="#2B9348", hover_color="#55A630")
        self.SearchButton.grid(row=0, column=1, sticky="w")

        #SearchUtilityWrapper | Filter Button
        self.FilterButton = ctk.CTkButton(master=self.SearchUtilityWrapper, width=70, text="Filter", text_color=("#242424", 'white'), font=ctk.CTkFont(family="Poppins", size=11), fg_color="transparent", image=self.FilterImage, compound="right", border_color=self.THEME_GREEN, border_width=2, corner_radius=5, hover=self.THEME_YELLOW)
        self.FilterButton.grid(row=1, column=0, sticky="w")

        #SearchUtilityWrapper | Sort ComboBox
        self.SortVariable = ctk.StringVar(value="Sort")
        self.Sort = ctk.CTkComboBox(master=self.SearchUtilityWrapper, command=lambda value: self.UpdateDisplay(asc=value), values=["Ascending", "Descending"], variable=self.SortVariable, height=30, text_color=("#242424", 'white'), font=ctk.CTkFont(family="Poppins", size=11), dropdown_fg_color=self.THEME_YELLOW, fg_color=self.DEFAULT, border_color=self.THEME_GREEN, border_width=2, corner_radius=5, button_hover_color="#55A630", button_color=self.THEME_GREEN)
        self.Sort.grid(row=1, column=0, sticky="w")

        # ConsultationDataWrapper | For Data generated by querying the database
        self.ConsultationDataWrapper = ctk.CTkScrollableFrame(master=self.ConsultationWrapper, fg_color=self.THEME_GREEN)
        self.ConsultationDataWrapper.grid(row=1, columnspan=1, padx=5, pady=5, sticky="nsew")
    
    def UpdateDisplay(self, asc: str = "Descending") -> None:
        # Sort account history once, reducing computation needed in the loop below
        account_history = sorted(self.db_instance.FetchStudentHistory(self.user_data['student_id']), 
                                key=lambda x: x['scheduled_on'], 
                                reverse=(asc == "Descending"))

        # Using cashed data (record) and f-strings for variable name generation and string formatting
        for idx, record in enumerate(account_history):
            #creating the frames for each record
            frame = ctk.CTkFrame(master=self.ConsultationDataWrapper, fg_color="transparent", 
                                border_color="gray", border_width=2, corner_radius=5)
            frame.grid(row=idx, column=0, pady=10, padx=5, sticky="nsew")
            frame.grid_columnconfigure(3, weight=1)
            frame.grid_rowconfigure(2, weight=1)

            inner_frame = ctk.CTkFrame(master=frame, fg_color=self.THEME_BLUE, corner_radius=5)
            inner_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsw")
            inner_frame.grid_columnconfigure(0, weight=1)
            inner_frame.grid_rowconfigure(0, weight=1)

            teacher_frame = ctk.CTkFrame(master=frame, fg_color="transparent")
            teacher_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsw")
            teacher_frame.grid_columnconfigure(0, weight=1)
            teacher_frame.grid_rowconfigure(0, weight=1)

            info_frame = ctk.CTkFrame(master=frame, fg_color="transparent")
            info_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nsw")
            info_frame.grid_columnconfigure(0, weight=1)
            info_frame.grid_rowconfigure(0, weight=1)

            ctk.CTkLabel(master=inner_frame, 
                        text=f"{record['scheduled_on'].strftime('%d')}", 
                        text_color=("#2B9348", "#Fdf0d5"), 
                        font=ctk.CTkFont(family="Poppins", size=20, weight='bold')).grid(row=0, column=0, padx=30, sticky="nsew")

            ctk.CTkLabel(master=inner_frame, 
                        text=f"{record['scheduled_on'].strftime('%B')[0:3]}", 
                        text_color=("#2B9348", "#Fdf0d5"), 
                        font=ctk.CTkFont(family="Poppins", size=18, weight='bold')).grid(row=1, column=0, sticky="nsew")

            ctk.CTkLabel(master=teacher_frame, 
                        text=f"{record['teacher']}", 
                        text_color=("#2B9348", "#Fdf0d5"), 
                        font=ctk.CTkFont(family="Poppins", size=20, weight='bold')).grid(row=0, column=0, sticky="nsew")
            #Converting time and creating a formatted string
            session_start = dtf.ConvertTime(record['open_at'])
            session_end = dtf.ConvertTime(record['close_at'])
            formatted_time = f"{session_start} - {session_end}"

            ctk.CTkLabel(master=teacher_frame, 
                        text=f"{formatted_time}", 
                        text_color=("black", "white"), 
                        font=ctk.CTkFont(family="Poppins", size=12)).grid(row=1, column=0, sticky="w")

            ctk.CTkLabel(master=info_frame, 
                        text=f"{record['task_name']}", 
                        text_color=("black", "white"), 
                        font=ctk.CTkFont(family="Poppins", size=13, weight='bold')).grid(row=0, column=0, sticky="nsew")

            ctk.CTkLabel(master=info_frame, 
                        text=f"    {record['status']}", 
                        text_color=("black", "white"), 
                        font=ctk.CTkFont(family="Poppins", size=12)).grid(row=1, column=0, padx=30, sticky="w")
            # adding a clickable button for each record
            ctk.CTkButton(master=frame, 
                        command=lambda: self.master.SelectedPanel("consultation"), 
                        image=self.GoNextImage, 
                        text=None, 
                        fg_color="transparent", 
                        hover=None).grid(row=0, column=3, padx=5, pady=10, sticky="e")
