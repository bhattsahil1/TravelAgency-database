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
def updateTourguide():
    try:
        id = input("Enter the Tourguide id of the Tourguide to update:")
        query1 = """
        SELECT * FROM TOUR_GUIDE WHERE Tourguide_id = %s;
        """
        try:
            cur.execute(query1,id)
        except:
            print("Error executing Search")
        records = []
        result = cur.fetchall()
        if not result:
            print("The Tour guide does not exist in the database")
        else:
            # print("The customer exists in the database")

            row = {}
            print("Enter new Tour guide details: ")
            row["Name"] = (input("Name: "))
            row["Dob"] = input("Date of Birth (YYYY-MM-DD): ")

            query2 = """
            UPDATE TOUR_GUIDE SET Tourguide_name='%s' , Dob='%s' WHERE Tourguide_id = '%s' ;
            """%(row["Name"], row["Dob"], id)
            try:
                print(query2)
                try:
                    cur.execute(query2)
                except:
                    print("SQL execution")
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

def Addhotel():
    try:
        row = {}
        print("Enter new HOTEL details: ")
        name = (input("Hotel Name: "))
        row["Hotel_Name"] = name
        row["Hotel_address"] = input("HOTEL ADDRESS:  ")
        row["Rating"] = input("Rating: ")  #Assuming the employee of the travel agency knows the rating of the hotel the customer chooses
        """
        In addition to taking input, you are required to handle domain errors as well
        HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
        """

        query = "INSERT INTO HOTELS(Hotel_Name,Hotel_address,Rating) VALUES('%s', '%s','%s')" %(row["Hotel_Name"] ,row["Hotel_address"],row["Rating"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Hotels")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)
        
    return

def Addpackage():
    try:
        id = input("Enter Customer id")
        query1 = """
        SELECT * FROM CUSTOMERS WHERE CUSTOMERS.Sno = %s;
        """
        query2 = """
        SELECT * FROM CUSTOMER_PACKAGE WHERE CUSTOMER_PACKAGE.Sno = %s;
        """
        try:
            cur.execute(query1,id)
        except:
            print("Error executing Search")
        result = cur.fetchall()
        print(result)
        if not result:
            print("The customer does not exist in the database")
            return
        try:
            cur.execute(query2,id)
        except:
            print("Error executing Search2")
        result = cur.fetchall()
        if result:
            print("Customer has already entered his package details")
            return

        row = {}
        print("Enter Package details: ")
        name = (input("Package Category "))
        row["Package_category"] = name
        row["Transport"] = input("Transport Vehicle:  ")
        row["type"] = input("Package Type: ")  #Assuming the employee of the travel agency knows the rating of the hotel the customer chooses
        """
        In addition to taking input, you are required to handle domain errors as well
        HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
        """

        query = "INSERT INTO PACKAGE(Package_category,Transport_vehicle,Package_type) VALUES('%s', '%s','%s')" %(row["Package_category"] ,row["Transport"],row["type"])

        print(query)
        cur.execute(query)
        con.commit()
        print("Inserted Into Package")

        q = "SELECT LAST_INSERT_ID();"
        cur.execute(q)
        result = cur.fetchall()
        print(result)
        query = "INSERT INTO CUSTOMER_PACKAGE(Sno,Package_Opted) VALUES('%s','%s')" %( id, result[0]["LAST_INSERT_ID()"])
        cur.execute(query)
        con.commit()
        print("Successfully inserted into Customer_Package TABLE")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)
        
    return

def ChooseHotel():
    """
    get the id
    id should exist corresponding hotel should not exist
    If both conditions are satisfied Display HOTELS table and enquire for choosing the Hotel Name
    INSERT the customer id and hotel Name into HOTEL_DETAILS
    """
    try:
        id = input("Enter customer ID: ")
        query1 = """
        SELECT * FROM CUSTOMERS WHERE CUSTOMERS.Sno = %s;
        """
        query2 = """
        SELECT * FROM HOTEL_DETAILS WHERE HOTEL_DETAILS.Sno = %s;
        """
        try:
            cur.execute(query1,id)
        except:
            print("Error executing Search")
        result = cur.fetchall()
        print(result)
        if not result:
            print("The customer does not exist in the database")
            return
        try:
            cur.execute(query2,id)
        except:
            print("Error executing Search2")
        result = cur.fetchall()
        if result:
            print("Customer has already entered his hotel details")
            return
        else:
            try:
                print("Available Hotels")
                try:
                    cur.execute("SELECT * FROM HOTELS")
                except:
                    print("display hotel err")
                hotels=[]
                hotellist=cur.fetchall()
                for row in hotellist:
                    hotels.append(row)
                printTable(hotels)
                hotelname = input("Enter Hotel Name: ")
                query3 = "INSERT INTO HOTEL_DETAILS(Sno,Hotel_Opted) VALUES('%s', '%s')" %(id,hotelname)
                try:
                    cur.execute(query3)
                except:
                    print("Final execution err")
                con.commit()
                print("Successfully added the record")
            except:
                print("Error executing insertion")
    except:
        print("Error inserting record")
    

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

def RemoveTourguide():
    try:
        id = input("Enter the Tour guide id of the Tour Guide to be removed.")
        query1 = """
        SELECT * FROM TOUR_GUIDE WHERE Tourguide_id = %s;
        """
        try:
            cur.execute(query1,id)
        except:
            print("Error executing Search")
        records = []
        result = cur.fetchall()
        if not result:
            print("The Tour guide does not exist in the database")
        else:
            # print("The customer exists in the database")
            query2 = """
            DELETE FROM TOUR_GUIDE WHERE Tourguide_id = %s;
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

def enterEdetails():
    try:
        id = input("Enter Customer id")
        query1 = """
        SELECT * FROM CUSTOMERS WHERE CUSTOMERS.Sno = %s;
        """
        query2 = """
        SELECT * FROM EMERGENCY_DETAILS WHERE EMERGENCY_DETAILS.Sno = %s;
        """
        try:
            cur.execute(query1,id)
        except:
            print("Error executing Search")
        result = cur.fetchall()
        print(result)
        if not result:
            print("The customer does not exist in the database")
            return
        try:
            cur.execute(query2,id)
        except:
            print("Error executing Search2")
        result = cur.fetchall()
        if result:
            print("Customer has already entered his emergency details")
            return

        row = {}
        print("Enter Emergency details: ")
        name = (input("Emergency Cantact Name: "))
        row["Contact_Name"] = name
        row["Contact_Pno"] = input("Contact Ph.No:  ")
        row["Address"] = input("Address: ")  
        """
        In addition to taking input, you are required to handle domain errors as well
        HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
        """

        query = "INSERT INTO EMERGENCY_DETAILS VALUES('%s','%s', '%s','%s')" %(id,row["Contact_Name"] ,row["Contact_Pno"],row["Address"])

        print(query)
        cur.execute(query)
        con.commit()
        print("Inserted Emergency Contact Details")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)
        
    return

def enterSPneeds():
    try:
        id = input("Enter Customer id")
        query1 = """
        SELECT * FROM CUSTOMERS WHERE CUSTOMERS.Sno = %s;
        """
        query2 = """
        SELECT * FROM SPECIAL_REQUESTS WHERE SPECIAL_REQUESTS.Sno = %s;
        """
        query3 = """
        SELECT * FROM MEDICINE WHERE MEDICINE.Sno = %s;
        """
        
        try:
            cur.execute(query1,id)
        except:
            print("Error executing Search")
        result = cur.fetchall()
        print(result)
        if not result:
            print("The customer does not exist in the database")
            return
        try:
            cur.execute(query2,id)
        except:
            print("Error executing Search2")
        result = cur.fetchall()
        if result:
            print("Customer has already entered his Special request details")
            return
        try:
            cur.execute(query3,id)
        except:
            print("Error executing search3")
        result = cur.fetchall()
        if result:
            print("Customer has already entered his medicine details")
        row = {}
        print("Enter Special  details: ")
        child = (input("Is a child travelling with you? "))
        row["child_status"] = child
        row["Disability_status"] = input("Is a differently abled person travelling with you?  ")
        row["Medicine"] = input("Do you need any medicines for your travel? ")  
        """
        In addition to taking input, you are required to handle domain errors as well
        HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
        """

        query = "INSERT INTO SPECIAL_REQUESTS VALUES('%s','%s', '%s')" %(id,row["child_status"] ,row["Disability_status"])

        print(query)
        cur.execute(query)
        query= "INSERT INTO MEDICINE VALUES('%s','%s')" %(id,row["Medicine"])
        print(query)
        cur.execute(query)
        con.commit()
        print("Inserted Special Requests and Medicine Details")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)
        
    return


def CustomerStatistics():
    """
    Function prints a report containing 
    the tour details of the customer.
    """
    # print("Not implemented")
    query = """
    SELECT CUSTOMERS.Sno,Fname,Mname,Lname,Start_date,Last_date,Hno,City,DOB,No_of_travellers FROM CUSTOMERS 
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

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)
        
    return

