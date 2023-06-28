""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
import models.resources as res
import models.datetimeformatter as dtf
from threading import Thread

class RequestFrame(ctk.CTkFrame):


    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # user data defined by the master
        self.user_data = self.master.user_data

        # Cache frames
        self._cache_frame = {}
        self._cache_inner_frame = {}
        self._cache_teacher_frame = {}
        self._cache_info_frame = {}

        # Instance of the database inherit from the master application window
        self.db_instance = self.master.db_instance

        # load images with light and dark mode image
        """ File directory pathing for images """
        self.CalendarImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.calendar_dark), dark_image=res.fetch_image(res.images.nav_ico.calendar_light), size=(20, 20))
        self.NotifImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.notif_dark), dark_image=res.fetch_image(res.images.nav_ico.notif_light), size=(20, 20))
        self.AlertNotifImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.alert_notif_dark), dark_image=res.fetch_image(res.images.nav_ico.alert_notif_light), size=(20, 20))
        self.SearchImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.search_light), dark_image=res.fetch_image(res.images.nav_ico.search_dark), size=(20, 20))
        self.SortImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.sort_light), dark_image=res.fetch_image(res.images.nav_ico.sort_dark), size=(20, 20))
        self.FilterImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.filter_light), dark_image=res.fetch_image(res.images.nav_ico.filter_dark), size=(20, 20))
        self.AcceptImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.check_dark), dark_image=res.fetch_image(res.images.nav_ico.check_light), size=(20, 20))
        self.DenyImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.deny_dark), dark_image=res.fetch_image(res.images.nav_ico.deny_light), size=(20, 20))
        self.PendingImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.pending_dark), dark_image=res.fetch_image(res.images.nav_ico.pending_light), size=(20, 20))
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


        # Dashboard wrapper for grouping the dashboard utilities
        self.DashWrapper = ctk.CTkFrame(master=self, fg_color="transparent")
        self.DashWrapper.grid(row=0, columnspan=1, padx=20, pady=10, ipady=10, sticky="nsew")
        self.DashWrapper.grid_columnconfigure(0, weight=1)

        # DashWrapper | Dashboard Welcome Message
        self.WelcomeLabel = ctk.CTkLabel(self.DashWrapper, text=f"Welcome, {self.user_data['username']}!", text_color=("#2B9348", "#Fdf0d5"), font=ctk.CTkFont(family="Poppins", size=24, weight='bold'))
        self.WelcomeLabel.grid(row=0, column=0, pady=20, padx=10, sticky="w")

        # DashWrapper | Calendar Icon
        self.CalendarIcon = ctk.CTkButton(self.DashWrapper, text=None, image=self.CalendarImage, width=5, fg_color="transparent", hover_color=(self.THEME_YELLOW))
        self.CalendarIcon.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # DashWrapper | Notifications
        self.NotifIcon = ctk.CTkButton(self.DashWrapper, text=None, image=self.NotifImage, width=5, fg_color="transparent", hover_color=(self.THEME_YELLOW))
        self.NotifIcon.grid(row=0, column=2, padx=10, pady=10, sticky="e")

        # Upcoming Consultation wrapper for grouping the dashboard utilities
        self.ConWrapper = ctk.CTkFrame(master=self, fg_color="transparent")
        self.ConWrapper.grid(row=1, columnspan=1, padx=20, pady=5, ipady=10, sticky="nsew")
        self.ConWrapper.grid_columnconfigure(0, weight=1)
        self.ConWrapper.grid_rowconfigure(1, weight=1)
        
        # Upcoming Consultation List Wrapper
        self.ConListWrapper = ctk.CTkScrollableFrame(master=self.ConWrapper, fg_color="transparent")
        self.ConListWrapper.grid(row=1, column=0, padx=20, pady=10, ipady=10, sticky="nsew")
        self.ConListWrapper.grid_columnconfigure(0, weight=1)

        # Upcoming Consultation Info Wrapper
        self.ConInfoWrapper = ctk.CTkFrame(master=self.ConWrapper, fg_color="transparent")
        self.ConInfoWrapper.grid(row=1, column=1, padx=20, pady=10, ipady=10, sticky="nsew")
        self.ConInfoWrapper.grid_columnconfigure(0, weight=1)
        self.ConInfoWrapper.grid_rowconfigure(0, weight=1)

        # ConWrapper | Upcoming Consultations Label
        self.UpcomingConsultationsLabel = ctk.CTkLabel(self.ConWrapper, text="Upcoming schedule today", text_color=("#2B9348", "#Fdf0d5"), font=ctk.CTkFont(family="Poppins", size=20, weight='bold'))
        self.UpcomingConsultationsLabel.grid(row=0, column=0, pady=20, padx=20, sticky="w")

        self.SearchUtilityWrapper = ctk.CTkFrame(master=self.ConWrapper, fg_color="transparent")
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
        self.Sort = ctk.CTkComboBox(master=self.SearchUtilityWrapper,command=lambda sort: self.UpdateRequest(sort), values=["Ascending", "Descending"], variable=self.SortVariable, height=30, text_color=("#242424", 'white'), font=ctk.CTkFont(family="Poppins", size=11), dropdown_fg_color=self.THEME_YELLOW, fg_color=self.DEFAULT, border_color=self.THEME_GREEN, border_width=2, corner_radius=5, button_hover_color="#55A630", button_color=self.THEME_GREEN)
        self.Sort.grid(row=1, column=0, sticky="w")

    def ForgetAll(self):
        # Forget every grid
        for _ in map(lambda x: self._cache_frame[x].grid_forget(), list(self._cache_frame.keys())):
            pass
        for _ in map(lambda x: self._cache_inner_frame[x].grid_forget(), list(self._cache_inner_frame.keys())):
            pass
        for _ in map(lambda x: self._cache_teacher_frame[x].grid_forget(), list(self._cache_teacher_frame.keys())):
            pass
        for _ in map(lambda x: self._cache_info_frame[x].grid_forget(), list(self._cache_info_frame.keys())):
            pass

        # Forget current index widget
        self._cache_frame.clear()
        self._cache_inner_frame.clear()
        self._cache_teacher_frame.clear()
        self._cache_info_frame.clear()

    def UpdateStatus(self, history_id: int, schedule_id: int, status: str) -> None:
        try:
            
            schedule_data = [dat for  dat in self.db_instance.FetchRequestHistory(self.user_data['teacher_id']) if dat['schedule_id'] == schedule_id and dat['history_id'] == history_id]
            if status == 'Accepted':
                if schedule_data[0]['schedule_status'] == 'Open':
                    self.db_instance.AcceptRequestOnDB(schedule_id=schedule_id, history_id=history_id)
                    self.ForgetAll()

            elif status == 'Denied':
                if schedule_data[0]['request_status'] != 'Rejected':
                    self.db_instance.DenyRequestOnDB(history_id=history_id)
                    self.ForgetAll()

        except ValueError as var:
            print(f"Error: {var}")
        finally:
            self.UpdateRequest()


    def UpdateRequest(self, asc: str = "Ascending") -> None:
        
        """ Reference
        Update incoming consultation request based on realtime database."""

        account_history = [data for data in self.db_instance.FetchRequestHistory(self.user_data['teacher_id']) if data['request_status'] == 'Pending' and data['schedule_status'] == 'Open']
        if asc == "Ascending" and account_history:
            account_history = sorted(account_history, key=lambda x: x["scheduled_on"])
        elif asc == "Descending" and account_history:
            account_history = sorted(account_history, key=lambda x: x["scheduled_on"], reverse=True)

        # Iteration to place dynamic data in the frame
        for idx in range(len(account_history)):

            # Main frame
            self._cache_frame[idx] = ctk.CTkFrame(master=self.ConListWrapper, fg_color="transparent", border_color="gray", border_width=2, corner_radius=5)
            self._cache_frame[idx].grid(row=idx, column=0, pady=10, padx=5, sticky="nsew")
            self._cache_frame[idx].grid_columnconfigure(3, weight=1)
            self._cache_frame[idx].grid_rowconfigure(3, weight=1)

            # Inner frame for date
            self._cache_inner_frame[idx] = ctk.CTkFrame(master=self._cache_frame[idx], fg_color=self.THEME_BLUE, corner_radius=5)
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
            ctk.CTkLabel(master=self._cache_inner_frame[idx], text=f"{account_history[idx]['scheduled_on'].strftime('%d')}", text_color=("#2B9348", "#Fdf0d5"), font=ctk.CTkFont(family="Poppins", size=20, weight='bold')).grid(row=0, column=0, padx=30, sticky="nsew")
            # Inner Month
            ctk.CTkLabel(master=self._cache_inner_frame[idx], text=f"{account_history[idx]['scheduled_on'].strftime('%B')[0:3]}", text_color=("#2B9348", "#Fdf0d5"), font=ctk.CTkFont(family="Poppins", size=18, weight='bold')).grid(row=1, column=0, sticky="nsew")
            #Inner Teacher Text
            ctk.CTkLabel(master=self._cache_teacher_frame[idx], text=f"{account_history[idx]['student']}", text_color=("#2B9348", "#Fdf0d5"), font=ctk.CTkFont(family="Poppins", size=20, weight='bold')).grid(row=0, column=0, sticky="nsew")


            # timedelta lost my sanity. It is not even a timezone conversion wtf.
            session_start = dtf.ConvertTime(account_history[idx]['open_at'])
            session_end = dtf.ConvertTime(account_history[idx]['close_at'])
            formatted_time = f"{session_start} - {session_end}"

            # Inner TimeSpan in TeacherWrapper
            ctk.CTkLabel(master=self._cache_teacher_frame[idx], text=f"Requested Time: {formatted_time}", text_color=("black", "white"), font=ctk.CTkFont(family="Poppins", size=12)).grid(row=1, column=0, sticky="w")
            # Inner TimeSpan in TeacherWrapper
            ctk.CTkLabel(master=self._cache_info_frame[idx], text=f"{account_history[idx]['task_name']}", text_color=("black", "white"), font=ctk.CTkFont(family="Poppins", size=14)).grid(row=0, column=0, padx=10, sticky="w")

            # Button gg go next
            ctk.CTkButton(master=self._cache_frame[idx], command=lambda key=idx: self.UpdateStatus(schedule_id=account_history[key]['schedule_id'], history_id=account_history[key]['history_id'], status='Accepted'),image=self.AcceptImage, text="Accept", fg_color="green", hover=None).grid(row=0, column=4, padx=5, pady=10, sticky="e")
            # Button gg go next
            ctk.CTkButton(master=self._cache_frame[idx], command=lambda key=idx: self.UpdateStatus(schedule_id=account_history[key]['schedule_id'], history_id=account_history[key]['history_id'], status='Denied'),image=self.DenyImage, text="Decline", fg_color="red", hover=None).grid(row=0, column=5, padx=5, pady=10, sticky="e")

            # Button gg go next
            ctk.CTkLabel(master=self._cache_frame[idx], image=self.PendingImage, text=None, fg_color="transparent", font=ctk.CTkFont(family="Poppins", size=15)).grid(row=0, column=6, padx=10, pady=10, sticky="esn")