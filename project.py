from tkinter import *
from tkinter import ttk
import os
def main_account_screen():
    global main_screen
    main_screen = Tk()   # create a GUI window 
    main_screen.geometry("300x250") # set the configuration of GUI window 
    main_screen.title("Health Monitoring System") # set the title of GUI window
    
    
    main_screen.geometry("300x250")

    
    Label(main_screen, text="Please enter details below to login").pack()
    Label(main_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()
    Label(main_screen, text="Username  ").pack()
    username_login_entry = Entry(main_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(main_screen, text="").pack()
    Label(main_screen, text="Password  ").pack()
    password__login_entry = Entry(main_screen, textvariable=password_verify, show= '*')
    password__login_entry.pack()
    Label(main_screen, text="").pack()
    Button(main_screen, text="Login", width=10, height=1, command=home_page).pack()
    main_screen.mainloop()
def home_page():
    screen=Toplevel(main_screen)
    screen.geometry("300x250")
    Label(screen, text="Home Page").pack()
    Label(screen, text="").pack()
    Button(screen, text="SIGN UP",width=20, height=3,bd=10,command=sign_up ).pack()
    Button(screen, text="LOGIN", width=20, height=3,bd=10,command=log_in).pack()
   
def sign_up():
    sign_screen=Toplevel(main_screen)
    sign_screen.geometry("500x350")
    Label(sign_screen, text="Sign up").pack()
    Label(sign_screen, text="").pack()
    Button(sign_screen, text="Doctor",width=20, height=3,bd=10).pack()
    Button(sign_screen, text="Patient",width=20, height=3,bd=10).pack()

def log_in():
    log_screen=Toplevel(main_screen)
    log_screen.geometry("500x350")
    Label(log_screen, text="Log in").pack()
    Label(log_screen, text="").pack()
    Button(log_screen, text="Doctor",width=20, height=3,bd=10).pack()
    Button(log_screen, text="patient",width=20, height=3,bd=10).pack()



def pd_login():
    screen=Toplevel(main_screen)
    screen.geometry("300x250")
    Label(screen, text="log page").pack()
    Label(screen, text="").pack()
    Button(screen, text="SIGN UP",width=20, height=3,bd=10,command=doctor_sign ).pack()
    Button(screen, text="LOGIN", width=20, height=3,bd=10,command=patient_login).pack()

def doctor_sign():
    username_verify = StringVar()
    password_verify = StringVar()
 
    dsign_screen=Toplevel(main_screen)
    dsign_screen.geometry("500x350")
    Label(dsign_screen, text="sign up").pack()
    Label(dsign_screen, text="Username  ").pack()
    username_dsign_entry = Entry(d_screen, textvariable=username_verify)
    username_dsign_entry.pack()
    
    Label(dsign_screen, text="").pack()
    Label(dsign_screen, text="Password  ").pack()
    password__dsign_entry = Entry(d_screen, textvariable=password_verify, show= '*')
    password__dsign_entry.pack()
    Label(dsign_screen, text="").pack()
    Button(dsign_screen, text="signup", width=10, height=1,command=home_page).pack()

def patient_log():
    username_verify = StringVar()
    password_verify = StringVar()
    
    p_screen=Toplevel(main_screen)
    p_screen.geometry("500x350")
    Label(p_screen, text="log in").pack()
    Label(p_screen, text="Username  ").pack()
    username_p_entry = Entry(p_screen, textvariable=username_verify)
    username_p_entry.pack()
    Label(p_screen, text="").pack()
    
    Label(p_screen, text="Password  ").pack()
    password__p_entry = Entry(p_screen, textvariable=password_verify, show= '*')
    password__p_entry.pack()
    Label(p_screen, text="").pack()
    Button(p_screen, text="login", width=10, height=1,command=p_login).pack()



    




def doctor_page():
    doctor_screen=Toplevel(main_screen)
    doctor_screen.geometry("500x350")
    Label(doctor_screen, text="view all patients").pack()
    Button(doctor_screen, text="patient1",width=20, height=3,bd=10).pack()
    Button(doctor_screen, text="patient2",width=20, height=3,bd=10).pack()
    Button(doctor_screen, text="Search",width=20, height=3,bd=10).pack()
   
    Button(doctor_screen, text="Back",width=10,height=2,command=pd_login).pack()
def patient_page():
    patient_screen=Toplevel(main_screen)
    patient_screen.geometry("500x350")
    Label(patient_screen, text="Patient Page").pack()
    Button(patient_screen, text="",width=20, height=3,bd=10).pack()
    Button(patient_screen, text="UPDATE",width=20, height=3,bd=10).pack()
   
    Button(cus_screen, text="Back",width=10,height=2,command=pd_login).pack()
main_account_screen()
 
