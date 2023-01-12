# importing sqlite module
import sqlite3
  
# create connection to the database 
# geeks_database
connection = sqlite3.connect('data.db')


# create table named address of customers
# with 3 columns id , garbage , password
connection.execute('''CREATE TABLE quickshare
         (ID INTEGER PRIMARY KEY    AUTOINCREMENT,
         LITERAL           TEXT    NOT NULL,
         PASSWORD           TEXT  );''')
connection.commit()
# close the connection
connection.close()