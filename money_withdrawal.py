import datetime
def withdraw_money(cursor,cust_id):
	print ("****** MONEY WITHDRAWAL ******")
	option = int(input(" Enter the account(1.Savings 2.Current Account) : "))
	if(option == 1):
		print ("****** SAVINGS ******")
		acc_num = int(input(" Enter account number"))
		cursor.execute("SELECT BalanceAmount,Withdrawals,DateCreated FROM Savings WHERE AccountNumber = %s AND CustomerId = %s",(acc_num,cust_id))
		res = cursor.fetchone()
		if(res):
			balance = float(res[0])
			withdrawal = int(res[1])
			date = res[2]
			cur_date = datetime.datetime.now()
			date_diff = cur_date - date
			if(date_diff.days > 30):
				withdrawal = 0%acc_num
			flag = True
			while(flag):
				amt = float(input(" Enter amount to withdraw : "))
				if(amt <= 0):
					print (" Amount canot be negative or zero")
				else:
					flag = False
			if((balance-amt)>=0):
				if(withdrawal < 10):
					balance -= amt
					withdrawal += 1
					cursor.execute("""UPDATE Savings SET BalanceAmount = %s, Withdrawals = %s WHERE AccountNumber = %s""",(balance,withdrawal,acc_num))
					cursor.execute("INSERT INTO TransactionDetails VALUES ("+str(acc_num)+",'"+str(cust_id)+"','"+str(datetime.datetime.now())+"','Debit',"+str(amt)+")")
					print (" Current balance : ", balance)
					return 1
				else:
					return -2
			else:
				return -3
	elif(option == 2):
		print ("****** CURRENT ACCOUNT ******")
		acc_num = int(input(" Enter account number : "))
		cursor.execute("SELECT BalanceAmount FROM CurrentAccount WHERE AccountNumber = %s AND CustomerId = %s",(acc_num,cust_id))
		res = cursor.fetchone()
		if(res):
			balance = float(res[0])
			flag = True
			while(flag):
				amt = float(input(" Enter amount to withdraw : "))
				if(amt <= 0):
					print (" Amount canot be negative or zero")
				else:
					flag = False
			print (amt)
			if((balance-amt)>= 5000):
				balance -= amt
				cursor.execute("""UPDATE CurrentAccount SET BalanceAmount = %s WHERE AccountNumber = %s""",(balance,acc_num))
				cursor.execute("INSERT INTO TransactionDetails VALUES ("+str(acc_num)+",'"+str(cust_id)+"','"+str(datetime.datetime.now())+"','Debit',"+str(amt)+")")
				print (" Current balance : ", balance)
				return 1
			else:
				return -1
		else:
			return -3
	else:
		return -3
