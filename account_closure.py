import datetime
import re
def close_account(cursor,cust_id):
	acc_num = input(" Enter the Account Number to be closed : ")
	cursor.execute("SELECT * FROM CurrentAccount WHERE AccountNumber = %s AND CustomerId = %s",(acc_num,cust_id))
	res = cursor.fetchone()
	cursor.execute("SELECT * FROM Savings WHERE AccountNumber = %s AND CustomerId = %s",(acc_num,cust_id))
	res1 = cursor.fetchone()
	if(res or res1):
		option = input(" Confirm deletion (yes or no) : ")
		if(re.match(r'[Yy]es',option,0)):
			cursor.execute("INSERT INTO ClosedAccounts VALUES("+str(acc_num)+",'"+str(datetime.datetime.now())+"')")
			if(res):
				cursor.execute("DELETE FROM CurrentAccount WHERE AccountNumber="+str(acc_num)+"")
			if(res1):
				cursor.execute("DELETE FROM Savings WHERE AccountNumber="+str(acc_num)+"")
			return 1
		elif(re.match(r'[Nn]o',option,0)):
			return -1
	else:
		return -2
