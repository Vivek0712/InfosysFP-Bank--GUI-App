import datetime
import random
import re
from tkinter import *
from tkinter import messagebox

def authsavings(amt):
        if(int(amt) < 0):
            messagebox.showinfo("Invalid", " Enter valid amount")
     
        else:
            messagebox.showinfo("Successful", " Amount Deposited Successfully")
           
            
def authcurrent(amt):
        if(int(amt) < 5000):
            messagebox.showinfo("Invalid", " Enter valid amount")
           
        else:
            messagebox.showinfo("Successful", " Amount Deposited Successfully")
        
def authfixed(amt,term):
        if(int(amt) < 0):
            messagebox.showinfo("Invalid", " Enter valid amount")
           
        else:
            messagebox.showinfo("Successful", " Amount Deposited Successfully")
            
            
class Savings():
    __date = ""
    __amt = 0.0
    __accnum = 0
    __withdrawals = 0
    def __init__(self):
        self.set_details()
    
    def set_details(self):
        self.__date = datetime.datetime.now()
        savings = Toplevel()
        savings.title("Savings account")
        savings.geometry("600x400")
        label = Label(savings,text= "amount to be deposited")
        label.place(x=40,y=40)
        T = Entry(savings,width=20)
        T.place(x=200,y=40)
        submit = Button(savings,text="submit",command = lambda : authsavings(T.get())).place(x=120,y=80)
        amt = (T.get())
        self.__amt = int(amt)
 
       
       
    def set_accnum(self,acc_num):
        self.__accnum = acc_num
    def writeDetails(self,cursor,cust_id):
        
        cursor.execute("INSERT INTO Savings VALUES(%s,%s,%s,%s,%s)",(self.__accnum,cust_id,self.__amt,self.__date,self. __withdrawals))
        self.display_details()
    def display_details(self):
        stmt = "\nAccount Number : " +self.__accnum + "\nBalance : "+self.__amt+"\n Date Created : "+self.__date+"\n No of Withdrawal done : "+self.__withdrawals+"" 
        messagebox.showinfo("Details",stmt)

class CurrentAccount():
    __date = ""
    __amt = 0.0
    __accnum = 0
    def __init__(self):
        self.set_details()
    def set_details(self):
        self.__date = datetime.datetime.now()
        savings = Toplevel()
        savings.title("Current account")
        savings.geometry("600x400")
        label = Label(savings,text= "amount to be deposited")
        label.place(x=40,y=40)
        T = Entry(savings,width=20)
        T.place(x=200,y=40)
        submit = Button(savings,text="submit",command = lambda : authcurrent(T.get())).place(x=120,y=80)
        self.__amt = T.get()
    def set_accnum(self,acc_num):
        self.__accnum = acc_num
    def writeDetails(self,cursor,cust_id):
        cursor.execute("INSERT INTO CurrentAccount VALUES(%s,%s,%s,%s)",(self.__accnum,cust_id,self.__amt,self.__date))
        self.display_details()
    def display_details(self):
        stmr = "\nAccount Number : " + self.__accnum + "\nBalance : "+ self.__amt + "\n Date Created : " +self.__date+""
        messagebox.showinfo("Details","%s"%stmr)

class FixedDeposit():
    __date = ""
    __amt = 0.0
    __accnum = 0
    __deposit_term = 0
    def __init__(self):
        self.set_details()
    def set_details(self):
        self.__date = datetime.datetime.now()
        savings = Toplevel()
        savings.title("Current account")
        savings.geometry("600x400")
        label = Label(savings,text= "amount to be deposited")
        label.place(x=40,y=40)
        T = Entry(savings,width=20)
        T.place(x=200,y=40)
        label1 = Label(savings, text = "Deposit term : ")
        label1.place(x=40,y=70)
        T1 = Entry(savings,width=20)
        T1.place(x=200,y=70)
        submit = Button(savings,text="submit",command = lambda : authfixed(T.get(),T1.get())).place(x=120,y=80)
        self.__amt = T.get()
    def set_accnum(self,acc_num):
        self.__accnum = acc_num
    def writeDetails(self,cursor,cust_id):
        cursor.execute("INSERT INTO FixedDeposit VALUES(%s,%s,%s,%s,%s)",(self.__accnum,cust_id,self.__amt,self.__date,self.__deposit_term))
        self.display_details(cursor,cust_id)
    def display_details(self,cursor,cust_id):
        cursor.execute("SELECT * FROM FixedDeposit WHERE CustomerId='"+str(cust_id)+"'")
        res =  cursor.fetchall()
        stmt1= "\n {0:15s} \t{1:8s}\t{2:20s}\t{3:15s}".format("Account Number","Amount","Date Created","Deposit Term")+""
        for result in res:
            stmt2 = " {0:14d} \t{1:8f}\t{2}\t{3:12d}".format(result[0],result[2],result[3],result[4])+""
        stmt1= stmt1+stmt2    
        messagebox.showinfo("Details",stmt1)
def open_account(cursor,cust_id):
    root = Toplevel()
    v = IntVar()
    Label(root, text="""Choose the account type:""",justify = LEFT,padx = 20).pack()
    Radiobutton(root,text="Savings",indicatoron = 0,padx = 20,variable=v,value=1,command = lambda : typeacc(cursor,cust_id,v)).pack(anchor=W)
    Radiobutton(root,text="Current",indicatoron = 0,padx = 20,variable=v,value=2,command = lambda : typeacc(cursor,cust_id,v)).pack(anchor=W)
    Radiobutton(root,text="Fixed",indicatoron = 0,padx = 20,variable=v,value=3,command = lambda : typeacc(cursor,cust_id,v)).pack(anchor=W)
    root.mainloop()
def typeacc(cursor,cust_id,v):
    print(v.get())
    if (v.get() == 1):
        savings_acc = Savings()
        savings_acc.set_accnum(generate_accnum(cursor))
        savings_acc.writeDetails(cursor,cust_id)
    elif (v.get() == 2):
        print (" ******* CURRENT ACCOUNT *******")
        current_acc = CurrentAccount()
        current_acc.set_accnum(generate_accnum(cursor))
        current_acc.writeDetails(cursor,cust_id)
    elif (v.get() == 3):
        print (" ******* FIXED DEPOSIT ACCOUNT *******")
        fd_acc = FixedDeposit()
        fd_acc.set_accnum(generate_accnum(cursor))
        fd_acc.writeDetails(cursor,cust_id)
    else:
        print (" Enter valid option")
def generate_accnum(cursor):
    flag = True
    while(flag):
    	random_num = random.randint(10000,99999)
    	cursor.execute("SELECT s.AccountNumber FROM Savings s INNER JOIN CurrentAccount ca INNER JOIN FixedDeposit fd INNER JOIN LoanAccount la ON s.AccountNumber = ca.AccountNumber AND s.AccountNumber = fd.AccountNumber AND s.AccountNumber = la.AccountNumber WHERE s.AccountNumber = %d"%random_num)
    	if(not(cursor.fetchone())):
    		account_num = random_num
    		flag = False
    return account_num


