import datetime
def deposit_money(cursor,cust_id):

	cursor.execute("SELECT BalanceAmount FROM CurrentAccount WHERE AccountNumber = %d"%acc_num)
	res = cursor.fetchone()
	cursor.execute("SELECT BalanceAmount FROM Savings WHERE AccountNumber = %d"%acc_num)
	res1 = cursor.fetchone()
	if(res):
		flag = "current"
		balance = float(res[0])
	elif(res1):
		flag = "savings"
		balance = float(res1[0])
	else:
		return -1
	if(flag == "current"):
		amt = float(input(" Enter amount to be deposited : "))
		if(amt <= 0):
			return -2
		balance += amt
		cursor.execute("""UPDATE CurrentAccount SET BalanceAmount = %s WHERE AccountNumber = %s""",(balance,acc_num))
		cursor.execute("INSERT INTO TransactionDetails VALUES ("+str(acc_num)+",'"+str(cust_id)+"','"+str(datetime.datetime.now())+"','Credit',"+str(amt)+")")
		return 1
	if(flag == "savings"):
		amt = float(input(" Enter amount to be deposited : "))
		balance += amt
		cursor.execute("""UPDATE Savings SET BalanceAmount = %s WHERE AccountNumber = %s""",(balance,acc_num))
		cursor.execute("INSERT INTO TransactionDetails VALUES ("+str(acc_num)+",'"+str(cust_id)+"','"+str(datetime.datetime.now())+"','Credit',"+str(amt)+")")
		return 1
