import sign_up
import mysql.connector
from sign_in import signin
from admin_signin import *
from tkinter import *
def signup_page(c,window):
    window.destroy()
    res = sign_up.signup(c)

def signin_page(db,c,window):
    window.destroy()
    res = signin(db,c)
    
def adm_page(c,window):
    window.destroy()
    res = main(c)
    
    
def mainfunc():
    db=mysql.connector.connect(host="localhost",user="root",passwd="",db="mysql")
    c=db.cursor()
    window= Tk()
    window.title("NoMoney Bank")
    window.geometry("600x600")
    label = Label(text="NoMoney Bank")
    label.place(x=80,y=50)
    label.config(font=("Courier", 44))
    cotton_type=StringVar(window)
    button_signup =  Button(text="SignUP",command = lambda : signup_page(c,window))
    button_signup.place(x=200,y=150)
    button_signup.config(font=("Courier", 20))
    button_signin =  Button(text="Sign In",command = lambda : signin_page(db,c,window))
    button_signin.place(x=200,y=250)
    button_signin.config(font=("Courier", 20))
    
    button_admin =  Button(text="Admin Sign In",command = lambda : adm_page(c,window))
    button_admin.place(x=200,y=350)
    button_admin.config(font=("Courier", 20))
    button_exit =  Button(text="Exit")
    button_exit.place(x=200,y=450)
    button_exit.config(font=("Courier", 20))
    window.mainloop()	
    c.close()

mainfunc()
'''	if(res == -1):
			print(" Account creation failed: Insufficient inital deposit(<5000)")
		else:
			print(" Account creation successful")
			db.commit()
	elif(menu_option == 2):
		signin(db,c)
	elif(menu_option == 3):
		admin_sign_in(db,c)
	else:
		print ("Enter valid menu")'''