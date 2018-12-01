import re
def print_loan_report(cursor):
    print (" ****** Loan Report ******")
    cust_id = int(input(" Enter Customer Id : "))
    cursor.execute("SELECT * FROM LoanAccount WHERE CustomerId = %d"%cust_id)
    res = cursor.fetchall()
    if(res):
        print (" {0:15s} \t{1:8s}\t{2:20s}".format("Account Number","Amount","Deposit Term"))
        for result in res:
            print (" {0:14d} \t{1:8f}\t\t{2}".format(result[0],result[3],result[4]))
        return 1
    else:
        return -1

def print_loan_report_customer(cursor):
    print (" ****** Loan Report ******")
    cust_id = int(input(" Enter Customer Id : "))
    cursor.execute("SELECT * FROM LoanAccount WHERE CustomerId = %d"%cust_id)
    res = cursor.fetchall()
    if(res):
        cursor.execute("SELECT * FROM LoanAccount WHERE LoanAmount >= (SELECT SUM(LoanAmount) FROM LoanAccount WHERE CustomerId = %d)"%cust_id)
        res = cursor.fetchall()
        if(res):
            print (" {0:15s} \t{1:8s}\t{2:20s}\t{3:10s}".format("Customer Id","Account Number","Amount","Deposit Term"))
            for result in res:
                print (" {0:11d} \t{1:20d}\t{2:8f}\t\t{3:4d}".format(result[1],result[0],result[3],result[4]))
            return 1
        else:
            return -2
    else:
        return -1

def print_loan_report_amount(cursor):
    print (" ****** Loan Report ******")
    flag = True
    while(flag):
        amt = int(input(" Enter Amount : "))
        if(amt > 0):
            if(amt%1000==0):
                flag = False
            else:
                print (" Amount should be in terms of 1000")
        else:
            print (" Enter valid amount")
    cursor.execute("SELECT DISTINCT(c.CustomerId),c.FirstName,c.LastName,la.LoanAmount FROM Customer c INNER JOIN LoanAccount la ON c.CustomerId = la.CustomerId WHERE la.LoanAmount >= %f"%float(amt))
    res = cursor.fetchall()
    if(res):
        print (" {0:15s} \t{1:20s}\t{2:20s}\t{3:10s}".format("Customer Id","First Name","Last Name","Amount"))
        for result in res:
            print (" {0:11d}\t \t{1:20s}\t{2:20s}\t{3:10f}".format(result[0],result[1],result[2],result[3]))
        return 1
    else:
        return -1

def print_loan_report_(cursor):
    print (" ****** Loan Report ******")
    cursor.execute("SELECT c.CustomerId,c.FirstName,c.LastName,SUM(fd.Amount),(SELECT SUM(LoanAmount) FROM LoanAccount WHERE CustomerId = c.CustomerId) FROM Customer c INNER JOIN FixedDeposit fd ON c.CustomerId = fd.CustomerId GROUP BY CustomerId HAVING (SELECT SUM(LoanAmount) FROM LoanAccount WHERE CustomerId = c.CustomerId) > SUM(fd.Amount)")
    res = cursor.fetchall()
    if(res):
        print (" {0:15s} \t{1:20s}\t{2:20s}\t{3:10s}\t{4:10s}".format("Customer Id","First Name","Last Name","Sum of Fixed Deposit","Sum of Loan"))
        for result in res:
            print (" {0:11d} \t{1:20s}\t{2:20s}\t\t{3:5f}\t\t{4:5f}".format(result[0],result[1],result[2],result[3],result[4]))
        return 1
    else:
        return -1
