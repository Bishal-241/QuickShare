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


def retriveData(id , pswd):
    authenticated = False                                                              #DEFAULT_AUTHEN_STATE
    conn = sql.connect('data.db')                                                   
    cur = conn.cursor()   

    respond =  cur.execute(f'SELECT * FROM quickshare WHERE ID={id}').fetchone()

    conn.commit()                                                                      #COMMITING_ACTIONS
    conn.close() 

    if(list(respond)[2] == pswd):
        authenticated = True
        return list(respond)[1]                                                            # RETURNS DATA FROM[ID,LITERAL,PASSWORD]
    else:
        return 'Authetication Error or recoed not available'

    



def executeQuery(query):
    conn = sql.connect('data.db')                                                   
    cur = conn.cursor()   

    respond =  cur.execute(query).fetchall()
   
    conn.commit()                                                                   #COMMITING_ACTIONS
    conn.close() 
    return respond


def editData(id):
    pass  

def insertData(data , password):                                               # INSERT_DATA_CREATING_NEW_ROW
    conn = sql.connect('data.db')                                                   
    cur = conn.cursor()   
    id = list(cur.execute('select * from LOG').fetchone())[0] + 1 
    if (password == ""):
        password = 'default'
    respond =  cur.execute(f"insert into quickshare (ID , LITERAL , PASSWORD) values ({id},'{data}','{password}')")

    cur.execute(f'''UPDATE LOG
        SET POINTER = {id}
        ''')
        
    conn.commit()                                                                     
    conn.close() 
    return [id,data,password]


if __name__=="__main__":                                                            #CALLING_FROM_OUTSIDE_DOESNOTWORK_HERE
    # main()                                                                        #MAIN_LABORATORY
    # print(retriveData(11,'kingofwadia')  )                                                       #GIVING_DATA_OF_SPECIFIC_ID
    # print(executeQuery('SELECT * FROM quickshare'))                               #GIVING_EXPEXTED_RESULT
    print(insertData('Do u think the world is having Valentine week?',""))
    # executeQuery('DELETE  from quickshare WHERE ID = 21')                               #GIVING_EXPEXTED_RESULT

    # print(executeQuery('select * from quickshare'))
    # for i in range(1,3):                                                         #CONTINIOUS DATA ENTRY
    #     data = input(f"enter data[{i}]: ")
    #     password = input(f'enter password[{i}]')
    #     print(insertData(data,password))

    pass

