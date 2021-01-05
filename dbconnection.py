import csv
import pymysql,json
from zipfile import ZipFile
from datetime import datetime
from datetime import timedelta
import urllib.request

with open('conf.json', 'r') as f:
    conf_dict = json.load(f)

sqlserver = conf_dict['sqlhost']
print("SQL:"+sqlserver)

def executeQueryAll():
    db = pymysql.connect(host=sqlserver,    
                        user="root", 
                        password="Pass@123",        
                        database="murthy")       
    cur = db.cursor()
    cur.execute("SELECT name,value,target FROM invest_data")
    res=cur.fetchall()
    cur.execute("SELECT name,value,target FROM invest_data WHERE tag='short'")
    short=cur.fetchall()
    cur.execute("SELECT name,value,target FROM invest_data WHERE tag='long'")
    lng=cur.fetchall()
    cur.execute("SELECT tag as name,sum(value) as 'value',sum(target) as 'target' FROM invest_data group by tag")
    axisemi=cur.fetchall()
    return res,short,lng,axisemi
    
def executeQuery(qry):
    db = pymysql.connect(host=sqlserver,    
                        user="root", 
                        password="Pass@123",        
                        database="murthy")       
    cur = db.cursor()
    cur.execute(qry)
    axisemi=cur.fetchall()
    return axisemi

def getHoldings(script,sort_key):
    #TODO change the below query for scripts
    srch_qry = "select sd.name,sd.name,sd.units,sd.avg_value,sd.current_value,ROUND(sd.units * sd.avg_value,2) as invested,ROUND(sd.units * sd.current_value,2) tot_current_value,sd.perc_change,sd.amt_change,tr.target_perc_reached from script_details sd , tr_targets tr where sd.name = tr.script_id and sd.name like '%"+script+"%' order by "+sort_key+" desc"
    if script == "pending":
        srch_qry = "select name,quantity,price,current_value,notes from pending_trades"
    if script == "nothing":
        srch_qry = "select sd.name,sd.name,sd.units,sd.avg_value,sd.current_value,ROUND(sd.units * sd.avg_value,2) as invested,ROUND(sd.units * sd.current_value,2) tot_current_value,sd.perc_change,sd.amt_change,tr.target_perc_reached from script_details sd , tr_targets tr where sd.name = tr.script_id  order by "+sort_key+" desc"
    print("srchQry:"+srch_qry)
    return executeQuery(srch_qry)


