# importing sqlite module
import sqlite3
  
# create connection to the database 
# geeks_database
connection = sqlite3.connect('data.db')


# create table named address of customers
# with 3 columns id , garbage , password

 # FOR DATA TABLE
connection.execute('''CREATE TABLE quickshare                    
         (ID INTEGER PRIMARY KEY    AUTOINCREMENT,
         LITERAL           TEXT    NOT NULL,
         PASSWORD           TEXT  );''')

# FOR LOGS
connection.execute('''CREATE TABLE LOG                            
(POINTER INTEGER);

''')

connection.execute('INSERT INTO LOG(POINTER) VALUES(0);')       # INITIAL VALUE

connection.commit()
# close the connection
connection.close()


