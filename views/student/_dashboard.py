""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
import models.resources as res
import models.datetimeformatter as dtf

class DashboardFrame(ctk.CTkFrame):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # user data defined by the master
        self.user_data = self.master.user_data

        # Instance of the database inherit from the master application window
        self.db_instance = self.master.db_instance

        # cache frames
        self._cache_frame = {}
        self._cache_inner_frame = {}
        self._cache_teacher_frame = {}
        self._cache_info_frame = {}

        # Styling as row-stretch
        self.grid_columnconfigure(0, weight=5)
        self.grid_rowconfigure(1, weight=1)


        # Dashboard wrapper for grouping the dashboard utilities
        self.DashWrapper = ctk.CTkFrame(master=self, fg_color="transparent")
        self.DashWrapper.grid(row=0, columnspan=1, padx=20, pady=10, ipady=10, sticky="nsew")
        self.DashWrapper.grid_columnconfigure(0, weight=1)

        # DashWrapper | Dashboard Welcome Message
        self.WelcomeLabel = ctk.CTkLabel(self.DashWrapper, text=f"Welcome, {self.user_data['username']}!", text_color=res.constants.THEME_TEXT, font=ctk.CTkFont(family=res.fonts.POPPINS, size=24, weight='bold'))
        self.WelcomeLabel.grid(row=0, column=0, pady=20, padx=10, sticky="w")

        # DashWrapper | Notifications
        self.NotifIcon = ctk.CTkButton(self.DashWrapper, text=None, image=self.master.NotifImage, width=5, fg_color="transparent", hover_color=(res.constants.THEME_YELLOW))
        self.NotifIcon.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # Inner dashboard wrapper for grouping the dashboard utilities
        self.InnerDashWrapper = ctk.CTkFrame(self.DashWrapper, fg_color="transparent")
        self.InnerDashWrapper.grid(row=1, columnspan=5, padx=0, sticky="nsew")
        self.InnerDashWrapper.grid_columnconfigure(0, weight=1)
        self.InnerDashWrapper.grid_rowconfigure(0, weight=1)

        # Inner dashboard wrapper for grouping the dashboard utilities
        self.InnerInnerDashWrapper = ctk.CTkFrame(self.InnerDashWrapper, fg_color="transparent")
        self.InnerInnerDashWrapper.grid(row=0, column=0, padx=0)
        self.InnerInnerDashWrapper.grid_columnconfigure(1, weight=1)
        self.InnerInnerDashWrapper.grid_rowconfigure(0, weight=1)

        # Yet another inner wrapper for containing navigations
        self.FacultyDashWrapper = ctk.CTkFrame(self.InnerInnerDashWrapper, fg_color=(res.constants.THEME_YELLOW), width=160, height=185, corner_radius=5)
        self.FacultyDashWrapper.grid(row=0, column=0, padx=20, pady=0)
        self.FacultyDashWrapper.grid_columnconfigure(0, weight=1)
        self.FacultyDashWrapper.grid_rowconfigure(3, weight=2)

        # Yet another inner wrapper for containing navigations
        self.CalendarDashWrapper = ctk.CTkFrame(self.InnerInnerDashWrapper, fg_color=res.constants.THEME_YELLOW)
        self.CalendarDashWrapper.grid(row=0, column=1, padx=20, pady=0)
        self.CalendarDashWrapper.grid_columnconfigure(0, weight=1)
        self.CalendarDashWrapper.grid_rowconfigure(3, weight=2)

        # Yet another inner wrapper for containing navigations
        self.ConsultationDashWrapper = ctk.CTkFrame(self.InnerInnerDashWrapper, fg_color=res.constants.THEME_YELLOW)
        self.ConsultationDashWrapper.grid(row=0, column=2, padx=20, pady=0)
        self.ConsultationDashWrapper.grid_columnconfigure(0, weight=1)
        self.ConsultationDashWrapper.grid_rowconfigure(3, weight=2)

        # Large Faculty Image
        self.FacultyDashImage = ctk.CTkLabel(self.FacultyDashWrapper, text=None, image=self.master.FacultyImage)
        self.FacultyDashImage.grid(row=0, column=0, padx=5, pady=10)
        # Faculty Label
        self.FacultyDashLabel = ctk.CTkLabel(self.FacultyDashWrapper, text="Faculty Schedule", font=ctk.CTkFont(size=13, weight='bold'), text_color=res.constants.THEME_TEXT)
        self.FacultyDashLabel.grid(row=1, column=0, padx=25, pady=0)
        # Faculty Label
        self.FacultyDashButton = ctk.CTkButton(self.FacultyDashWrapper, text="View All",command=lambda: self.master.SelectedPanel('faculty'), width=100, height=25, corner_radius=5, fg_color="#2B9348", hover_color="#55A630", font=ctk.CTkFont(size=12))
        self.FacultyDashButton.grid(row=2, column=0, padx=7, pady=10)

        # Large Calendar Image
        self.CalendarDashImage = ctk.CTkLabel(self.CalendarDashWrapper, text=None, image=self.master.CalendarImage)
        self.CalendarDashImage.grid(row=0, column=0, padx=5, pady=10)
        # Calendar Label
        self.CalendarDashLabel = ctk.CTkLabel(self.CalendarDashWrapper, text="Calendar History", font=ctk.CTkFont(size=13, weight='bold'), text_color=res.constants.THEME_TEXT)
        self.CalendarDashLabel.grid(row=1, column=0, padx=25, pady=0)
        # Calendar Button
        self.CalendarDashButton = ctk.CTkButton(self.CalendarDashWrapper, text="View All", command=lambda: self.master.SelectedPanel('calendar'), width=100, height=25, corner_radius=5, fg_color="#2B9348", hover_color="#55A630", font=ctk.CTkFont(size=12))
        self.CalendarDashButton.grid(row=2, column=0, padx=7, pady=10)

        # Large Consultation Image
        self.ConsultationDashImage = ctk.CTkLabel(self.ConsultationDashWrapper, text=None, image=self.master.ConsultationImage)
        self.ConsultationDashImage.grid(row=0, column=0, padx=5, pady=10)
        # Consultation Label
        self.ConsultationDashLabel = ctk.CTkLabel(self.ConsultationDashWrapper, text="My Consultations", font=ctk.CTkFont(size=13, weight='bold'), text_color=res.constants.THEME_TEXT)
        self.ConsultationDashLabel.grid(row=1, column=0, padx=25, pady=0)
        # Consultation Button
        self.ConsultationDashButton = ctk.CTkButton(self.ConsultationDashWrapper, text="View All", command=lambda: self.master.SelectedPanel('history'), width=100, height=25, corner_radius=5, fg_color="#2B9348", hover_color="#55A630", font=ctk.CTkFont(size=12))
        self.ConsultationDashButton.grid(row=2, column=0, padx=7, pady=10)

        # Upcoming Consultation wrapper for grouping the dashboard utilities
        self.ConWrapper = ctk.CTkFrame(master=self, fg_color="transparent")
        self.ConWrapper.grid(row=1, columnspan=1, padx=20, pady=5, ipady=10, sticky="nsew")
        self.ConWrapper.grid_columnconfigure(0, weight=1)
        self.ConWrapper.grid_rowconfigure(2, weight=1)

        # ConWrapper | Upcoming Consultations Label
        self.UpcomingConsultationsLabel = ctk.CTkLabel(self.ConWrapper, text="Upcoming Consultations", text_color=res.constants.THEME_TEXT, font=ctk.CTkFont(family=res.fonts.POPPINS, size=20, weight='bold'))
        self.UpcomingConsultationsLabel.grid(row=0, column=0, pady=20, padx=20, sticky="w")

        # SearchUtilityWrapper | For Searching Utilities
        self.SearchUtilityWrapper = ctk.CTkFrame(master=self.ConWrapper, fg_color="transparent")
        self.SearchUtilityWrapper.grid(row=1, column=0, columnspan=1, padx=15, pady=15, sticky="nsew")

        #SearchUtilityWrapper | Search Entry
        self.SearchEntry = ctk.CTkEntry(master=self.SearchUtilityWrapper, fg_color="transparent", placeholder_text="Search", text_color=res.constants.THEME_TEXT, corner_radius=5, height=35, width=345, font=ctk.CTkFont(family=res.fonts.POPPINS, size=13))
        self.SearchEntry.grid(row=0, column=0, sticky="w")

        #SearchUtilityWrapper | Search Button
        self.SearchButton = ctk.CTkButton(master=self.SearchUtilityWrapper, command=self.UpdateUpcoming, width=90, height=33, text="Search", image=self.master.SearchImage, compound="right", text_color=res.constants.THEME_YELLOW, font=ctk.CTkFont(family=res.fonts.POPPINS, size=13), fg_color="#2B9348", hover_color="#55A630")
        self.SearchButton.grid(row=0, column=1, sticky="w")

        #SearchUtilityWrapper | Filter Button
        self.FilterButton = ctk.CTkButton(master=self.SearchUtilityWrapper, width=70, text="Filter", text_color=res.constants.THEME_TEXT, font=ctk.CTkFont(family=res.fonts.POPPINS, size=11), fg_color="transparent", image=self.master.FilterImage, compound="right", border_color=res.constants.THEME_GREEN, border_width=2, corner_radius=5, hover=res.constants.THEME_YELLOW)
        self.FilterButton.grid(row=1, column=0, sticky="w")

        #SearchUtilityWrapper | Sort ComboBox
        self.SortVariable = ctk.StringVar(value="Sort")
        self.Sort = ctk.CTkComboBox(master=self.SearchUtilityWrapper, command=lambda sort: self.UpdateUpcoming(sort), values=["Ascending", "Descending", "Alphabetical"], variable=self.SortVariable, height=30, text_color=res.constants.THEME_TEXT, font=ctk.CTkFont(family=res.fonts.POPPINS, size=11), dropdown_fg_color=res.constants.THEME_YELLOW, fg_color=res.constants.THEME_DEFAULT, border_color=res.constants.THEME_GREEN, border_width=2, corner_radius=5, button_hover_color="#55A630", button_color=res.constants.THEME_GREEN)
        self.Sort.grid(row=1, column=0, sticky="w")

        # Upcoming Consultation List Wrapper
        self.ConListWrapper = ctk.CTkScrollableFrame(master=self.ConWrapper, fg_color="transparent")
        self.ConListWrapper.grid(row=2, column=0, padx=20, pady=10, ipady=10, sticky="nsew") 
        self.ConListWrapper.grid_columnconfigure(0, weight=1)

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

    def UpdateUpcoming(self, asc: str = "Ascending") -> None:
        self.ForgetAll()

        # get the search entry value
        query = self.SearchEntry.get()
        
        """ Reference
        Update upcoming consultation based on realtime database."""

        account_history = [data for data in self.db_instance.FetchUpcomingTeacherConsultation(self.user_data['student_id']) if data['status'] == 'Accepted']

        if asc == "Ascending":
            account_history = sorted(account_history, key=lambda x: x["scheduled_on"])
        elif asc == "Descending":
            account_history = sorted(account_history, key=lambda x: x["scheduled_on"], reverse=True)
        elif asc == "Alphabetical":
            account_history = sorted(account_history, key=lambda x: x["teacher"])
        
        # if search is not empty, which is empty by default. Filter data to its value
        if query != "":
            query_data = [data for data in account_history if str(query).lower() in str(data['teacher']).lower()]
            if query_data is not None:
                account_history = query_data
                
        # Iteration to place dynamic data in the frame
        for idx in range(len(account_history)):


            # Main frame
            self._cache_frame[idx] = ctk.CTkFrame(master=self.ConListWrapper, fg_color="transparent", border_color="gray", border_width=2, corner_radius=5)
            self._cache_frame[idx].grid(row=idx, column=0, pady=10, padx=5, sticky="nsew")
            self._cache_frame[idx].grid_columnconfigure(3, weight=1)
            self._cache_frame[idx].grid_rowconfigure(2, weight=1)

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
            ctk.CTkLabel(master=self._cache_teacher_frame[idx], text=f"{account_history[idx]['prefix']}. {account_history[idx]['teacher']}", text_color=res.constants.THEME_TEXT, font=ctk.CTkFont(family=res.fonts.POPPINS, size=20, weight='bold')).grid(row=0, column=0, sticky="nsew")


            # timedelta lost my sanity. It is not even a timezone conversion wtf.
            session_start = dtf.ConvertTime(account_history[idx]['open_at'])
            session_end = dtf.ConvertTime(account_history[idx]['close_at'])
            formatted_time = f"{session_start} - {session_end}"

            # Inner TimeSpan in TeacherWrapper
            ctk.CTkLabel(master=self._cache_teacher_frame[idx], text=f"{formatted_time}", text_color=("black", "white"), font=ctk.CTkFont(family=res.fonts.POPPINS, size=12)).grid(row=1, column=0, sticky="w")
            # Inner TimeSpan in TeacherWrapper
            ctk.CTkLabel(master=self._cache_info_frame[idx], text=f"{account_history[idx]['task_name']}", text_color=("black", "white"), font=ctk.CTkFont(family=res.fonts.POPPINS, size=13, weight='bold')).grid(row=0, column=0, sticky="nsew")
            # Inner TimeSpan in TeacherWrapper
            ctk.CTkLabel(master=self._cache_info_frame[idx], text=f"    {account_history[idx]['status']}", text_color=("black", "white"), font=ctk.CTkFont(family=res.fonts.POPPINS, size=12)).grid(row=1, column=0, padx=30, sticky="w")
            # Button gg go next
            ctk.CTkButton(master=self._cache_frame[idx], command=lambda:self.master.SelectedPanel("history"),image=self.master.GoNextImage, text=None, fg_color="transparent", hover=None).grid(row=0, column=3, padx=5, pady=10, sticky="e")