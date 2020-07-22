import pymysql

def executeQuery():
    db = pymysql.connect(host="localhost",    
                        user="root", 
                        password="Sairf529*",        
                        database="murthy")       
    cur = db.cursor()
    cur.execute("SELECT name,value,target FROM invest_data")
    res=cur.fetchall()
    cur.execute("SELECT name,value,target FROM invest_data WHERE tag='short'")
    short=cur.fetchall()
    cur.execute("SELECT name,value,target FROM invest_data WHERE tag='long'")
    lng=cur.fetchall()
    return res,short,lng

