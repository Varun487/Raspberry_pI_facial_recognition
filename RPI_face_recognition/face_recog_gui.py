import tkinter as tk
from tkinter import font as tkfont

from face_recog import *


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # change this
        self.geometry("1000x500")

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, RegistrationPage, PasswordFailed, RegisterSuccess, RegisterFailed, Authenticate, AccessDenied, AccessGranted, RegisterName):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="black")

        self.controller = controller
        WelcomeLabel = tk.Label(self,
                                text="Welcome",
                                font=controller.title_font,
                                background="black",
                                foreground="white",
                                width=100,
                                height=10
                                )
        WelcomeLabel.pack(side="top", fill="x", pady=10)

        register_button = tk.Button(self,
                                    text="Register",
                                    command=lambda: controller.show_frame("RegistrationPage"),
                                    background="blue",
                                    foreground="white"
                                    )
        register_button.pack(side="left")

        authenticate_button = tk.Button(self,
                                        text="Authenticate",
                                        command=lambda: controller.show_frame("Authenticate"),
                                        background="blue",
                                        foreground="white"
                                        )
        authenticate_button.pack(side="right")


class RegistrationPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.configure(bg="black")

        titleLabel = tk.Label(self,
                              text="Registration",
                              font=controller.title_font,
                              background="black",
                              foreground="white",
                              width=100,
                              )
        titleLabel.pack(side="top", fill="x", pady=10)

        infoLabel = tk.Label(self,
                             text="Please enter the administrator password to register yourself",
                             font=controller.title_font,
                             background="black",
                             foreground="white",
                             width=80
                             )
        infoLabel.pack(side="top", fill="x", pady=10)

        password = tk.Entry(self, show="*")
        password.pack()

        button = tk.Button(self, text="Register",
                           command=lambda: controller.show_frame("RegisterName") if (password.get() == "a")
                           else controller.show_frame("PasswordFailed"),
                           background="blue",
                           foreground="white"
                           )
        button.pack(side="bottom")

class RegisterName(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.configure(bg="black")

        titleLabel = tk.Label(self,
                              text="Registration",
                              font=controller.title_font,
                              background="black",
                              foreground="white",
                              width=100,
                              )
        titleLabel.pack(side="top", fill="x", pady=10)

        infoLabel = tk.Label(self,
                             text="Please enter your name and stand infront of the camera, then press the button below",
                             font=controller.title_font,
                             background="black",
                             foreground="white",
                             width=80
                             )
        infoLabel.pack(side="top", fill="x", pady=10)

        name = tk.Entry(self)
        name.pack()

        button = tk.Button(self, text="Register",
                           command=lambda: take_registration_picture(controller, name.get()),
                           background="blue",
                           foreground="white"
                           )
        button.pack(side="bottom")

class PasswordFailed(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.configure(bg="black")

        label = tk.Label(self,
                         text="Seems like you typed the wrong password, please try again",
                         font=controller.title_font,
                         background="black",
                         foreground="white",
                         width=100,
                         height=10
                         )
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("StartPage"),
                           background="blue",
                           foreground="white"
                           )
        button.pack()


class RegisterSuccess(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.configure(bg="black")

        label = tk.Label(self,
                         text="Registration Success!!",
                         font=controller.title_font,
                         background="black",
                         foreground="green",
                         width=100,
                         height=10
        )
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("StartPage"),
                           background="blue",
                           foreground="white"
                           )
        button.pack()


class RegisterFailed(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.configure(bg="black")

        label = tk.Label(self,
                         text="Sorry, due to an internal issue the registration failed, please try again",
                         font=controller.title_font,
                         background="black",
                         foreground="red",
                         width=100,
                         height=10
                        )
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("StartPage"),
                           background="blue",
                           foreground="white"
                           )
        button.pack()


class Authenticate(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.configure(bg="black")

        label = tk.Label(self, text="Please be in front of the camera and press the button to authenticate", font=controller.title_font,
                         background="black",
                         foreground="white",
                         width=100,
                         height=5
                         )
        label.pack(side="top", fill="x", pady=5)
        
        label1 = tk.Label(self, text="Please press any key after the image is shown to complete authentication", font=controller.title_font,
                         background="black",
                         foreground="white",
                         width=100,
                         height=5
                         )
        label1.pack(side="top", fill="x", pady=5)
        
        button = tk.Button(self, text="Authenticate",
                           command=lambda: grant_access(controller),
                           background="blue",
                           foreground="white"
                           )
        button.pack()


class AccessGranted(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="black")
        label = tk.Label(self, text="ACCESS GRANTED", font=controller.title_font,
                         background="black",
                         foreground="green",
                         width=100,
                         height=10
                         )
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="back",
                           command=lambda: controller.show_frame("StartPage"),
                           background="blue",
                           foreground="white"
                           )
        button.pack()


class AccessDenied(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="black")
        label = tk.Label(self, text="ACCESS DENIED", font=controller.title_font,
                         background="black",
                         foreground="red",
                         width=100,
                         height=10
                         )
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("StartPage"),
                           background="blue",
                           foreground="white"
                           )
        button.pack()
