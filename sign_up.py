import mysql.connector
import random
import re
import getpass
from tkinter import *
from tkinter import messagebox
from main import *

def signup(cursor):
    signup1 = Tk()
    signup1.title("SignUp")
    signup1.geometry("600x600")
    label = Label(text="First Name")
    label.place(x=80,y=50)
    T = Entry(signup1, width=20)
    T.place(x=190,y=50)
    label1 = Label(text="Last Name")
    label1.place(x=80,y=80)
    T1 = Entry(signup1, width=20)
    T1.place(x=190,y=80)
    label2 = Label(text="AddressLine1")
    label2.place(x=80,y=110)
    T2 = Entry(signup1, width=20)
    T2.place(x=190,y=110)
    label3 = Label(text="Address Line 2")
    label3.place(x=80,y=140)
    T3 = Entry(signup1, width=20)
    T3.place(x=190,y=140)
    label4 = Label(text="City")
    label4.place(x=80,y=170)
    T4 = Entry(signup1, width=20)
    T4.place(x=190,y=170)
    label5 = Label(text="State")
    label5.place(x=80,y=200)
    T5 = Entry(signup1, width=20)
    T5.place(x=190,y=200)
    label6 = Label(text="Pincode")
    label6.place(x=80,y=230)
    T6 = Entry(signup1, width=20)
    T6.place(x=190,y=230)
    label7 = Label(text="Password")
    label7.place(x=80,y=270)
    T7 = Entry(signup1,show="*",width=20)
    T7.place(x=190,y=270)
    label8 = Label(text="Confirm Password")
    label8.place(x=80,y=300)
    T8 = Entry(signup1,show="*",width=20)
    T8.place(x=190,y=300)
    submit  = Button(signup1, text="SignUP",command = lambda : senddata(signup1,cursor,T.get(),T1.get(),T2.get(),T3.get(),T4.get(),T5.get(),T6.get(),T7.get(),T8.get()))
    submit.place(x=190,y=330)
    #submit =  Button(text="SignUP", command=lambda : signup(cursor,T.get(),T1.get(),T2.get(),T3.get(),T4.get(),T5.get(),T6.get(),T7.get(),T8.get()).place(x=190,y=330)
    signup1.mainloop()
    #flag = True
    return 1

def senddata(signup1,cursor,first_name,last_name,addr1,addr2,city,state,pin,password1,password2):
    flag = True
    flag1= True
    flag2= True
    while(flag and flag1 and flag2):	
        random_num = random.randint(10000,99999)
        cursor.execute("SELECT CustomerId FROM Customer WHERE CustomerId = %d"%random_num)
        if(not(cursor.fetchone())):
            customer_id = random_num
            flag = False
        if(re.match(r'^[0-9]{6}$',pin,0)):
            flag1 = False
        else:
            messagebox.showinfo("Invalid", " Invalid pin( Valid pin: 6 digits")
        if(re.search(r'\w{8,}',password1,0)):
            if(password1 == password2):
                flag2 = False
            else:
                messagebox.showinfo("Invalid" ," Password mismatch")
        else:
            messagebox.showinfo("Invalid"," Invalid password (Minimum 8 letters)")
    messagebox.showinfo("Successful" ,"Account Created Successfully. Your Customer Id is %s"%customer_id)
    cursor.execute("INSERT INTO Customer VALUES("+str(customer_id)+",'"+first_name+"','"+last_name+"','"+addr1+"','"+addr2+"','"+city+"','"+state+"',"+str(pin)+",'"+password1+"')")
    signup1.destroy()
    mainfunc()