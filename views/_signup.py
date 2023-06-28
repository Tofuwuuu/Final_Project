""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
import re
import base64
import models.resources as res
from models._cryptography import Security
from models.db_system import DBSystem
from views import init_app

ctk.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class SignUpFrame(ctk.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        # Title Label
        self.titleLabel = ctk.CTkLabel(self, text="Create an Account", font=("Roboto", 40, "bold"), text_color=("black", "#2B9348"))
        self.titleLabel.grid(rowspan=1, columnspan=5, padx=10, pady=20, sticky="nsew")

        # Name Label
        self.err_label = ctk.CTkLabel(self, text=None, text_color="red", font=("Roboto", 15))
        self.err_label.grid(row=2, columnspan=5, padx=5, pady=20, sticky="nsew")

        # Name Label
        self.firstNameLabel = ctk.CTkLabel(self, text="First Name", text_color=("black", "#2B9348"))
        self.firstNameLabel.grid(row=3, column=0, padx=10, pady=10)

        # Last Name Label
        self.lastNameLabel = ctk.CTkLabel(self, text="Last Name", text_color=("black", "#2B9348"))
        self.lastNameLabel.grid(row=3, column=2, padx=10, pady=10)

        # Username Label
        self.usernameLabel = ctk.CTkLabel(self, text="Username", text_color=("black", "#2B9348"))
        self.usernameLabel.grid(row=4, column=0, padx=10, pady=10)

        # Name Entry Field
        self.firstNameEntry = ctk.CTkEntry(self, placeholder_text="John")
        self.firstNameEntry.grid(row=3, column=1, padx=10, pady=10)

        # Email Label
        self.emailLabel = ctk.CTkLabel(self, text="Email", text_color=("black", "#2B9348"))
        self.emailLabel.grid(row=5, column=0, padx=10, pady=10)

        # Last Name Entry Field
        self.lastNameEntry = ctk.CTkEntry(self, placeholder_text="Doe")
        self.lastNameEntry.grid(row=3, column=3, padx=10, pady=10)

        # Password Label
        self.passwordLabel = ctk.CTkLabel(self, text="Password", text_color=("black", "#2B9348"))
        self.passwordLabel.grid(row=6, column=0, padx=10, pady=10)

        # Username Field
        self.usernameEntry = ctk.CTkEntry(self, placeholder_text="John Doe")
        self.usernameEntry.grid(row=4, column=1, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Confirm Password Label
        self.confirmPasswordLabel = ctk.CTkLabel(self, text="Confirm Password", text_color=("black", "#2B9348"))
        self.confirmPasswordLabel.grid(row=6, column=2, padx=10, pady=10)

        # Email Entry Field
        self.emailEntry = ctk.CTkEntry(self, placeholder_text="example@example.com")
        self.emailEntry.grid(row=5, column=1, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Password Entry Field
        self.passwordEntry = ctk.CTkEntry(self, show="*", placeholder_text="Password")
        self.passwordEntry.grid(row=6, column=1, padx=10, pady=10)

        # Confirm Password Entry Field
        self.confirmPasswordEntry = ctk.CTkEntry(self, show="*", placeholder_text="Confirm Password")
        self.confirmPasswordEntry.grid(row=6, column=3, padx=10, pady=10)

        # Confirm Button
        self.confirmButton = ctk.CTkButton(self, text="Confirm", command=self.confirm, bg_color=("#2B9348", "#2B9348"), fg_color=("#2B9348", "#2B9348"), hover=("#2B9348", "#2B9348"))
        self.confirmButton.grid(row=9, columnspan=4, padx=10, pady=50, sticky="nsew")
        
        #Sign Up Label
        self.SignUp = ctk.CTkButton(self, text="Already have an account? Login here.", command=self.ToLogin, fg_color="transparent", hover=False, text_color=("black", "#2B9348"), font=ctk.CTkFont(underline=True))
        self.SignUp.grid(row=10, columnspan=5, padx=5, pady=10, sticky="nsew")

    
    # Methods defined
    def ToLogin(self):
        self.destroy()
        _LogIn_frame = init_app.LogInFrame(master=init_app.init, fg_color="#Fdf0d5")
        _LogIn_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Frame Methods
    def confirm(self) -> None:

        # regex expression for email validation
        regex = re.compile(res.constants.REGEX_EMAIL)

        # Lambda expressions for simplified functions needed for this method
        format_str = lambda: (fname.title(), lname.title(), username.title())
        not_existing_username = lambda: True if not isinstance(self.master.db_instance.SearchUser(username), (dict, list)) else False
        valid_email = lambda: True if re.fullmatch(regex, email) else False
        not_existing_email = lambda: True if not isinstance(self.master.db_instance.SearchUser(email), (dict, list)) else False

        fname = self.firstNameEntry.get()
        lname = self.lastNameEntry.get()
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        cpass = self.confirmPasswordEntry.get()
        email = self.emailEntry.get().lower()

        # Format String Completion
        format_str()
        
        # Check if all fields are filled.
        not_Empty = (fname != '' and lname != '' and username != '' and password != '')
        password_Matched = (password == cpass)
        isValid_Email = (valid_email() and not_existing_email())
        isExisting_User = not_existing_username()
        valid_account = (not_Empty and isExisting_User and password_Matched and email != '' and isValid_Email)
        
        if not not_Empty:
            self.err_label.configure(text="Fields are empty.")
        elif not password_Matched:
            self.err_label.configure(text="Password fields do not match.")
        elif not isValid_Email:
            self.err_label.configure(text="Not a valid email address.")
        elif not isExisting_User:
            self.err_label.configure(text="Username already exists.")

        if valid_account:
            # Remove error label
            self.err_label.configure(text=None)

            # Password encryption algorithms defined in _cryptography.py
            password_hash = self.master.security.EncryptData(password)

            # Commit to the database
            self.master.db_instance.RegisterStudent(fname=fname, lname=lname, username=username, email=email, password=password_hash)

            # Redirecting to the login frame
            self.ToLogin()

