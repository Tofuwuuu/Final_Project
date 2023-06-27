""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
import tkinter as tk
import models.resources as res
import models.datetimeformatter as dtf

class DashboardFrame(ctk.CTkFrame):


    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # user data defined by the master
        self.user_data = self.master.user_data

        # Instance of the database inherit from the master application window
        self.db_instance = self.master.db_instance

        # load images with light and dark mode image
        """ File directory pathing for images """
        self.FacultyImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.faculty_dark), dark_image=res.fetch_image(res.images.nav_ico.faculty_light), size=(80, 80))
        self.CalendarImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.calendar_dark), dark_image=res.fetch_image(res.images.nav_ico.calendar_light), size=(80, 80))
        self.SmallCalendarImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.calendar_dark), dark_image=res.fetch_image(res.images.nav_ico.calendar_light), size=(20, 20))
        self.ConsultationImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.consultation_dark), dark_image=res.fetch_image(res.images.nav_ico.consultation_light), size=(80, 80))
        self.NotifImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.notif_dark), dark_image=res.fetch_image(res.images.nav_ico.notif_light), size=(20, 20))
        self.AlertNotifImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.alert_notif_dark), dark_image=res.fetch_image(res.images.nav_ico.alert_notif_light), size=(20, 20))
        self.GoNextImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.go_next_dark), dark_image=res.fetch_image(res.images.nav_ico.go_next_light), size=(50, 50))
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


        # Dashboard wrapper for grouping the dashboard utilities
        self.DashWrapper = ctk.CTkFrame(master=self, fg_color="transparent")
        self.DashWrapper.grid(row=0, columnspan=1, padx=20, pady=10, ipady=10, sticky="nsew")
        self.DashWrapper.grid_columnconfigure(0, weight=1)

        # DashWrapper | Dashboard Welcome Message
        self.WelcomeLabel = ctk.CTkLabel(self.DashWrapper, text=f"Welcome, {self.user_data['username']}!", text_color=("#2B9348", "#Fdf0d5"), font=ctk.CTkFont(family="Poppins", size=24, weight='bold'))
        self.WelcomeLabel.grid(row=0, column=0, pady=20, padx=10, sticky="w")

        # DashWrapper | Notifications
        self.NotifIcon = ctk.CTkButton(self.DashWrapper, text=None, image=self.NotifImage, width=5, fg_color="transparent", hover_color=(self.THEME_YELLOW))
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
        self.FacultyDashWrapper = ctk.CTkFrame(self.InnerInnerDashWrapper, fg_color=(self.THEME_YELLOW), width=160, height=185, corner_radius=5)
        self.FacultyDashWrapper.grid(row=0, column=0, padx=20, pady=0)
        self.FacultyDashWrapper.grid_columnconfigure(0, weight=1)
        self.FacultyDashWrapper.grid_rowconfigure(3, weight=2)

        # Yet another inner wrapper for containing navigations
        self.CalendarDashWrapper = ctk.CTkFrame(self.InnerInnerDashWrapper, fg_color=self.THEME_YELLOW)
        self.CalendarDashWrapper.grid(row=0, column=1, padx=20, pady=0)
        self.CalendarDashWrapper.grid_columnconfigure(0, weight=1)
        self.CalendarDashWrapper.grid_rowconfigure(3, weight=2)

        # Yet another inner wrapper for containing navigations
        self.ConsultationDashWrapper = ctk.CTkFrame(self.InnerInnerDashWrapper, fg_color=self.THEME_YELLOW)
        self.ConsultationDashWrapper.grid(row=0, column=2, padx=20, pady=0)
        self.ConsultationDashWrapper.grid_columnconfigure(0, weight=1)
        self.ConsultationDashWrapper.grid_rowconfigure(3, weight=2)

        # Large Faculty Image
        self.FacultyDashImage = ctk.CTkLabel(self.FacultyDashWrapper, text=None, image=self.FacultyImage)
        self.FacultyDashImage.grid(row=0, column=0, padx=5, pady=10)
        # Faculty Label
        self.FacultyDashLabel = ctk.CTkLabel(self.FacultyDashWrapper, text="Faculty Schedule", font=ctk.CTkFont(size=13, weight='bold'), text_color=("#2B9348", "#Fdf0d5"))
        self.FacultyDashLabel.grid(row=1, column=0, padx=25, pady=0)
        # Faculty Label
        self.FacultyDashButton = ctk.CTkButton(self.FacultyDashWrapper, text="View All",command=lambda: self.master.SelectedPanel('faculty'), width=100, height=25, corner_radius=5, fg_color="#2B9348", hover_color="#55A630", font=ctk.CTkFont(size=12))
        self.FacultyDashButton.grid(row=2, column=0, padx=7, pady=10)

        # Large Calendar Image
        self.CalendarDashImage = ctk.CTkLabel(self.CalendarDashWrapper, text=None, image=self.CalendarImage)
        self.CalendarDashImage.grid(row=0, column=0, padx=5, pady=10)
        # Calendar Label
        self.CalendarDashLabel = ctk.CTkLabel(self.CalendarDashWrapper, text="Calendar History", font=ctk.CTkFont(size=13, weight='bold'), text_color=("#2B9348", "#Fdf0d5"))
        self.CalendarDashLabel.grid(row=1, column=0, padx=25, pady=0)
        # Calendar Button
        self.CalendarDashButton = ctk.CTkButton(self.CalendarDashWrapper, text="View All", command=lambda: self.master.SelectedPanel('faculty'), width=100, height=25, corner_radius=5, fg_color="#2B9348", hover_color="#55A630", font=ctk.CTkFont(size=12))
        self.CalendarDashButton.grid(row=2, column=0, padx=7, pady=10)

        # Large Consultation Image
        self.ConsultationDashImage = ctk.CTkLabel(self.ConsultationDashWrapper, text=None, image=self.ConsultationImage)
        self.ConsultationDashImage.grid(row=0, column=0, padx=5, pady=10)
        # Consultation Label
        self.ConsultationDashLabel = ctk.CTkLabel(self.ConsultationDashWrapper, text="My Consultations", font=ctk.CTkFont(size=13, weight='bold'), text_color=("#2B9348", "#Fdf0d5"))
        self.ConsultationDashLabel.grid(row=1, column=0, padx=25, pady=0)
        # Consultation Button
        self.ConsultationDashButton = ctk.CTkButton(self.ConsultationDashWrapper, text="View All", command=lambda: self.master.SelectedPanel('faculty'), width=100, height=25, corner_radius=5, fg_color="#2B9348", hover_color="#55A630", font=ctk.CTkFont(size=12))
        self.ConsultationDashButton.grid(row=2, column=0, padx=7, pady=10)

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
        self.UpcomingConsultationsLabel = ctk.CTkLabel(self.ConWrapper, text="Upcoming Consultations", text_color=("#2B9348", "#Fdf0d5"), font=ctk.CTkFont(family="Poppins", size=20, weight='bold'))
        self.UpcomingConsultationsLabel.grid(row=0, column=0, pady=20, padx=20, sticky="w")

        # ConWrapper | View Details Label
        self.ViewDetailsButton = ctk.CTkButton(self.ConWrapper, fg_color="transparent", bg_color="transparent",text="View Details", text_color="gray", font=ctk.CTkFont(family="Poppins", size=13, underline=True), command=lambda: self.master.SelectedPanel("consultation"), hover=None)
        self.ViewDetailsButton.grid(row=0, column=1, pady=20, padx=50, sticky="w")


    def UpdateUpcoming(self) -> None:
        
        """ Reference
        Update upcoming consultation based on realtime database."""

        account_history = self.db_instance.FetchUpcomingConsultations(self.user_data['account_id'])

        _cache_frame = []
        _cache_inner_frame = []
        _cache_teacher_frame = []
        _cache_info_frame = []

        # Upcoming account consultation denoted by ("Pending", "Accepted") on column "status"
        upcoming_data = sorted([data for data in account_history if data['status'] == 'Accepted'], key=lambda data: data['scheduled_on'])
        
        

        # Iteration to place dynamic data in the frame
        for idx in range(len(upcoming_data)):
            
            # Initializing cache variables
            _cache_frame.append("_cache_frame_".join(str(idx)))
            _cache_inner_frame.append("_cache_inner_frame_".join(str(idx)))
            _cache_teacher_frame.append("_cache_teacher_frame_".join(str(idx)))
            _cache_info_frame.append("_cache_info_frame_".join(str(idx)))

            # Main frame
            _cache_frame[idx] = ctk.CTkFrame(master=self.ConListWrapper, fg_color="transparent", border_color="gray", border_width=2, corner_radius=5)
            _cache_frame[idx].grid(row=idx, column=0, pady=10, padx=5, sticky="nsew")
            _cache_frame[idx].grid_columnconfigure(3, weight=1)
            _cache_frame[idx].grid_rowconfigure(2, weight=1)

            # Inner frame for date
            _cache_inner_frame[idx] = ctk.CTkFrame(master=_cache_frame[idx], fg_color=self.THEME_BLUE, corner_radius=5)
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
            ctk.CTkLabel(master=_cache_inner_frame[idx], text=f"{upcoming_data[idx]['scheduled_on'].strftime('%d')}", text_color=("#2B9348", "#Fdf0d5"), font=ctk.CTkFont(family="Poppins", size=20, weight='bold')).grid(row=0, column=0, padx=30, sticky="nsew")
            # Inner Month
            ctk.CTkLabel(master=_cache_inner_frame[idx], text=f"{upcoming_data[idx]['scheduled_on'].strftime('%B')[0:3]}", text_color=("#2B9348", "#Fdf0d5"), font=ctk.CTkFont(family="Poppins", size=18, weight='bold')).grid(row=1, column=0, sticky="nsew")
            #Inner Teacher Text
            ctk.CTkLabel(master=_cache_teacher_frame[idx], text=f"{upcoming_data[idx]['teacher']}", text_color=("#2B9348", "#Fdf0d5"), font=ctk.CTkFont(family="Poppins", size=20, weight='bold')).grid(row=0, column=0, sticky="nsew")


            # timedelta lost my sanity. It is not even a timezone conversion wtf.
            session_start = dtf.ConvertTime(upcoming_data[idx]['open_at'])
            session_end = dtf.ConvertTime(upcoming_data[idx]['close_at'])
            formatted_time = f"{session_start} - {session_end}"

            # Inner TimeSpan in TeacherWrapper
            ctk.CTkLabel(master=_cache_teacher_frame[idx], text=f"{formatted_time}", text_color=("black", "white"), font=ctk.CTkFont(family="Poppins", size=12)).grid(row=1, column=0, sticky="w")
            # Inner TimeSpan in TeacherWrapper
            ctk.CTkLabel(master=_cache_info_frame[idx], text=f"{upcoming_data[idx]['task_name']}", text_color=("black", "white"), font=ctk.CTkFont(family="Poppins", size=13, weight='bold')).grid(row=0, column=0, sticky="nsew")
            # Inner TimeSpan in TeacherWrapper
            ctk.CTkLabel(master=_cache_info_frame[idx], text=f"    {upcoming_data[idx]['status']}", text_color=("black", "white"), font=ctk.CTkFont(family="Poppins", size=12)).grid(row=1, column=0, padx=30, sticky="w")
            # Button gg go next
            ctk.CTkButton(master=_cache_frame[idx], command=lambda:self.master.SelectedPanel("consultation"),image=self.GoNextImage, text=None, fg_color="transparent", hover=None).grid(row=0, column=3, padx=5, pady=10, sticky="e")