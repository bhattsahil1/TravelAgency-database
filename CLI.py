import subprocess as sp
import pymysql
import pymysql.cursors

def printTable(myDict, colList=None):
   if not colList: colList = list(myDict[0].keys() if myDict else [])
   myList = [colList] # 1st row = header
   for item in myDict: myList.append([str(item[col] if item[col] is not None else '') for col in colList])
   colSize = [max(map(len,col)) for col in zip(*myList)]
   formatStr = ' | '.join(["{{:<{}}}".format(i) for i in colSize])
   myList.insert(1, ['-' * i for i in colSize]) # Seperating line
   for item in myList: print(formatStr.format(*item))

def viewtable():

    print("LIST OF ALL TABLES")
    print("1. CUSTOMERS")
    print("2. CUSTOMER_PACKAGE")
    print("3. FLIGHT_DETAILS")
    print("4. HOTELS")
    print("5. HOTEL_DETAILS")
    print("6. PACKAGE")
    print("7. TOUR_GUIDE")
    print("8. TRANSPORTATION")
    tablist = ["CUSTOMERS","CUSTOMER_PACKAGE","FLIGHT_DETAILS","HOTELS","HOTEL_DETAILS","PACKAGE","TOUR_GUIDE","TRANSPORTATION"]
    cxe = int(input("Enter choice> "))
    query = "SELECT * FROM " + tablist[cxe-1]
    cur.execute(query)
    records = []
    result = cur.fetchall()
    for row in result:
        records.append(row)
    printTable(records)



def InsertGuide():
    try:
        row = {}
        print("Enter new Tour Guide details: ")
        name = (input("Name: "))
        row["Tourguide_name"] = name
        row["Dob"] = input("Date of Birth (YYYY-MM-DD): ")

        """
        In addition to taking input, you are required to handle domain errors as well
        HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
        """

        query = "INSERT INTO TOUR_GUIDE(Tourguide_name,Dob) VALUES('%s', '%s')" %(row["Tourguide_name"] ,row["Dob"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)
        
    return

    
def RemoveCustomer():
    try:
        id = input("Enter the customer id of the customer to be removed:")
        query1 = """
        SELECT * FROM CUSTOMERS WHERE Sno = %s;
        """
        try:
            cur.execute(query1,id)
        except:
            print("Error executing Search")
        records = []
        result = cur.fetchall()
        if not result:
            print("The customer does not exist in the database")
        else:
            # print("The customer exists in the database")
            query2 = """
            DELETE FROM CUSTOMERS WHERE Sno = %s;
            """
            try:
                cur.execute(query2,id)
                records = []
                result = cur.fetchall()
                for row in result:
                    records.append(row)
                printTable(records)
                con.commit()
                print("Successfully deleted the record")
            except:
                print("Error executing Deletion")
    except:
        print("Error deleting record")
    """
    Function to fire a Customer
    """
    # print("Not implemented")

def updateCustomer():
    """
    Function performs one of three jobs
    1. Increases salary
    2. Makes Customer a supervisor
    3. Makes Customer a manager
    """
    try:
        id = input("Enter the customer id of the customer to update:")
        query1 = """
        SELECT * FROM CUSTOMERS WHERE Sno = %s;
        """
        try:
            cur.execute(query1,id)
        except:
            print("Error executing Search")
        records = []
        result = cur.fetchall()
        if not result:
            print("The customer does not exist in the database")
        else:
            # print("The customer exists in the database")

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

            query2 = """
            UPDATE CUSTOMERS SET Fname='%s', Mname='%s', Lname='%s', Start_date='%s', Last_date='%s', HNo='%d', City='%s', DOB='%s', No_of_travellers='%d' WHERE Sno = '%s' ;
            """%(row["Fname"], row["Mname"], row["Lname"], row["Start_date"], row["Last_date"], row["HNo"], row["City"], row["DOB"], row["No_of_travellers"],id)
            try:
                print(query2)
                cur.execute(query2)
                records = []
                result = cur.fetchall()
                for row in result:
                    records.append(row)
                printTable(records)
                con.commit()
                print("Successfully updated the record")
            except:
                print("Error executing Update")
    except:
        print("Error updating record")
    """
    Function to update a Customer's details
    """
    # print("Not implemented")

    # print("Not implemented")


def CustomerStatistics():
    """
    Function prints a report containing 
    the tour details of the customer.
    """
    # print("Not implemented")
    query = """
    SELECT * FROM CUSTOMERS 
    LEFT JOIN HOTEL_DETAILS ON CUSTOMERS.Sno=HOTEL_DETAILS.Sno
    LEFT JOIN FLIGHT_DETAILS ON CUSTOMERS.Sno = FLIGHT_DETAILS.Sno
    """
    print(query)
    cur.execute(query)
    records = []
    result = cur.fetchall()
    for row in result:
        records.append(row)
        # print(row)
    printTable(records)

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

        print("Inserted Into Database successfully")

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
        updateCustomer()
    elif(ch==4):
        CustomerStatistics()
    elif(ch==6):
        InsertGuide()
    elif(ch==7):
        viewtable()
    else:
        print("Error: Invalid Option")

# Global
k=0
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
                print("2. Remove Tour Data")
                print("3. Update Tour Data")
                print("4. Customer Statistics")
                print("5. Logout")
                print("6. Enter Tour Guide data")
                print("7. View all tables")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear',shell=True)
                if ch==5:
                    k=5
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")


    except:
        tmp = sp.call('clear',shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
    if k==5:
        break
