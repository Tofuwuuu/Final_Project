""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
import models.resources as res
from views import init_app
from tkinter import messagebox

class ChangePasswordFrame(ctk.CTkFrame):




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        """ File directory pathing for images """
        self.BackImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.back_dark), dark_image=res.fetch_image(res.images.nav_ico.back_light), size=(20, 20))
        """ End of resource pathing """

        # Styling as row-stretch
        self.grid_columnconfigure(0, weight=5)
        self.grid_rowconfigure(1, weight=1)

        # TitleWrapper for grouping the title bars
        self.TitleWrapper = ctk.CTkFrame(master=self, fg_color="transparent")
        self.TitleWrapper.grid(row=0, columnspan=1, padx=20, pady=10, ipady=10, sticky="nsew")
        self.TitleWrapper.grid_columnconfigure(0, weight=1)

        # TitleWrapper | Back Button
        self.BackButton = ctk.CTkButton(self.TitleWrapper, text=" ", image=self.BackImage, hover=None, fg_color="transparent", command=self.ExitFrame)
        self.BackButton.grid(row=0, column=0, pady=15, padx=100, sticky="w")

        # TitleWrapper | TitleWrapper Welcome Message
        self.TitleLabel = ctk.CTkLabel(self.TitleWrapper, text=f"Change Your Password", text_color=res.constants.THEME_TEXT, font=ctk.CTkFont(family=res.fonts.POPPINS, size=20, weight='bold'))
        self.TitleLabel.grid(row=1, column=0, pady=0, padx=100, sticky="w")

        # MainWrapper
        self.MainWrapper = ctk.CTkFrame(master=self, fg_color=res.constants.THEME_GREEN)
        self.MainWrapper.grid(row=1, columnspan=1, padx=20, pady=10, sticky="nsew")
        self.MainWrapper.grid_columnconfigure(0, weight=1)


        # Email Label
        self.EmailLabel = ctk.CTkLabel(self.MainWrapper, text=f"Email", text_color=res.constants.THEME_TEXT, font=ctk.CTkFont(family=res.fonts.POPPINS, size=13, weight='bold'))
        self.EmailLabel.grid(row=0, column=0, pady=20, padx=15, sticky="w")

        # Email Entry
        self.EmailEntry = ctk.CTkEntry(master=self.MainWrapper, placeholder_text="Enter your Email")
        self.EmailEntry.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        # New Password Label
        self.NewPasswordLabel = ctk.CTkLabel(self.MainWrapper, text=f"New Password", text_color=res.constants.THEME_TEXT, font=ctk.CTkFont(family=res.fonts.POPPINS, size=13, weight='bold'))
        self.NewPasswordLabel.grid(row=2, column=0, pady=20, padx=20, sticky="w")

        # Enter New Password Entry
        self.NewPasswordEntry = ctk.CTkEntry(master=self.MainWrapper, placeholder_text="Enter your new password", show="*")
        self.NewPasswordEntry.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

        # Confirm Password Label
        self.ConfirmPasswordLabel = ctk.CTkLabel(self.MainWrapper, text=f"Confirm Password", text_color=res.constants.THEME_TEXT, font=ctk.CTkFont(family=res.fonts.POPPINS, size=13, weight='bold'))
        self.ConfirmPasswordLabel.grid(row=4, column=0, pady=20, padx=20, sticky="w")

        # Enter Confirm Password Entry
        self.ConfirmPasswordEntry = ctk.CTkEntry(master=self.MainWrapper, placeholder_text="Confirm your Password", show="*")
        self.ConfirmPasswordEntry.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

        #space 
        self.space1 = ctk.CTkLabel(self, text=None)
        self.space1.grid(row=6, column=0, padx=0, pady=2)

        # Submit Button
        self.SubmitButton = ctk.CTkButton(master=self.MainWrapper, command=self.ValidateUser, text=" Submit ")
        self.SubmitButton.grid(row=7, column=0, padx=5, pady=5)

    # Validate if user email 
    def ValidateUser(self) -> None:
        # Instances used in this method block
        email = self.EmailEntry.get()
        password = self.NewPasswordEntry.get()
                
        # Fetch user data from the database
        user_data = self.master.db_instance.SearchUser(email)

        if user_data is None:
            messagebox.showerror('Error', 'Email not found. Please create an account.')


        else:
            if self.EmailEntry.get() == '':
                messagebox.showwarning('Warning', 'Please input your email')
            elif self.NewPasswordEntry.get() == '':
                messagebox.showwarning('Warning', 'Please input your new password')
            elif self.ConfirmPasswordEntry.get() == '':
                messagebox.showwarning('Warning', 'Please input again your new password')
            elif self.NewPasswordEntry.get() != self.ConfirmPasswordEntry.get():
                messagebox.showerror('Error', 'The passwords do not match.')
            else:
                # Redirecting to the login frame
                self.ExitFrame()


    def ExitFrame(self) -> None:
        self.destroy()

        _LogIn_frame = init_app.LogInFrame(master=init_app.init, fg_color="#Fdf0d5")
        _LogIn_frame.place(relx=0.5, rely=0.5, anchor="center")