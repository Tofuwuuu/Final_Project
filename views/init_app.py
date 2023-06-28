""" Application Interface Module

This file is modified to run using a runner file defined in the run.py file.
If you wish to test this file change all import paths to its relative path.

Because this file imports are based on the run.py relative paths, you cannot run this file as a "__main__".


File definition:
init_app is the application interface for login/signup window before the user authenticate/register into the database.
"""


import customtkinter as ctk
from views._login import LogInFrame # Based on the run.py path, you cannot run this file alone.
from views._signup import SignUpFrame # Based on the run.py path, you cannot run this file alone.
from models.db_system import DBSystem
from models._cryptography import Security
import models.resources as res

ctk.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Initial frame class for each window
class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Database instance for initial app window
        self.db_instance = DBSystem()
        self.security = Security()

        #Configure Window
        self.geometry(f"{res.constants.WIN_SMALL_WIDTH}x{res.constants.WIN_SMALL_HEIGHT}")
        self.title("CvSU-Carmona Campus Consultation Scheduling System")
        self.iconbitmap(res.images.window_icon)
        self.configure(fg_color="white")

        #File directory pathing for images
        self.logo_image = ctk.CTkImage(res.fetch_image(res.images.login_bg), size=(1920, 1080))

        #Background Image
        self.bg = ctk.CTkLabel(self, text="", image=self.logo_image)  
        self.bg.place(relx=0.5, rely=0.5, anchor="center")

        #Configure Log In Frame. Login frame generated from the _login.py, _file.py means that it is a ctk frame.
        #screen_width = App.winfo_screenwidth()
        #window_width = App.winfo_width(self)
        #y = (window_width//2)
        self.LogIn_frame = LogInFrame(master=self, fg_color="#Fdf0d5", corner_radius=0)
        self.LogIn_frame.place(relx=0.5, rely=0.5, anchor="center")

        #Configure Log In Frame. Sign up frame generated from the _signup.py, _file.py means that it is a ctk frame.
        self.SignUp_frame = SignUpFrame(master=self, fg_color="#Fdf0d5")

init = App()
