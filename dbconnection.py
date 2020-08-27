import pymysql

def executeQuery():
    db = pymysql.connect(host="mysql-server",    
                        user="root", 
                        password="Pass@123",        
                        database="murthy")       
    cur = db.cursor()
    cur.execute("SELECT name,value,target FROM invest_data")
    csv_url = "https://www1.nseindia.com/content/historical/EQUITIES/2020/AUG/cm27AUG2020bhav.csv.zip"
    req = requests.get(csv_url)
    print(req)
    res=cur.fetchall()
    return res

