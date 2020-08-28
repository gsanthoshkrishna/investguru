from flask import Flask, render_template, flash, request, url_for, redirect,session
from dbconnection import executeQuery
from dbconnection import insertDailyData
app = Flask(__name__)
app.config['SECRET_KEY']='sample'

@app.route("/")
def initial():
    res=executeQuery()
    cur=[]
    for i in res:
        cur.append([i[0].upper(),round(((i[1])/i[2])*100)])
    print(cur)
    insertDailyData()
    return render_template("index.html",cur=cur,len=len(cur))
if __name__ == "__main__":
    app.secret_key="dwqwfewfwqdqw"
    app.run(host="0.0.0.0", port="8222")
