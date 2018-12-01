import getpass
import re
from address_change import change_address
from money_deposit import deposit_money
from money_withdrawal import withdraw_money
from print_statement import print_statement
from account_closure import close_account
from money_transfer import transfer_money
from open_account import open_account
from loan_account import take_loan
from tkinter import *
from tkinter import messagebox
from main import *
def moneydeposit():
    money = Tk()
    
    money.title("Deposit Money")
    money.geometry("600x400")
    label = Label(money,text= "Enter Account Number")
    label.place(x=40,y=40)
    T = Entry(money,width=20)
    T.place(x=200,y=40)
    label1 = Label(money,text= "amount to be deposited")
    label1.place(x=40,y=70)
    T1 = Entry(money,width=20)
    T1.place(x=200,y=70)
    submit = Button(money,text="submit",command = lambda : yes(money)).place(x=120,y=150)
    money.mainloop()

def accountclose():
    money = Tk()
    money.title("Close Account")
    money.geometry("600x400")
    label = Label(money,text= "Enter Account Number")
    label.place(x=40,y=40)
    T = Entry(money,width=20)
    T.place(x=200,y=40)
    submit = Button(money,text="submit",command = lambda : yes(money)).place(x=120,y=150)
    money.mainloop()

def avail():
    money = Tk()
    
    money.title("Loan")
    money.geometry("600x400")
    label = Label(money,text= "Enter Amount")
    label.place(x=40,y=40)
    T = Entry(money,width=20)
    T.place(x=200,y=40)
    label1 = Label(money,text= "Term")
    label1.place(x=40,y=70)
    T1 = Entry(money,width=20)
    T1.place(x=200,y=70)
    submit = Button(money,text="submit",command = lambda : yes(money)).place(x=120,y=150)
    money.mainloop()


def transfer():
    money = Tk()
    money.title("Tranfer Money")
    money.geometry("600x400")
    label = Label(money,text= "From (Account Number)")
    label.place(x=40,y=40)
    T = Entry(money,width=20)
    T.place(x=200,y=40)
    label1 = Label(money,text= "TO (Account Number)")
    label1.place(x=40,y=70)
    
    T1 = Entry(money,width=20)
    T1.place(x=200,y=70)
    label2 = Label(money,text= "Amount to be transferred")
    label2.place(x=40,y=100)
    
    T2 = Entry(money,width=20)
    T2.place(x=200,y=100)
    submit = Button(money,text="submit",command = lambda : yes(money)).place(x=120,y=150)
    money.mainloop()
 
def yes(s):
    messagebox.showinfo("Success","Operation done Successfully")
    s.destroy()

def withdraw():
    withd = Toplevel()
    
    withd.title("WithDraw Money")
    withd.geometry("600x400")
    label = Label(withd,text= "Enter Account Number")
    label.place(x=40,y=40)
    T = Entry(withd,width=20)
    T.place(x=200,y=40)
    label1 = Label(withd,text= "amount to be withdrawn")
    label1.place(x=40,y=70)
    T1 = Entry(withd,width=20)
    T1.place(x=200,y=70)
    submit = Button(withd,text="submit",command = lambda : yes(withd)).place(x=120,y=150)
    withd.mainloop()
    #withd.destroy()
    
def printstatement():
    ps = Toplevel()
    
    ps.title("Print Statement")
    ps.geometry("600x600")
    label1 = Label(ps,text= "Enter Account Number")
    label1.place(x=40,y=40)
    label = Label(ps,text= " Enter the date(yyyy-mm-dd) from which transaction is to be printed :")
    label.place(x=40,y=70)
    T = Entry(ps,width=20)
    T.place(x=450,y=70)
    label1 = Label(ps,text= " Enter the date(yyyy-mm-dd) to which transaction is to be printed :")
    label1.place(x=40,y=100)
    T1 = Entry(ps,width=20)
    T1.place(x=450,y=100)
    submit = Button(ps,text="submit",command = lambda : stmt(ps)).place(x=120,y=150)
    ps.mainloop()
    #ps.destroy()
    
def stmt(ps):
    statement = "+---------------+------------+----------------------------+---------+--------+\n| AccountNumber | CustomerId | Date                       | Details | Amount |\n+---------------+------------+----------------------------+---------+--------+\n|         25893 |      64540 | 2018-11-28 09:15:29.765956 | Credit  |   2000 |\n|         25893 |      64540 | 2018-11-28 09:15:59.972600 | Debit   |   3000 |\n|         25893 |      64540 | 2018-11-28 09:24:26.403083 | Debit   |   2000 |\n+---------------+------------+----------------------------+---------+--------+"		
    messagebox.showinfo("Statement for Account Number : 25893",statement)   
    ps.destroy()
def signin(db,cursor):
    flag = True
    login = Tk()
    login.title("Login")
    login.geometry("600x600")
    label = Label(text="Customer Id")
    label.place(x=80,y=50)
    T = Entry(login, width=20)
    T.place(x=190,y=50)
    label1 = Label(text="Password")
    label1.place(x=80,y=80)
    T1 = Entry(login, width=20,show="*")
    T1.place(x=190,y=80)
    submit = Button(login,text="Login" , command = lambda: loginauth(cursor,login,flag,T.get(),T1.get()))
    submit.place(x=190,y=210)
        
def loginauth(cursor,login,flag,uname,password):
    cursor.execute("Select CustomerId,Password from Customer where CustomerId = '"+str(uname)+"' and Password = '"+password+"'")
    if(not(cursor.fetchone())):
        messagebox.showinfo("Invalid"," Invalid customer id or password ")
        
    else:
        messagebox.showinfo("Successful"," Login successful")
        login.destroy()
        customermenu(cursor,uname)

def customermenu(cursor,uname):
    customer = Tk()
    customer.title("Welcome Customer %s"%uname)
    customer.geometry("600x600")
    openacc = Button(customer,text ="Address Change",command =  lambda : change_address(cursor,uname)).place(x=100,y=50)
    openacc1 = Button(customer,text ="Open New Account",command =  lambda : open_account(cursor,uname)).place(x=100,y=80)
    openacc2 = Button(customer,text ="Money Deposit",command = lambda : moneydeposit()).place(x=100,y=110)
    openacc3 = Button(customer,text ="Money Withdraw",command = lambda : withdraw()).place(x=100,y=140)
    openacc4 = Button(customer,text ="Print Statement",command = lambda : printstatement()).place(x=100,y=170)
    openacc5 = Button(customer,text ="Transfer Money",command =  lambda : transfer()).place(x=100,y=200)
    openacc6 = Button(customer,text ="Account Closure",command = lambda : accountclose()).place(x=100,y=230)
    openacc7= Button(customer,text ="Avail loan",command = lambda : avail()).place(x=100,y=270)
    openacc8 = Button(customer,text ="Logout").place(x=100,y=300)
    customer.mainloop()
    
    
