import sqlite3 as sql

def main():
    conn = sql.connect('data.db')                                                   #CONNECTING_TO_DATABASE_FILE
    cur = conn.cursor()                                                             #CREATING_CURSOR


    print(cur.execute('insert into quickshare values (2,"Bishal" , "abcd")'))       #EXECUTING_COMMANDS
    respond = cur.execute('select * from quickshare')
    print(respond.fetchall())
    

    conn.commit()                                                                   #COMMITING_ACTIONS
    conn.close()                                                                    #CLOSING_CONNECTION


'''
def makeConnection():
    conn = sql.connect('data.db')                                                   #CONNECTING_TO_DATABASE_FILE
    cur = conn.cursor()   

def closeConnection(conn):
    conn.commit()                                                                   #COMMITING_ACTIONS
    conn.close()  
'''


def retriveData(id):
    conn = sql.connect('data.db')                                                   
    cur = conn.cursor()   

    respond =  cur.execute(f'SELECT * FROM quickshare WHERE ID={id}').fetchone()
   
    conn.commit()                                                                      #COMMITING_ACTIONS
    conn.close() 

    return list(respond)[1]   


def executeQuery(query):
    conn = sql.connect('data.db')                                                   
    cur = conn.cursor()   

    respond =  cur.execute(query).fetchall()
   
    conn.commit()                                                                   #COMMITING_ACTIONS
    conn.close() 
    return respond


def editData(id):
    pass  

def insertData( id , data , password):
    conn = sql.connect('data.db')                                                   
    cur = conn.cursor()   

    respond =  cur.execute(f"insert into quickshare (ID , LITERAL , PASSWORD) values ({id},{data},{password})")
   
    conn.commit()                                                                     
    conn.close() 

    

if __name__=="__main__":                                                            #CALLING_FROM_OUTSIDE_DOESNOTWORK_HERE
    # main()                                                                        #MAIN_LABORATORY
    # print(retriveData(2)  )                                                       #GIVING_DATA_OF_SPECIFIC_ID
    print(executeQuery('SELECT LITERAL FROM quickshare'))                               #GIVING_EXPEXTED_RESULT
    # insertData(3,'data','asdf')


