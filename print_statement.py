import mysql.connector
import re
import datetime
def print_statement(cursor,cust_id):
	acc_num = int(input(" Enter account number : "))
	cursor.execute("SELECT BalanceAmount FROM CurrentAccount WHERE AccountNumber = %s AND CustomerId = %s",(acc_num,cust_id))
	res = cursor.fetchone()
	cursor.execute("SELECT BalanceAmount FROM Savings WHERE AccountNumber = %s AND CustomerId = %s",(acc_num,cust_id))
	res1 = cursor.fetchone()
	if(res):
		balance = float(res[0])
	elif(res1):
		balance = float(res1[0])
	if(res or res1):
		flag = True
		while(flag):
			from_date = input(" Enter the date(yyyy-mm-dd) from which transaction is to be printed : ")
			if(re.match(r'^([0-9]{4})-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[012])$',from_date,0)):
				flag = False
				fdate = datetime.datetime.strptime(from_date,'%Y-%m-%d').date()
			else:
				print (" Invalid date format")
		flag = True
		while(flag):
			to_date = input(" Enter the date(yyyy-mm-dd) to which transaction is to be printed : ")
			if(re.match(r'^([0-9]{4})-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[012])$',to_date,0)):
				flag = False
				tdate = datetime.datetime.strptime(to_date,'%Y-%m-%d').date()
			else:
				print (" Invalid date format")
		date_diff = tdate - fdate
		if(date_diff.days < 0):
			return -1
		else:
			cursor.execute("""SELECT Date,Details,Amount FROM TransactionDetails WHERE Date BETWEEN %s AND %s AND AccountNumber = %s""",(fdate,tdate,str(acc_num)))
			res = cursor.fetchone()
			if(res):
				print (" *********  Statement  ********\n Account Number : ",acc_num)
				print (" Date\t\t\t Transaction Type\t\t Amount")
				while(res):
					print ("",res[0],"\t ",res[1],"\t\t\t",res[2])
					res = cursor.fetchone()
			else:
				print (" No transaction during the given date")
			print (" Balance : ",balance)
			return 1
	else:
		return -2