def insertDailyData():
    latestDate = datetime.now()
    print(latestDate.strftime('%H'))

    print('--------------------')
    print(latestDate.date())
    print(latestDate.date() > (datetime.now()).date())
    print((datetime.now()).date())
    print('--------------------')
    
    db = pymysql.connect(host=sqlserver,    
                        user="root", 
                        password="Pass@123",        
                        database="murthy")       
    cur = db.cursor()
    cur.execute("select max(STR_TO_DATE(TIMESTAMP,'%d-%b-%Y')) AS latestDate FROM history_data")
    res=cur.fetchall()
    if(res[0][0] != None):
        print("LatestDate:")
        print(res[0][0])
        latestDate = datetime.strptime(res[0][0], '%Y-%m-%d')
    else:
        latestDate = latestDate + timedelta(days=-8)
    latestDate = latestDate + timedelta(days=1)

    if latestDate.date() < (datetime.now()).date():
        print('inserting history')
        #return
    else:
        if int(latestDate.strftime('%H')) < 16 :
            print('exiting as < 8PM')
            return

    #Skip latest data is yesterdays.
    
    
    
    dt_obj = latestDate#datetime.strptime(latestDate, "%Y-%m-%d %H:%M:%S")
    zip_file = download_zip(dt_obj)
    #If no data available/ market holiday. insert one record.
    if(zip_file == 'NoData'):
        sql = "INSERT INTO history_data(TIMESTAMP) VALUES(%s)"
        cur=db.cursor()
        cur.execute(sql,dt_obj.strftime('%d-%b-%Y'))
        db.commit()
        print(cur.rowcount, "record inserted.")
        return


    
    print('unzipping file')
    csvfile = unzipcsv(zip_file)
    cur.close()


    history_data = getCSVData(csvfile)
    #print(history_data)
    #TODO insert the values from csv data
    #sql = "INSERT INTO history_data(SYMBOL,SERIES,OPEN,HIGH,LOW,CLOSE,LAST,PREVCLOSE,TOTTRDQTY,TOTTRDVAL,TIMESTAMP,TOTALTRADES,col1,col2) VALUES('SBICARD','EQ','824','846','823.55','838.9','837','819.7','2309206','1931891501.2','2020-08-28','78166')"
    #sql = "INSERT INTO history_data(SYMBOL,SERIES,OPEN,HIGH,LOW,CLOSE,LAST,PREVCLOSE,TOTTRDQTY,TOTTRDVAL,TIMESTAMP,TOTALTRADES,col1,col2) VALUES(%s,%s,'0.012','0.012','0.012','0.012','0.012','0.012','0.012','0.012',%s,'0.012',%s,%s)"
    sql = "INSERT INTO history_data(SYMBOL,SERIES,OPEN,HIGH,LOW,CLOSE,LAST,PREVCLOSE,TOTTRDQTY,TOTTRDVAL,TIMESTAMP,TOTALTRADES,col1,col2) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #sql = "INSERT INTO history_data(SYMBOL,TOTTRDVAL,TIMESTAMP,TOTALTRADES,col1) VALUES(%s,%s,%s,%s,%s)"
    cur=db.cursor()
    for row in history_data:
        cur.execute(sql,row)
        
    db.commit()

    #Inserting data same into    
    print(cur.rowcount, "record inserted.")
    cur=db.cursor()
    sql = "update history_data set col2 = TRUNCATE(((CLOSE-OPEN)/OPEN)*100,2) WHERE TIMESTAMP='"+dt_obj.strftime('%d-%b-%Y')+"'"
    cur.execute(sql)
    db.commit()

    sql = "truncate today_values"
    cur.execute(sql)
    db.commit()

    sql = "insert into today_values select * from history_data WHERE TIMESTAMP='"+dt_obj.strftime('%d-%b-%Y')+"'"
    cur.execute(sql)
    db.commit()

    sql = "update script_details sd, today_values tv set sd.current_value = tv.CLOSE where tv.SYMBOL = sd.name AND tv.SERIES = 'EQ'"
    cur.execute(sql)
    db.commit()

    #Updating %ch in script details.
    sql = 'update script_details set perc_change = ((current_value - avg_value)/ avg_value)*100 , amt_change = (current_value - avg_value)*units'
    cur.execute(sql)
    db.commit()

    sql = 'UPDATE script_details SET low_value = CASE WHEN current_value < low_value THEN current_value ELSE low_value END, high_value = CASE WHEN current_value > high_value THEN current_value ELSE high_value END'
    cur.execute(sql)
    db.commit()

    

def updateQuery(qry):
    db = pymysql.connect(host=sqlserver,    
                        user="root", 
                        password="Pass@123",        
                        database="murthy")
    cur=db.cursor()
    cur.execute(qry)
    db.commit()
    print(cur.rowcount, "record updated.")
    return

def insertQuery(qry,valuesList):
    cur=db.cursor()
    cur.execute(qry+" values(%s)",valuesList)
    db.commit()
    print(cur.rowcount, "record inserted.")
    return

def download_zip(from_date):
    x = from_date #datetime.datetime.now()
    date_of_file = x.strftime('%d')
    month_of_file = x.strftime('%b').upper()
    filename = "cm"+str(date_of_file)+month_of_file+str(x.year)+"bhav.csv.zip"
    print("Downloading report file "+filename)
    print(filename)
    url = "https://www1.nseindia.com/content/historical/EQUITIES/"+str(x.year)+"/"+month_of_file+"/"+filename
    #url = "https://archives.nseindia.com/content/historical/EQUITIES/"+str(x.year)+"/"+month_of_file+"/"+filename
    save_path = "raw_data/"+filename
    try:
        resp = urllib.request.urlopen(url,timeout=30)
        with resp as dl_file:
            print(dl_file.status)
            with open(save_path, 'wb') as out_file:
                out_file.write(dl_file.read())
    except Exception as e:
        if str(e).find('FileNotFoundError'):
            print("file not found exception"+str(e))
            return 'NoData'
            
    
    return save_path


def unzipcsv(filename):
    import zipfile
    csvfile = filename.replace('.zip','')
    print("exctracting zip file "+filename)
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall("raw_data")
    
    print("Extracted csv"+csvfile)
    return csvfile


#TODO Get the values from downloaded csv.
def getCSVData(csvfile):
    history_data = []
    with open(csvfile, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        skiprow = 1
        for row in reader:
            history_data.append(row)
        return history_data

