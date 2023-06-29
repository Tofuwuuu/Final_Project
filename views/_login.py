""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
from views import init_app
from views.teacher import teacher_app
from views.student import student_app
from PIL import Image

ctk.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

#Log In Frame class
class LogInFrame(ctk.CTkFrame):
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #File directory pathing for images
        
        image_path = "./resources/images/CvSU Consult Logo.png"
        self.logo_image = ctk.CTkImage(Image.open(image_path), size=(48, 48))

        #space 
        self.space1 = ctk.CTkLabel(self, text=None)
        self.space1.grid(row=0, column=0, padx=0, pady=2)

        #Create Header
        self.imgheader = ctk.CTkLabel(self, text=" ", image=self.logo_image)
        self.imgheader.place(x=75, y = 35)
        self.header = ctk.CTkLabel(self, text=" CvSU Consult ", text_color="#55A630", font=ctk.CTkFont('Roboto', 15, weight='bold'))
        self.header.grid(row=1, column=0, padx=140, pady=0, sticky="nw")
        self.header = ctk.CTkLabel(self, text="Carmona Campus", text_color="#55A630", font=('Roboto', 13))
        self.header.grid(row=3, column=0, padx=140, pady=0, sticky="nsew")

        #space
        self.space2 = ctk.CTkLabel(self, text=None)
        self.space2.grid(row=4, column=0, padx=0, pady=10)

        #Welcome Greeting
        self.welcomeg = ctk.CTkLabel(self, text="Welcome!", text_color="#2B9348", font=ctk.CTkFont('Roboto', 16, weight='bold'))
        self.welcomeg.grid(row=5, column=0, padx=55, pady=10, sticky="w")

        #Welcome Greeting
        self.err_label = ctk.CTkLabel(self, text=None, text_color="red", font=ctk.CTkFont('Roboto', 13))
        self.err_label.grid(row=6, column=0, padx=55, pady=0, sticky="w")
       
        #Email Label and Entry
        self.Email_lbl = ctk.CTkLabel(self, text="Email:", font=('Arial', 12))
        self.Email_lbl.grid(row=7, column=0, padx=55, pady=0, sticky="w")
        self.Email = ctk.CTkEntry(self, placeholder_text="Enter your Email", width=285)
        self.Email.grid(row=8, column=0, padx=10, pady=0)


        #Password Label and Entry
        self.Password_lbl = ctk.CTkLabel(self, text="Password:")
        self.Password_lbl.grid(row=9, column=0, padx=55, pady=0, sticky="w")
        self.Password = ctk.CTkEntry(self, placeholder_text="Enter your password", width= 285, show="*")
        self.Password.grid(row=10, column=0, padx=10, pady=0)

        #Forgot Password Label
        self.ForgotPass = ctk.CTkLabel(self, text="Forgot Password?", fg_color="transparent", text_color="black", font=ctk.CTkFont('Arial', 10, underline=True))
        self.ForgotPass.grid(row=11, column=0, padx=60, pady=0, sticky="e")
    

        #Remember Me CheckBox
        self.RememberMe = ctk.CTkCheckBox(self, text="Remember Me", checkbox_height=17, checkbox_width=17, border_width=2, corner_radius=1, hover_color="#2B9348")
        self.RememberMe.grid(row=12, column=0, padx=55, pady=0, sticky="w")
        
        #space 
        self.space3 = ctk.CTkLabel(self, text=" ")
        self.space3.grid(row=13, column=0, padx=0, pady=7)

        #Log In Button
        self.LogIn_btn = ctk.CTkButton(self, text="Log In", fg_color="#2B9348", hover_color="#55A630", command=self.ValidateUser)
        self.LogIn_btn.grid(row=14, column=0, padx=5, pady=5)
        
        #space 
        self.space3 = ctk.CTkLabel(self, text=" ")
        self.space3.grid(row=15, column=0, padx=0, pady=4)

        #Sign Up Label
        self.SignUp = ctk.CTkButton(self, text="Don't have an account? Sign Up here", command=self.ToSignUp, fg_color="transparent", hover=False, text_color="black", font=ctk.CTkFont(underline=True))
        self.SignUp.grid(row=16, column=0, padx=10, pady=15)

        #space 
        self.space3 = ctk.CTkLabel(self, text=None)
        self.space3.grid(row=17, column=0, padx=0, pady=1)
        
    # Frame Methods
    def ToSignUp(self) -> None:
        self.destroy()

        # New instance created because of the destroy() destroying the defined value of SignIn_frame in the init_app
        _signupframe = init_app.SignUpFrame(master=init_app.init, fg_color="#Fdf0d5")
        _signupframe.place(relx=0.5, rely=0.5, anchor="center")

    # Frame Methods
    def ToResetPass(self) -> None:
        self.destroy()
    
    # Validate if user email and password is the same as the query data.    
    def ValidateUser(self) -> None:
        # Instances used in this method block
        email = self.Email.get()
        password = self.Password.get()

        
        # Fetch user data from the database
        user_data = self.master.db_instance.SearchUser(email)

        if user_data is None:
            # Fixed: Implement proper error message handling (value of self.err_label is not set anywhere in this class)
            self.err_label.configure(text="Email address doesn't exist")
        else:
            # Decrypt and compare the user's password with the provided password
            db_password = self.master.db_instance.GetPassHash(user_data['pass_id'])
            decrypt_pass = self.master.security.DecryptData(db_password)

            if decrypt_pass == password:
                if user_data.get("student_id") is not None:

                    init_app.init.destroy()
                    student_app._dangerouslyInit(user_data=user_data)
                else:
                    init_app.init.destroy()
                    teacher_app._dangerouslyInit(user_data=user_data)
            else:
                self.err_label.configure(text="Username or password is incorrect.")