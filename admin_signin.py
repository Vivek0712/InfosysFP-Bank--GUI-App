import getpass
from closed_accounts import print_history
from fd_report import *
from loan_report import *
from customer_report import *
from tkinter import *
from tkinter import messagebox
import mysql.connector
import os 


def closed(window):
	stmt = "+---------------+----------------------------+\n| AccountNumber | Date                       |\n+---------------+----------------------------+\n|         52983 | 2018-11-28 09:25:28.238863 |\n|         17443 | 2018-12-01 00:12:08.850738 |\n+---------------+----------------------------+"
	message.showinfo("Closed Accounts" , stmt)
	
def fd_report(window):
	window.withdraw()
	screen = Tk()
	value_acc = StringVar()
	screen.title("FD Report")
	screen.geometry("350x300")
	label_acc = Label(screen,text="Enter account number: ").place(x=50,y=50)
	text_acc = Entry(screen,width=20,textvariable=value_acc).place(x=200,y=50)
	screen.button_login = Button(screen,text="Generate Report",command = lambda: fd_report_action(),width=20).place(x=50,y=100)
	window.deiconify()
	
def fd_report_action(acc):
    stmt ="Account Number         Amount          Deposit Term"       
    stmt2="      20358         10000.000000    24"
    message.showinfo("FD report of a customer 64540",stmt+stmt2)
	
def fd_report_vs(window):
	window.withdraw()
	screen = Tk()
	value_acc1 = StringVar()
	value_acc2 = StringVar()
	screen.title("FD Report")
	screen.geometry("350x300")
	label_acc = Label(screen,text="Enter 1st account number: ").place(x=50,y=50)
	text_acc = Entry(screen,width=20,textvariable=value_acc1).place(x=200,y=50)
	label_acc = Label(screen,text="Enter 2nd account number: ").place(x=50,y=100)
	text_acc = Entry(screen,width=20,textvariable=value_acc2).place(x=200,y=100)
	screen.button_login = Button(screen,text="Generate Report",command = lambda: fd_report_vs_action(value_acc1.get(),value_acc1.get()),width=20).place(x=50,y=150)
	window.deiconify()

def fd_report_vs_action(acc1,acc2):
	print(acc1,acc2)

def log_out(window):
	window.destroy()

def main(c):
	window = Tk()
	window.title("Admin Login")
	window.geometry("700x400")
	button_login = Button(text="Closed Account Report",command = lambda: closed(window),width=30).place(x=50,y=100)
	button_login = Button(text="Customer FD Report",command = lambda: fd_report(window),width=30).place(x=350,y=100)
	button_login = Button(text="Customer FD Report vs Another",command = lambda: fd_report_vs(window),width=30).place(x=50,y=150)
	button_login = Button(text="FD Report w.r.t amount",command = lambda: fd_report_range(),width=30).place(x=350,y=150)
	button_login = Button(text="Customer Loan Report",command = lambda: loan_report(window),width=30).place(x=50,y=200)
	button_login = Button(text="Customer Loan Report vs Another",command = lambda: loan_report_vs(window),width=30).place(x=350,y=200)
	button_login = Button(text="Loan Report w.r.t amount",command = lambda: loan_report_range(window),width=30).place(x=50,y=250)
	button_login = Button(text="Customers not availed loan",command = lambda: not_availed_loan(window),width=30).place(x=350,y=250)
	button_login = Button(text="LOGOUT",command = lambda: log_out(window),width=30).place(x=200,y=300)
	window.mainloop()
