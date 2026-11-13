# how to start ? 
"""
Run in bash 
docker start mysql-db
"""

# CONNECT DATABASE

import mysql.connector as mydb

#ADMIN and CITIZEN portal management
verify = int(input("HOW DO YOU WANT TO PROCEED: \n \n as CITIZEN : 1 \n as ADMIN : 2 \n > Enter your choice here : "))

# Connect admin database

def connectDB():
    passwd = input("DATABASE PASSWORD : ")

    con = mydb.connect(
    host="localhost",
    user="root",
    passwd=passwd,
    database="demo_db")

    return con

# Create train database

def create_database():
    
    print("\n")
    print("===========>>>>> WELCOME ADMIN <<<<<<=================")
    print("\n")

    con = connectDB()
    cur = con.cursor()

# Create database if not exist

    scheduled_trains_table = '''CREATE TABLE IF NOT EXISTS trains(
    train_no INT,
    train_name VARCHAR(50),
    origin VARCHAR(50),
    destination VARCHAR(50),
    total_seats INT,
    available_seats INT
    )'''
    cur.execute(scheduled_trains_table)

#--PERMANENTLY SAVE THE DATA
    con.commit()
#--------------------------

    print("\n DATABASE READY THANKS FOR YOUR INPUT ")

    if con.is_connected():
        cur.close()
        con.close()


def admin_opt():

    while True:
        print("\n")
        ch = int(input(" ADD TRAIN : 1 \n VIEW TRAIN : 2 \n DELETE TRAIN : 3 \n Exit : 4 \n > Enter choice :: "))
        print("\n")
    
        if ch == 1:
            Add_Train()
        if ch == 2:
            View_Train()
        if ch == 3:
            Delete_Train()
        if ch == 4:
            print("Terminating programme \n")
            break




#ADD Table
def Add_Train():
    con = connectDB()
    cur = con.cursor()
    
    train_no = int(input("> Enter train number : "))
    train_name = input("> Enter train name : ")
    origin = input("> Enter origing station : ")
    destination = input("> Enter destination station : ")
    total_seats = int(input("> Enter total seats : "))
    available_seats = int(input("> Enter available seats : "))

    query = "INSERT INTO trains VALUES (%s,%s,%s,%s,%s,%s)"
    data = (train_no,train_name,origin,destination,total_seats,available_seats)
    cur.execute(query,data)
    con.commit()
    print("\n train added successfully \n")

#********************** ADD THIS IN CITIZEN SECTION AFTERWARDS **************************

def View_Train():
    con = connectDB()
    cur = con.cursor()
    cur.execute("SELECT * FROM trains")
    records = cur.fetchall()
    
    if len(records) == 0:
        print("no records found \n")
    else:
        print("\n")
        print("========------TRAIN-RECORD------==========")
        print("\n")
        print(" ____________________________________________________________________________________________________________________________________ ")
        print("|     TRAIN NO.      |      Train Name    |       Origin    |       Destination    |       Total Seats    |       Available Seats    |")
        print("|~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        
        l=0
        for i in records:
            m=0
            for j in i:
                decorate = len(str(records[l][m]))
                if decorate%2 != 0:
                    c = (15 - decorate)/2
                    c+=2
                    gap = int(c)*" "
                    print(gap,records[l][m],gap,end="")
                if decorate%2 == 0:
                    c = (16 - decorate)/2
                    c+=1
                    gap = int(c)*" "
                    print(gap,records[l][m],gap,end="")

                m+=1
                if m == 6:
                    l+=1
                    print("\n")
            
            

        print("|____________________|____________________|_________________|______________________|______________________|__________________________|")
        print("\n")
    con.close()
    cur.close()

def Delete_Train():
    con = connectDB()
    cur = con.cursor()
    train_no = int(input("> Enter Train number to be deleted : "))
    cur.execute("DELETE FROM trains WHERE train_no=%s",(train_no,))
    con.commit()

#cross checking 
    if cur.rowcount > 0:
        print("Train record deleted successfully \n")
    else:
        print("Train not found \n")

def Search_Train():
    con = connectDB()
    cur = con.cursor()

    train_no = int(input("> Enter Train number to search : "))
    cur.execute("SELECT * FROM trains WHERE train_no=%s",(train_no,))
    record = cur.fetchone()
    if record:
        print("Train Found \n")
        print("Train no. : ",record[0])
        print("Train name : ",record[1])
        print("Origin Station : ",record[2])
        print("Destination : ",record[3])
        print("Total seats : ",record[4])
        print("Available seats : ",record[5],"\n")

if verify==2:
    create_database()
    admin_opt()


#___________________________________________ ADMIN SECTION OVER ___________________________________________________________


def Citizen_login():

    con = mydb.connect(
    host="localhost",
    user="root",
    passwd="htmlcssjs6",
    database="demo_db")

    return con


def Citizen():
    print("\n")
    print("___________ >>>>> INDIAN RAILWAY WELCOMES YOU <<<<<< _______________")
    print("\n")

    while True:
        choice=int(input(">>> Select A Service <<< \n \n View All Trains : 1 \n Search Train : 2 \n Exit : 3 \n > Enter Your choice :: "))
        print("\n")
        if choice == 1:
            View_Train()
        if choice == 2:
            Search_Train()
        if choice == 3:
            print("Exiting programme \n")
            break

if verify == 1:
    Citizen() 