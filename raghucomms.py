import csv
import pymysql
from datetime import datetime
from datetime import timedelta
import urllib.request

def searchUser(custId):
      
    srch_qry = "select c.customer_id,c.name,c.contact,p.name,p.isp_package_name,t.tr_date,t.validity,t.payment_mode,t.payment_status,t.receipt_no from customer c,packages p,customer_transactions t where t.cust_id = c.customer_id and t.package_id = p.id and c.customer_id like '%"+custId+"%' "
    print(srch_qry)
    return executeQuery(srch_qry)
    
def executeQuery(qry):
    db = pymysql.connect(host="172.18.0.2",    
                        user="root", 
                        password="Pass@123",        
                        database="raghu_comms") 

    cur = db.cursor()
    cur.execute(qry)
    res=cur.fetchall()
    return res


