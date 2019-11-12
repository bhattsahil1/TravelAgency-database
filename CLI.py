import subprocess as sp
import pymysql
import pymysql.cursors

def RemoveCustomer():
    """
    Function to fire a Customer
    """
    print("Not implemented")

def promoteCustomer():
    """
    Function performs one of three jobs
    1. Increases salary
    2. Makes Customer a supervisor
    3. Makes Customer a manager
    """
    print("Not implemented")


def CustomerStatistics():
    """
    Function prints a report containing 
    the tour details of the customer.
    """
    # print("Not implemented")
    query = "SELECT * FROM CUSTOMERS INNER JOIN FLIGHTS ON CUSTOMERS.SNo=FLIGHTS.SNo"
    print(query)
    cur.execute(query)
    records = []
    result = cur.fetchall()
    for row in result:
        records.append(row)
        print(row)



def InsertCustomer():
    try:
        # Takes emplyee details as input
        row = {}
        print("Enter new Customer's details: ")
        name = (input("Name (Fname Minit Lname): ")).split(' ')
        row["Fname"] = name[0]
        row["Mname"] = name[1]
        row["Lname"] = name[2]
        row["Start_date"] = input("Start Date (YYYY-MM-DD): ")
        row["Last_date"] = input("End Date (YYYY-MM-DD): ")
        row["HNo"] = int(input("House No: "))
        row["City"] = input("City: ")
        row["DOB"] = input("Date of Birth (YYYY-MM-DD): ")
        row["No_of_travellers"] = int(input("Number of travellers: "))

        """
        In addition to taking input, you are required to handle domain errors as well

        For example: the SSN should be only 9 characters long
        Sex should be only M or F

        If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied

        HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
        """

        query = "INSERT INTO CUSTOMERS(Fname, Mname, Lname, Start_date, Last_date, HNo, City, DOB, No_of_travellers) VALUES('%s', '%s', '%s', '%s', '%s', %d, '%s', '%s', %d)" %(row["Fname"], row["Mname"], row["Lname"], row["Start_date"], row["Last_date"], row["HNo"], row["City"], row["DOB"], row["No_of_travellers"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)
        
    return

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch==1): 
        InsertCustomer()
    elif(ch==2):
        RemoveCustomer()
    elif(ch==3):
        promoteCustomer()
    elif(ch==4):
        CustomerStatistics()
    else:
        print("Error: Invalid Option")

# Global
while(1):
    tmp = sp.call('clear',shell=True)
    username = input("Username: ")
    password = input("Password: ")

    try:
        con = pymysql.connect(host='localhost',
                user=username,
                password=password,
                db='TRAVEL_AGENCY',
                cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear',shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")
        tmp = input("Enter any key to CONTINUE>")

        with con:
            cur = con.cursor()
            while(1):
                tmp = sp.call('clear',shell=True)
                print("1. Enter Tour Data")
                # print("2. Remove Tour Data")
                # print("3. ")
                # print("4. Customer Statistics")
                print("2. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear',shell=True)
                if ch==5:
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")


    except:
        tmp = sp.call('clear',shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
    
   


