import datetime
import random
import re
class LoanAccount():
    __amt = 0.0
    __term = 0
    __date = ""
    __accnum = 0

    def __init__(self):
        self.set_details()
    def set_details(self):
        self.__date = datetime.datetime.now()
        flag = True
        while(flag):
            self.__amt = int(input(" Enter loan amount to be availed : "))
            if(self.__amt > 0):
                if(self.__amt%1000==0):
                    flag = False
                else:
                    print (" Amount should be in terms of 1000")
            else:
                print (" Enter valid amount")
        flag = True
        while(flag):
            self.__term = int(input(" Enter Repayment term : "))
            if(self.__term > 0):
                flag = False
            else:
                print (" Invalid Repayment term")
    def set_accnum(self,acc_num):
        self.__accnum = acc_num
    def writeDetails(self,cursor,cust_id):
        cursor.execute("SELECT * FROM Savings WHERE CustomerId = %d"%cust_id)
        res = cursor.fetchone()
        if(res):
            balance = float(res[2])
            if(float(self.__amt) <= (2 * balance)):
                cursor.execute("INSERT INTO LoanAccount VALUES(%s,%s,%s,%s,%s)",(self.__accnum,cust_id,self.__date,self.__amt,self.__term))
                return 1
            else:
                return -1
        else:
            return -1

def take_loan(cursor,cust_id):
    la = LoanAccount()
    la.set_accnum(generate_accnum(cursor))
    res = la.writeDetails(cursor,cust_id)
    return res
def generate_accnum(cursor):
    flag = True
    while(flag):
    	random_num = random.randint(10000,99999)
    	cursor.execute("SELECT s.AccountNumber FROM Savings s INNER JOIN CurrentAccount ca INNER JOIN FixedDeposit fd INNER JOIN LoanAccount la ON s.AccountNumber = ca.AccountNumber AND s.AccountNumber = fd.AccountNumber AND s.AccountNumber = la.AccountNumber WHERE s.AccountNumber = %d"%random_num)
    	if(not(cursor.fetchone())):
    		account_num = random_num
    		flag = False
    return account_num
