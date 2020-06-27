import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root", 
                     password="1234",        # your username
                     db="personal")        # name of the data base


cur = db.cursor()

cur.execute("SELECT * FROM YOUR_TABLE_NAME")

for row in cur.fetchall():
    print(row[0])
print("success")

db.close()