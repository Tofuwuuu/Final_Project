""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
"""

import customtkinter as ctk
from ._dashboard import DashboardFrame
from ._faculty import FacultyFrame
from ._calendar import CalendarFrame
from ._history import HistoryFrame
from ._create import CreationFrame
from models.db_system import DBSystem
from .. import init_app
import models.resources as res

ctk.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class StudentApp(ctk.CTk):

    selected_panel = ""
    
    def __init__(self, user_data: list):
      
        super().__init__()

        self.db_instance = DBSystem()
        self.isMinimized = False
        # What is going on?
        self.user_data = user_data

        """ File directory pathing for images """
        # Large image
        self.FacultyImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.faculty_dark), dark_image=res.fetch_image(res.images.nav_ico.faculty_light), size=(80, 80))
        self.CalendarImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.calendar_dark), dark_image=res.fetch_image(res.images.nav_ico.calendar_light), size=(80, 80))
        self.GoNextImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.go_next_dark), dark_image=res.fetch_image(res.images.nav_ico.go_next_light), size=(50, 50))
        self.ConsultationImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.consultation_dark), dark_image=res.fetch_image(res.images.nav_ico.consultation_light), size=(80, 80))
        self.UserProfileImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.user_profile_dark), dark_image=res.fetch_image(res.images.nav_ico.user_profile_light), size=(50, 50))
        
        # Below Size 50x50; For icons
        self.LogoImage = ctk.CTkImage(res.fetch_image(res.images.cvsu_consult_logo), size=(30, 30))
        self.HomeImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.home_dark), dark_image=res.fetch_image(res.images.nav_ico.home_light), size=(20, 20))
        self.SmallCalendarImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.calendar_dark), dark_image=res.fetch_image(res.images.nav_ico.calendar_light), size=(20, 20))
        self.SmallFacultyImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.faculty_dark), dark_image=res.fetch_image(res.images.nav_ico.faculty_light), size=(20, 20))
        self.HistoryImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.history_dark), dark_image=res.fetch_image(res.images.nav_ico.history_light), size=(20, 20))
        self.NotifImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.notif_dark), dark_image=res.fetch_image(res.images.nav_ico.notif_light), size=(20, 20))
        self.AlertNotifImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.alert_notif_dark), dark_image=res.fetch_image(res.images.nav_ico.alert_notif_light), size=(20, 20))
        self.SearchImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.search_light), dark_image=res.fetch_image(res.images.nav_ico.search_dark), size=(20, 20))
        self.SortImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.sort_light), dark_image=res.fetch_image(res.images.nav_ico.sort_dark), size=(20, 20))
        self.FilterImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.filter_light), dark_image=res.fetch_image(res.images.nav_ico.filter_dark), size=(20, 20))
        self.MenuSliderImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.menu_dark), dark_image=res.fetch_image(res.images.nav_ico.menu_light), size=(20, 20))
        self.CreateImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.add_dark), dark_image=res.fetch_image(res.images.nav_ico.add_light), size=(20, 20))
        self.LogoutImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.logout_dark), dark_image=res.fetch_image(res.images.nav_ico.logout_light), size=(20, 20))
        """ End of resource pathing """

        # Window Configurations
        self.geometry(f"{res.constants.WIN_WIDTH}x{res.constants.WIN_HEIGHT}")
        self.title(f"CvSU Consult - Welcome, back teacher.")
        self.iconbitmap(res.images.window_icon)

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Slide Panel | Navigation - Implementation and Configurations
        self.SlidePanel = ctk.CTkFrame(self, corner_radius=0, fg_color= res.constants.THEME_GREEN)
        self.SlidePanel.grid(row=0, column=0, sticky="nsw")
        self.SlidePanel.grid_rowconfigure(7, weight=1)
        self.SlidePanel.grid_columnconfigure(1, weight=1)

        # Slide Panel | Burger as Label
        self.BurgerBtn = ctk.CTkButton(self.SlidePanel, text=None, image=self.MenuSliderImage, fg_color=res.constants.THEME_GREEN, width=3, bg_color=res.constants.THEME_GREEN, command=lambda: self.ToggleBurgerMenu())
        self.BurgerBtn.grid(row=0, column=0, sticky="e")

        # Slide Panel | Title as Label

        self.SlidePanelTitle = ctk.CTkLabel(self.SlidePanel, width=10, text=" CvSU Consult ", image=self.LogoImage, compound="left", font=ctk.CTkFont(size=15, weight="bold"))
        self.SlidePanelTitle.grid(row=1, column=0, padx=20, pady=20, sticky="nw")

        # Slide panel | Dashboard/Home Button
        self.ToDashboard = ctk.CTkButton(self.SlidePanel, corner_radius=0, width=10, height=40, border_spacing=10, text="Dashboard", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=res.constants.THEME_GRAY, image=self.HomeImage, anchor="w", command=lambda: self.SelectedPanel("dashboard"))
        self.ToDashboard.grid(row=2, column=0, sticky="ew")
        
        # Slide panel | Faculty Member Button
        self.ToFaculty = ctk.CTkButton(self.SlidePanel, corner_radius=0, width=10, height=40, border_spacing=10, text="Faculty Schedules", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=res.constants.THEME_GRAY, image=self.SmallFacultyImage, anchor="w", command=lambda: self.SelectedPanel("faculty"))
        self.ToFaculty.grid(row=3, column=0, sticky="ew")

        # Slide panel | Calendar Button
        self.ToCalendar = ctk.CTkButton(self.SlidePanel, corner_radius=0, width=10, height=40, border_spacing=10, text="Calendar", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=res.constants.THEME_GRAY, image=self.SmallCalendarImage, anchor="w", command=lambda: self.SelectedPanel("calendar"))
        self.ToCalendar.grid(row=4, column=0, sticky="ew")

        # Slide panel | historys Button
        self.ToHistory = ctk.CTkButton(self.SlidePanel, corner_radius=0, width=10, height=40, border_spacing=10, text="My historys", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=res.constants.THEME_GRAY, image=self.HistoryImage, anchor="w", command=lambda: self.SelectedPanel("history"))
        self.ToHistory.grid(row=5, column=0, sticky="ew")

        # Slide panel | Creation Button
        self.ToCreation = ctk.CTkButton(self.SlidePanel, corner_radius=0, width=10, height=40, border_spacing=10, text="Create history", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=res.constants.THEME_GRAY, image=self.CreateImage, anchor="w", command=lambda: self.SelectedPanel("creation"))
        self.ToCreation.grid(row=6, column=0, sticky="ew")

        # Slide panel | Theme Dropdown
        self.ThemeMode = ctk.CTkOptionMenu(self.SlidePanel, values=["Light", "Dark"], command=lambda mode: ctk.set_appearance_mode(mode), fg_color=res.constants.THEME_DARKGREEN, dropdown_fg_color=res.constants.THEME_DARKGREEN, button_color=res.constants.THEME_DARKGREEN, button_hover_color=res.constants.THEME_DARKGREEN, text_color=("black", "white"))
        self.ThemeMode.grid(row=7, column=0, padx=5, pady=5, sticky="s")

        # Slide panel | Logout Button

        self.Logout = ctk.CTkButton(self.SlidePanel, image=self.LogoutImage, width=10, corner_radius=0, height=10, border_spacing=10, text="Logout", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=res.constants.THEME_GRAY, anchor="w", command=lambda: self.logout_handler())
        self.Logout.grid(row=8, column=0, pady=5, padx=5, sticky="s")

        # Dashboard | Home Panel - Implementation and Configurations on ./_dashboard.py
        self.DashboardPanel = DashboardFrame(master=self, corner_radius=0, fg_color=res.constants.THEME_DEFAULT)
        # Faculty | Faculty Schedule Panel - Implementation and Configurations on ./_faculty.py
        self.FacultyPanel = FacultyFrame(master=self, corner_radius=0, fg_color=res.constants.THEME_DEFAULT)
        # Calendar | Calendar Panel - Implementation and Configurations on ./_calendar.py
        self.CalendarPanel = CalendarFrame(master=self, corner_radius=0, fg_color=res.constants.THEME_DEFAULT)
        # history | history Panel - Implementation and Configurations on ./_history.py
        self.HistoryPanel = HistoryFrame(master=self, corner_radius=0, fg_color=res.constants.THEME_DEFAULT)
        # Creation | Creation Panel - Implementation and Configurations on ./_Creation.py
        self.CreationPanel = CreationFrame(master=self, corner_radius=0, fg_color=res.constants.THEME_DEFAULT)

        # Default Window Frame on load
        self.SelectedPanel("dashboard")

    #There's probably no proper way to achieve this in python
    def ToggleBurgerMenu(self):
        if(self.isMinimized):
            self.BurgerBtn.grid(row=0, column=0, sticky="e")
            self.SlidePanelTitle.configure(text=" CvSU Consult ", anchor="center")
            self.ToDashboard.configure(text="Dashboard", anchor="w")
            self.ToFaculty.configure(text="Faculty Schedules", anchor="w")
            self.ToCalendar.configure(text="Calendar", anchor="w")
            self.ToHistory.configure(text="My history", anchor="w")
            self.ToCreation.configure(text="Create historys", anchor="w")
            self.Logout.configure(text="Logout", anchor="w")
            self.Logout.grid(row=8, column=0, pady=5, padx=5, sticky="s")

            self.ThemeMode.configure(values=["Light", "Dark"])
            self.ThemeMode.grid(row=7, column=0, padx=5, pady=5, sticky="s")
            self.isMinimized = False
        else:
            self.BurgerBtn.grid(row=0, column=0, sticky="ew")
            self.SlidePanelTitle.configure(text="", anchor="center")
            self.ToDashboard.configure(text=None, anchor="center")
            self.ToFaculty.configure(text=None, anchor="center")
            self.ToCalendar.configure(text=None, anchor="center")
            self.ToHistory.configure(text=None, anchor="center")
            self.ToCreation.configure(text=None, anchor="center")
            self.Logout.configure(text=None, anchor="center")

            self.ThemeMode.configure(values=[])
            self.ThemeMode.grid_forget()
            self.isMinimized = True


    def logout_handler(self):
        self.destroy()
        init_app.init = init_app.App()
        init_app.init.mainloop()

    # method for changing panel views
    def SelectedPanel(self, name) -> None:

        # Clean selected frame on call
        frames = [self.ToDashboard, self.ToFaculty, self.ToCalendar, self.ToHistory, self.ToCreation]
        for f in frames:
            f.configure(fg_color="transparent")

        # Display selected frame
        if name == "dashboard":
            if self.selected_panel != name:
                # Display
                self.DashboardPanel.grid(row=0, column=1, sticky="nsew")
                self.DashboardPanel.UpdateUpcoming()
                # Show as "selected button"
                self.ToDashboard.configure(fg_color=res.constants.THEME_GRAY)
                
                self.selected_panel = name
            else:
                pass
        else:
            self.DashboardPanel.grid_forget()

        if name == "faculty":
            if self.selected_panel != name:
                # Display
                self.FacultyPanel.grid(row=0, column=1, sticky="nsew")
                self.FacultyPanel.DisplayFaculty()
                # Show as "selected button"
                self.ToFaculty.configure(fg_color=res.constants.THEME_GRAY)
                self.selected_panel = name
            else:
                pass
        else:
            self.FacultyPanel.grid_forget()

        if name == "calendar":
            if self.selected_panel != name:
                # Display
                self.CalendarPanel.grid(row=0, column=1, sticky="nsew")
                # Show as "selected button"
                self.ToCalendar.configure(fg_color=res.constants.THEME_GRAY)
                self.selected_panel = name
            else:
                pass
            
        else:
            self.CalendarPanel.grid_forget()

        if name == "history":
            if self.selected_panel != name:
                # Display
                self.HistoryPanel.grid(row=0, column=1, sticky="nsew")
                self.HistoryPanel.UpdateHistory()
                # Show as "selected button"\
                self.ToHistory.configure(fg_color=res.constants.THEME_GRAY)
                self.selected_panel = name
            else:
                pass
        else:
            self.HistoryPanel.grid_forget()

        if name == "creation":
            if self.selected_panel != name:
                # Display
                self.CreationPanel.grid(row=0, column=1, sticky="nsew")
                self.CreationPanel.UpdateOpenFaculty()
                # Show as "selected button"
                self.ToCreation.configure(fg_color=res.constants.THEME_GRAY)
                self.selected_panel = name
            else:
                pass
        else:
            self.CreationPanel.grid_forget()


# This is used to initialize the student application window in the login method -> ValidateUser
def _dangerouslyInit(user_data: list) -> None:
    app = StudentApp(user_data=user_data)
    app.mainloop()