def enterflight():
    try:
        id = input("Enter the customer id of the customer to allot flight:")
        query1 = "SELECT * FROM CUSTOMERS WHERE Sno = %s;"
        print(query1)
        try:
            cur.execute(query1,id)
            # k = cur.fetchall()
            # print(k)
        except:
            print("Error executing Search")
        result = cur.fetchall()
        if not result:
            print("The customer does not exist in the database")
        else:
            print("List of available flights:")
            cur.execute("SELECT * FROM TRANSPORTATION")
            flylist = []
            flyresult = cur.fetchall()
            for row in flyresult:
                flylist.append(row)
             # print(row)
            printTable(flylist)

            flightno=input("Select a flight number : ")
            query2 ="INSERT INTO FLIGHT_DETAILS(Sno,Flight_Opted) VALUES('%s','%s')"%(id,flightno)
            cur.execute(query2)
            con.commit
            print("Flight allocated!")
    except:
        print("error")


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
    elif(ch==8):
        Addhotel()
    elif(ch==9):
        Addpackage()
    elif(ch==10):
        RemoveTourguide()
    elif(ch==11):
        updateTourguide()
    elif(ch==12):
        ChooseHotel()
    elif(ch==13):
	    enterflight()
    elif(ch==14):
	    enterEdetails()
    elif(ch==15):
	    enterSPneeds()
    # elif(ch==16):
	#     billcustomer()
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
                print("8. Insert new Hotel")
                print("9. Insert Package")
                print("10. Remove Tour Guide")
                print("11. Update Tour Guide")
                print("12. Choose Hotel")
                print("13. Choose Flight")
                print("14. Enter Emergency Details")
                print("15. Enter Special Requests")
                # print("16. Bill")
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