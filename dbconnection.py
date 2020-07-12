import pymysql

def executeQuery():
    db = pymysql.connect(host="mysql-server",    
                        user="root", 
                        password="Pass@123",        
                        database="murthy")       
    cur = db.cursor()
    cur.execute("SELECT * FROM invest_data")
    res=cur.fetchall()
    return res

