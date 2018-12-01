def print_history(cursor):
	print (" ********* Closed Account History *********")
	print (" Account Number\t\t Date")
	cursor.execute("SELECT * FROM ClosedAccounts")
	res = cursor.fetchall()
	for record in res:
		print ("",record[0],"\t\t\t",record[1])
