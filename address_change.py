import re
from tkinter import *
from tkinter import messagebox
def change_address(cursor,cust_id):
    signup1 = Tk()
    signup1.title("Address Change")
    signup1.geometry("600x600")
    label = Label(signup1,text="Address Line 1")
    label.place(x=80,y=50)
    T = Entry(signup1, width=20)
    T.place(x=190,y=50)
    label1 = Label(signup1,text="Address Line2")
    label1.place(x=80,y=80)
    T1 = Entry(signup1, width=20)
    T1.place(x=190,y=80)
    label2 = Label(signup1,text="City")
    label2.place(x=80,y=110)
    T2 = Entry(signup1, width=20)
    T2.place(x=190,y=110)
    label3 = Label(signup1,text="State")
    label3.place(x=80,y=140)
    T3 = Entry(signup1, width=20)
    T3.place(x=190,y=140)
    label4 = Label(signup1,text="Pincode")
    label4.place(x=80,y=170)
    T4 = Entry(signup1, width=20)
    T4.place(x=190,y=170)
    submit  = Button(signup1, text="Submit",command = lambda : senddata(signup1,cursor,cust_id,T.get(),T1.get(),T2.get(),T3.get(),T4.get()))
    submit.place(x=190,y=200)

def senddata(signup1,cursor,cust_id,addr1,addr2,city,state,pin):
    messagebox.showinfo("Successful","Address Changed Successfully!")
    cursor.execute("UPDATE Customer SET AddressLine1='"+addr1+"',AddressLine2='"+addr2+"',City='"+city+"',State='"+state+"',Pincode="+str(pin)+" WHERE CustomerId="+str(cust_id)+"")
    signup1.destroy()