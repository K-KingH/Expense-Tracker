import sqlite3
from sqlite3 import Error

#Creation of connection to database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)   
    return conn   

#Creation of table
def table(conn, tableC):
    try:
        c = conn.cursor()
        c.execute(tableC)
    except Error as e:
        print(e)
        
#Insert information in table using four user-defined inputs       
def addInfo(conn,nid,tid,did,pid):
        sql = ''' INSERT INTO Tracker(name,type,Date_of_Purchase, Price) VALUES(?,?,?,?)'''
        info = conn.cursor()
        info.execute(sql, (nid,tid,did,pid)) 
        return info.lastrowid   
    
#Delete entries based on row id(user input)    
def delInfo(conn, deleteK): 
    delC = ''' DELETE FROM Tracker WHERE id=? '''
    c = conn.cursor()
    c.execute(delC, (deleteK,))
    conn.commit()
#Run program     
def main():
    #creates database and table in speficed folder if both don't exist
    database = r"E:SQL\sqlite\db\expenses.db"
    tableC = """ CREATE TABLE IF NOT EXISTS Tracker (
                                        id integer PRIMARY KEY,
                                        Name text NOT NULL,
                                        Type text,
                                        Date of Purchase text,
                                        Price integer
                                    ); """  
         

    conn = create_connection(database)
    deletion = input("Do you wish to delete data or enter data? Y/N")
    if deletion == "n":
        nid = input("Enter Name of item:\n")
        tid = input("Enter Type of item:\n")
        did = input("Enter DoP of item:\n")
        pid = input("Enter Price of item:\n")
        if conn is not None:
            table(conn, tableC)
            with conn:
                addInfo(conn,nid,tid,did,pid)
        else:
            print("Error with connection to database!")
    else:
        deleteK = input("Enter Row id of entry you want to delete.")
        if conn is not None:
            table(conn, tableC)
            with conn:
                delInfo(conn, deleteK)
                
if __name__ == '__main__':
    main()