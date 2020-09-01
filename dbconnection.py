import pymysql

def executeQuery():
    db = pymysql.connect(host="172.18.0.2",    
                        user="root", 
                        password="Pass@123",        
                        database="murthy")       
    cur = db.cursor()
    cur.execute("SELECT name,value,target FROM invest_data")
    res=cur.fetchall()
    return res
def insertDailyData():
    db = pymysql.connect(host="172.18.0.2",    
                        user="root", 
                        password="Pass@123",        
                        database="murthy")       
    cur = db.cursor()
    history_datav = getCSVData()
    #TODO insert the values from csv data
    sql = "INSERT INTO history_data VALUES('SBICARD','EQ','824','846','823.55','838.9','837','819.7','2309206','1931891501.2','2020-08-28','78166')"
    cur.execute(sql)
    db.commit()
    print(cur.rowcount, "record inserted.")
    
#TODO Get the values from downloaded csv.
def getCSVData():
    test = 'nothingtosomething'
    return
