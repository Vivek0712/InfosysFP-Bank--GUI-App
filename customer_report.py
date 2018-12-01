def print_customer_no_loan(cursor):
    cursor.execute("SELECT c.CustomerId,c.FirstName,c.LastName FROM Customer c WHERE  NOT EXISTS (SELECT la.CustomerId FROM LoanAccount la WHERE c.CustomerId= la.CustomerId)")
    res=cursor.fetchall()
    if(res):
        print (" {0:15s} \t{1:20s}\t{2:20s}".format("Customer Id","First Name","Last Name"))
        for result in res:
            print (" {0:11d}\t \t{1:20s}\t{2:20s}".format(result[0],result[1],result[2]))
        return 1
def print_customer_no_fd(cursor):
    cursor.execute("SELECT c.CustomerId,c.FirstName,c.LastName FROM Customer c WHERE  NOT EXISTS (SELECT fd.CustomerId FROM FixedDeposit fd WHERE c.CustomerId= fd.CustomerId)")
    res=cursor.fetchall()
    if(res):
        print (" {0:15s} \t{1:20s}\t{2:20s}".format("Customer Id","First Name","Last Name"))
        for result in res:
            print (" {0:11d}\t \t{1:20s}\t{2:20s}".format(result[0],result[1],result[2]))
        return 1
def print_customer_noloanfd(cursor):
    cursor.execute("SELECT c.CustomerId,c.FirstName,c.LastName FROM Customer c WHERE  NOT EXISTS (SELECT la.CustomerId FROM LoanAccount la WHERE c.CustomerId= la.CustomerId) AND NOT EXISTS (SELECT fd.CustomerId FROM FixedDeposit fd WHERE c.CustomerId= fd.CustomerId) ")
    res=cursor.fetchall()
    if(res):
        print (" {0:15s} \t{1:20s}\t{2:20s}".format("Customer Id","First Name","Last Name"))
        for result in res:
            print (" {0:11d}\t \t{1:20s}\t{2:20s}".format(result[0],result[1],result[2]))
        return 1
