""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
import tkinter as tk
import models.resources as res
import datetime

class FacultyFrame(ctk.CTkFrame):

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
        self.TitleWrapper = ctk.CTkFrame(master=self, fg_color="transparent")
        self.TitleWrapper.grid(row=0, columnspan=1, padx=20, pady=10, ipady=10, sticky="nsew")
        self.TitleWrapper.grid_columnconfigure(0, weight=1)

        # TitleWrapper | TitleWrapper Welcome Message
        self.TitleLabel = ctk.CTkLabel(self.TitleWrapper, text=f"Faculty Consultation Schedule", text_color=("#2B9348", "#Fdf0d5"), font=ctk.CTkFont(family="Poppins", size=24, weight='bold'))
        self.TitleLabel.grid(row=0, column=0, pady=20, padx=10, sticky="w")

        # TitleWrapper | Notifications
        self.NotifIcon = ctk.CTkButton(self.TitleWrapper, text=None, image=self.NotifImage, width=5, fg_color="transparent", hover_color=self.THEME_YELLOW)
        self.NotifIcon.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # MainWrapper
        self.MainWrapper = ctk.CTkFrame(master=self, fg_color="transparent")
        self.MainWrapper.grid(row=1, columnspan=1, padx=20, pady=0, sticky="nsew")
        self.MainWrapper.grid_columnconfigure(0, weight=1)
        self.MainWrapper.grid_rowconfigure(0, weight=1)

        # FacultyWrapper | For faculty member schedules
        self.FacultyWrapper = ctk.CTkFrame(master=self.MainWrapper, fg_color="transparent")
        self.FacultyWrapper.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        self.FacultyWrapper.grid_columnconfigure(0, weight=1)
        self.FacultyWrapper.grid_rowconfigure(1, weight=1)

        # SearchUtilityWrapper | For Searching Utilities
        self.SearchUtilityWrapper = ctk.CTkFrame(master=self.FacultyWrapper, fg_color="transparent")
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
        self.Sort = ctk.CTkComboBox(master=self.SearchUtilityWrapper, values=["Ascending", "Descending"], variable=self.SortVariable, height=30, text_color=("#242424", 'white'), font=ctk.CTkFont(family="Poppins", size=11), dropdown_fg_color=self.THEME_YELLOW, fg_color=self.DEFAULT, border_color=self.THEME_GREEN, border_width=2, corner_radius=5, button_hover_color="#55A630", button_color=self.THEME_GREEN)
        self.Sort.grid(row=1, column=0, sticky="w")

        # FacultyDataWrapper | For Data generated by querying the database
        self.FacultyDataWrapper = ctk.CTkScrollableFrame(master=self.FacultyWrapper, fg_color=self.THEME_GREEN)
        self.FacultyDataWrapper.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.FacultyDataWrapper.grid_columnconfigure(0, weight=1)
        self.FacultyDataWrapper.grid_rowconfigure(0, weight=1)

        # FacultyInfoWrapper | For faculty member information
        self.FacultyInfoWrapper = ctk.CTkFrame(master=self.MainWrapper, fg_color=self.THEME_DARKGREEN)
        self.FacultyInfoWrapper.grid(row=0, column=1, columnspan=1, padx=10, pady=10, sticky="nsew")
        self.FacultyInfoWrapper.grid_columnconfigure(0, weight=1)
        self.FacultyInfoWrapper.grid_rowconfigure(1, weight=1)

        # FacultyHeaderWrapper | For faculty member profile and information
        self.FacultyHeaderWrapper = ctk.CTkFrame(master=self.FacultyInfoWrapper, fg_color=self.THEME_GREEN)
        self.FacultyHeaderWrapper.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        # FacultyBodyWrapper | For faculty member informations regarding on schedules
        self.FacultyBodyWrapper = ctk.CTkFrame(master=self.FacultyInfoWrapper, fg_color=self.THEME_GREEN)
        self.FacultyBodyWrapper.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        
    def DisplayFaculty(self, asc: str = "Ascending") -> None:
            
            """ Reference
            Display faculty members as bars"""

            account_history = self.db_instance.FetchFacultySchedules()

            _cache_frame = []
            _cache_inner_frame = []
            _cache_teacher_frame = []
            _cache_info_frame = []

            # Sort by username of the teacher
            sorted_faculty = account_history

            if asc == "Ascending":
                sorted_faculty = sorted(account_history, key=lambda x: x["username"])
            elif asc == "Descending":
                sorted_faculty = sorted(account_history, key=lambda x: x["username"], reverse=True)

            # Upcoming account consultation denoted by ("Pending", "Accepted") on column "status"
            upcoming_data = [data for data in sorted_faculty if data['status'] == 'Accepted' or 'Reserved']
            

            # Iteration to place dynamic data in the frame
            for idx in range(len(upcoming_data)):
                
                # Initializing cache variables
                _cache_frame.append("_cache_frame_".join(str(idx)))
                _cache_inner_frame.append("_cache_inner_frame_".join(str(idx)))
                _cache_teacher_frame.append("_cache_teacher_frame_".join(str(idx)))
                _cache_info_frame.append("_cache_info_frame_".join(str(idx)))

                # Main frame
                _cache_frame[idx] = ctk.CTkFrame(master=self.FacultyDataWrapper, fg_color=self.THEME_GREEN)
                _cache_frame[idx].grid(row=idx, column=0, pady=5, padx=5, sticky="nsew")
                _cache_frame[idx].grid_columnconfigure(3, weight=1)
                _cache_frame[idx].grid_rowconfigure(2, weight=1)

                # Inner frame for date
                _cache_inner_frame[idx] = ctk.CTkFrame(master=_cache_frame[idx], fg_color="transparent")
                _cache_inner_frame[idx].grid(row=0, column=0, padx=10, pady=10, sticky="nsw")
                _cache_inner_frame[idx].grid_columnconfigure(0, weight=1)
                _cache_inner_frame[idx].grid_rowconfigure(0, weight=1)

                # Inner frame for Schedule Info
                _cache_teacher_frame[idx] = ctk.CTkFrame(master=_cache_frame[idx], fg_color="transparent")
                _cache_teacher_frame[idx].grid(row=0, column=1, padx=10, pady=10, sticky="nsw")
                _cache_teacher_frame[idx].grid_columnconfigure(0, weight=1)
                _cache_teacher_frame[idx].grid_rowconfigure(0, weight=1)

                # Inner frame for Informations
                _cache_info_frame[idx] = ctk.CTkFrame(master=_cache_frame[idx], fg_color="transparent")
                _cache_info_frame[idx].grid(row=0, column=2, padx=10, pady=10, sticky="nsw")
                _cache_info_frame[idx].grid_columnconfigure(0, weight=1)
                _cache_info_frame[idx].grid_rowconfigure(0, weight=1)

                # Inner day label
                ctk.CTkLabel(master=_cache_inner_frame[idx], text=f"{upcoming_data[idx]['scheduled_on'].strftime('%b')}", text_color="white", font=ctk.CTkFont(family="Poppins", size=20, weight='bold')).grid(row=0, column=0, sticky="nsew")
                #Inner Teacher Text
                ctk.CTkLabel(master=_cache_teacher_frame[idx], text=f"{upcoming_data[idx]['username']}", text_color="white", font=ctk.CTkFont(family="Poppins", size=20, weight='bold')).grid(row=0, column=0, sticky="nsew")

                session_start = upcoming_data[idx]['open_at']
                session_end = upcoming_data[idx]['close_at']

                # Get the total seconds from the timedelta
                total_start = int(session_start.total_seconds())
                total_end = int(session_end.total_seconds())

                # Convert the total seconds to hours and minutes
                start_hours = total_start // 3600
                start_minutes = (total_start % 3600) // 60
                end_hours = total_end // 3600
                end_minutes = (total_end % 3600) // 60
                # Create a time object using the hours and minutes
                start_time_obj = datetime.time(start_hours, start_minutes)
                end_time_obj = datetime.time(end_hours, end_minutes)
                
                formatted_time = f"{start_time_obj.strftime('%I:%M %p')} - {end_time_obj.strftime('%I:%M %p')}"

                # Inner TimeSpan in TeacherWrapper
                ctk.CTkLabel(master=_cache_teacher_frame[idx], text=f"Time period: {formatted_time}", text_color="white", font=ctk.CTkFont(family="Poppins", size=10)).grid(row=1, column=0, sticky="nsew")
                # Status if Open or Reserved by tbl_faculty
                ctk.CTkLabel(master=_cache_info_frame[idx], text=f"{upcoming_data[idx]['status']}", text_color="white", font=ctk.CTkFont(family="Poppins", size=12)).grid(row=0, column=0, sticky="nsew")
                # Button GG go next
                ctk.CTkButton(master=_cache_frame[idx], image=self.GoNextImage, text=None, fg=self.THEME_YELLOW).grid(row=0, column=3, padx=20, pady=10, sticky="e")