import pymysql

def executeQuery():
    db = pymysql.connect(host="localhost",    
                        user="root", 
                        password="Sairf529*",        
                        database="murthy")       
    cur = db.cursor()
    cur.execute("SELECT * FROM invest_data")
    res=cur.fetchall()
    return res

