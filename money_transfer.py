import datetime
def transfer_money(cursor,cust_id):
	acc_num = input(" Enter the Account from which transaction is to be made : ")
	cursor.execute("SELECT BalanceAmount FROM CurrentAccount WHERE AccountNumber = %s AND CustomerId = %s",(acc_num,cust_id))
	res = cursor.fetchone()
	cursor.execute("SELECT BalanceAmount FROM Savings WHERE AccountNumber = %s AND CustomerId = %s",(acc_num,cust_id))
	res1 = cursor.fetchone()
	if(res):
		flag = "current"
		from_balance = float(res[0])
	elif(res1):
		flag = "savings"
		from_balance = float(res1[0])
	if(res or res1):
		to_acc=input(" Enter the Account No for Transaction : ")
		cursor.execute("SELECT * FROM CurrentAccount WHERE AccountNumber ="+str(to_acc)+"")
		res1=cursor.fetchone()
		cursor.execute("SELECT * FROM Savings WHERE AccountNumber ="+str(to_acc)+"")
		res2=cursor.fetchone()
		if(res1):
			res = res1
			to_flag = "current"
		elif(res2):
			res = res2
			to_flag = "savings"
		else:
			return -2
		amt=int(input(" Enter the Amount to be transfered : "))
		to_balance = float(res[2])
		balance_flag = False
		if(flag == "current"):
			if((from_balance - amt) >= 5000):
				balance_flag = True
		if(flag == "savings"):
			if((from_balance - amt) >= 0):
				balance_flag = True
		if(balance_flag):
			temp = to_balance + amt
			if(to_flag == "current"):
				cursor.execute("""UPDATE CurrentAccount SET BalanceAmount = %s WHERE AccountNumber = %s""",(temp,to_acc))
			else:
				cursor.execute("""UPDATE CurrentAccount SET BalanceAmount = %s WHERE AccountNumber = %s""",(temp,to_acc))
			temp = from_balance - amt
			if(flag == "current"):
				cursor.execute("""UPDATE Savings SET BalanceAmount = %s WHERE AccountNumber = %s""",(temp,acc_num))
			else:
				cursor.execute("""UPDATE Savings SET BalanceAmount = %s WHERE AccountNumber = %s""",(temp,acc_num))
			cursor.execute("INSERT INTO TransactionDetails VALUES ("+str(acc_num)+",'"+str(cust_id)+"','"+str(datetime.datetime.now())+"','Debit',"+str(amt)+")")
			to_cust_id = int(res[1])
			cursor.execute("INSERT INTO TransactionDetails VALUES ("+str(to_acc)+",'"+str(to_cust_id)+"','"+str(datetime.datetime.now())+"','Credit',"+str(amt)+")")
			print (" Current Balance : ",from_balance-amt)
			return 1
		else:
			return -1
	else:
		return -2
