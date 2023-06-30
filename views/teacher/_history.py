""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk 
import models.resources as res
import models.datetimeformatter as dtf
class HistoryFrame(ctk.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # user data defined by the master
        self.user_data = self.master.user_data

        # cache frames
        self._cache_frame = {}
        self._cache_inner_frame = {}
        self._cache_teacher_frame = {}
        self._cache_info_frame = {}

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
        self.TitleLabel = ctk.CTkLabel(self.TitleWrapper, text=f"Consultation History", text_color="black", font=ctk.CTkFont(family=res.fonts.POPPINS, size=24, weight='bold'))
        self.TitleLabel.grid(row=0, column=0, pady=20, padx=10, sticky="w")

        # DashWrapper | Notifications
        self.CreateIcon = ctk.CTkButton(self.TitleWrapper, command=self.master.ShowCreateWindow ,text=None, image=self.master.CreateImage, width=5, fg_color="transparent", hover_color=(res.constants.THEME_YELLOW))
        self.CreateIcon.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # TitleWrapper | Notifications
        self.NotifIcon = ctk.CTkButton(self.TitleWrapper, text=None, image=self.master.NotifImage, width=5, fg_color="transparent", hover_color="#Fdf0d5")
        self.NotifIcon.grid(row=0, column=2, padx=10, pady=10, sticky="e")

        # MainWrapper
        self.MainWrapper = ctk.CTkFrame(master=self, fg_color="transparent")
        self.MainWrapper.grid(row=1, columnspan=1, padx=20, pady=10, sticky="nsew")
        self.MainWrapper.grid_columnconfigure(0, weight=1)
        self.MainWrapper.grid_rowconfigure(0, weight=1)

        # ConsultationWrapper | For Consultation member schedules
        self.ConsultationWrapper = ctk.CTkFrame(master=self.MainWrapper, fg_color="transparent")
        self.ConsultationWrapper.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="nsew")
        self.ConsultationWrapper.grid_columnconfigure(0, weight=1)
        self.ConsultationWrapper.grid_rowconfigure(1, weight=1)

        # SearchUtilityWrapper | For Searching Utilities
        self.SearchUtilityWrapper = ctk.CTkFrame(master=self.ConsultationWrapper, fg_color="transparent")
        self.SearchUtilityWrapper.grid(row=0, column=0, columnspan=1, padx=5, pady=5, sticky="nsew")

        #SearchUtilityWrapper | Search Entry
        self.SearchEntry = ctk.CTkEntry(master=self.SearchUtilityWrapper, fg_color="transparent", placeholder_text="Search", text_color=("#242424", 'white'), corner_radius=5, height=35, width=345, font=ctk.CTkFont(family=res.fonts.POPPINS, size=13))
        self.SearchEntry.grid(row=0, column=0, sticky="w")

        #SearchUtilityWrapper | Search Button
        self.SearchButton = ctk.CTkButton(master=self.SearchUtilityWrapper, command=self.UpdateHistory, width=90, height=33, text="Search", image=self.master.SearchImage, compound="right", text_color=res.constants.THEME_YELLOW, font=ctk.CTkFont(family=res.fonts.POPPINS, size=13), fg_color="#2B9348", hover_color="#55A630")
        self.SearchButton.grid(row=0, column=1, sticky="w")

        #SearchUtilityWrapper | Filter Button
        self.FilterButton = ctk.CTkButton(master=self.SearchUtilityWrapper, width=70, text="Filter", text_color=("#242424", 'white'), font=ctk.CTkFont(family=res.fonts.POPPINS, size=11), fg_color="transparent", image=self.master.FilterImage, compound="right", border_color=res.constants.THEME_GREEN, border_width=2, corner_radius=5, hover=res.constants.THEME_YELLOW)
        self.FilterButton.grid(row=1, column=0, sticky="w")

        #SearchUtilityWrapper | Sort ComboBox
        self.SortVariable = ctk.StringVar(value="Sort")
        self.Sort = ctk.CTkComboBox(master=self.SearchUtilityWrapper, command=lambda value: self.UpdateDispUpdateHistorylay(asc=value), values=["Ascending", "Descending", "Alphabetical"], variable=self.SortVariable, height=30, text_color=("#242424", 'white'), font=ctk.CTkFont(family=res.fonts.POPPINS, size=11), dropdown_fg_color=res.constants.THEME_YELLOW, fg_color=res.constants.THEME_DEFAULT, border_color=res.constants.THEME_GREEN, border_width=2, corner_radius=5, button_hover_color="#55A630", button_color=res.constants.THEME_GREEN)
        self.Sort.grid(row=1, column=0, sticky="w")

        # ConsultationDataWrapper | For Data generated by querying the database
        self.ConsultationDataWrapper = ctk.CTkScrollableFrame(master=self.ConsultationWrapper, fg_color="transparent")
        self.ConsultationDataWrapper.grid(row=1, columnspan=1, padx=5, pady=5, sticky="nsew")
    
    def ForgetAll(self) -> None:
        # Forget every grid
        for _ in map(lambda x: self._cache_frame[x].grid_forget(), list(self._cache_frame.keys())):
            pass
        for _ in map(lambda x: self._cache_inner_frame[x].grid_forget(), list(self._cache_inner_frame.keys())):
            pass
        for _ in map(lambda x: self._cache_teacher_frame[x].grid_forget(), list(self._cache_teacher_frame.keys())):
            pass
        for _ in map(lambda x: self._cache_info_frame[x].grid_forget(), list(self._cache_info_frame.keys())):
            pass

        # Clear all dynamic var
        self._cache_frame.clear()
        self._cache_inner_frame.clear()
        self._cache_teacher_frame.clear()
        self._cache_info_frame.clear()

    def UpdateHistory(self, asc: str = "Ascending") -> None:
        
        self.ForgetAll()

        # get the search entry value
        query = self.SearchEntry.get()
        
        """ Reference
        Update upcoming consultation based on realtime database."""

        account_history = self.db_instance.FetchStudentRequest(self.user_data['teacher_id'])

        if asc == "Ascending":
            account_history = sorted(account_history, key=lambda x: x["scheduled_on"])
        elif asc == "Descending":
            account_history = sorted(account_history, key=lambda x: x["scheduled_on"], reverse=True)
        elif asc == "Alphabetical":
            account_history = sorted(account_history, key=lambda x: x["teacher"], reverse=True)
        
        # if search is not empty, which is empty by default. Filter data to its value
        if query != "":
            query_data = [data for data in account_history if str(query).lower() in str(data['student']).lower()]
            if query_data is not None:
                account_history = query_data
        
        # Iteration to place dynamic data in the frame
        for idx in range(len(account_history)):
            
            # Main frame
            self._cache_frame[idx] = ctk.CTkFrame(master=self.ConsultationDataWrapper, fg_color="transparent", border_color="gray", border_width=2, corner_radius=5)
            self._cache_frame[idx].grid(row=idx, column=0, pady=10, padx=5, sticky="nsew")
            self._cache_frame[idx].grid_columnconfigure(3, weight=1)
            self._cache_frame[idx].grid_rowconfigure(3, weight=1)

            # Inner frame for date
            self._cache_inner_frame[idx] = ctk.CTkFrame(master=self._cache_frame[idx], fg_color=res.constants.THEME_BLUE, corner_radius=5)
            self._cache_inner_frame[idx].grid(row=0, column=0, padx=10, pady=10, sticky="nsw")
            self._cache_inner_frame[idx].grid_columnconfigure(0, weight=1)
            self._cache_inner_frame[idx].grid_rowconfigure(0, weight=1)

            # Inner frame for Schedule Info
            self._cache_teacher_frame[idx] = ctk.CTkFrame(master=self._cache_frame[idx], fg_color="transparent")
            self._cache_teacher_frame[idx].grid(row=0, column=1, padx=10, pady=10, sticky="nsw")
            self._cache_teacher_frame[idx].grid_columnconfigure(0, weight=1)
            self._cache_teacher_frame[idx].grid_rowconfigure(0, weight=1)

            # Inner frame for Informations
            self._cache_info_frame[idx] = ctk.CTkFrame(master=self._cache_frame[idx], fg_color="transparent")
            self._cache_info_frame[idx].grid(row=0, column=2, padx=10, pady=10, sticky="nsw")
            self._cache_info_frame[idx].grid_columnconfigure(0, weight=1)
            self._cache_info_frame[idx].grid_rowconfigure(0, weight=1)

            # Inner day label
            ctk.CTkLabel(master=self._cache_inner_frame[idx], text=f"{account_history[idx]['scheduled_on'].strftime('%d')}", text_color=res.constants.THEME_TEXT, font=ctk.CTkFont(family=res.fonts.POPPINS, size=20, weight='bold')).grid(row=0, column=0, padx=30, sticky="nsew")
            # Inner Month
            ctk.CTkLabel(master=self._cache_inner_frame[idx], text=f"{account_history[idx]['scheduled_on'].strftime('%B')[0:3]}", text_color=res.constants.THEME_TEXT, font=ctk.CTkFont(family=res.fonts.POPPINS, size=18, weight='bold')).grid(row=1, column=0, sticky="nsew")
            #Inner Teacher Text
            ctk.CTkLabel(master=self._cache_teacher_frame[idx], text=f"{account_history[idx]['student']}", text_color=res.constants.THEME_TEXT, font=ctk.CTkFont(family=res.fonts.POPPINS, size=20, weight='bold')).grid(row=0, column=0, sticky="nsew")


            # timedelta lost my sanity. It is not even a timezone conversion wtf.
            session_start = dtf.ConvertTime(account_history[idx]['open_at'])
            session_end = dtf.ConvertTime(account_history[idx]['close_at'])
            formatted_time = f"{session_start} - {session_end}"

            # Inner TimeSpan in TeacherWrapper
            ctk.CTkLabel(master=self._cache_teacher_frame[idx], text=f"Time: {formatted_time} | Status: {account_history[idx]['request_status']}", text_color=("black", "white"), font=ctk.CTkFont(family=res.fonts.POPPINS, size=12)).grid(row=1, column=0, sticky="w")
            # Inner TimeSpan in TeacherWrapper
            ctk.CTkLabel(master=self._cache_info_frame[idx], text=f"{account_history[idx]['task_name']}", text_color=("black", "white"), font=ctk.CTkFont(family=res.fonts.POPPINS, size=13, weight='bold')).grid(row=0, column=0, sticky="nsew")
            # Inner TimeSpan in TeacherWrapper
            ctk.CTkLabel(master=self._cache_info_frame[idx], text=f"{account_history[idx]['task_description']}", text_color=("black", "white"), font=ctk.CTkFont(family=res.fonts.POPPINS, size=12)).grid(row=1, column=0, padx=30, sticky="w")
            # Button gg go next
            ctk.CTkButton(master=self._cache_frame[idx], command=lambda:self.master.SelectedPanel("history"),image=self.master.GoNextImage, text=None, fg_color="transparent", hover=None).grid(row=0, column=4, padx=5, pady=10, sticky="e")