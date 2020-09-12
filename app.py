from flask import Flask, render_template, flash, request, url_for, redirect,session
from dbconnection import executeQuery
from dbconnection import insertDailyData
app = Flask(__name__)
app.config['SECRET_KEY']='sample'

@app.route("/")
def initial():
    es,short,lng=executeQuery()
    cur=[]
    sh=[]
    ln=[]
    avg_long=avg_short=0
    for i in res:
        cur.append([i[0].upper(),round(((i[1])/i[2])*100)])
    print(cur)
    insertDailyData()
    for i in short:
        avg_short+=((i[1])/i[2])*100
        sh.append([i[0].upper(),round(((i[1])/i[2])*100)])
    avg_short=round(avg_short/len(short))
    for i in lng:
        avg_long+=((i[1])/i[2])*100
        ln.append([i[0].upper(),round(((i[1])/i[2])*100)])
    avg_long=round(avg_long/len(lng))
    return render_template("index.html",cur=cur,len=len(cur))
if __name__ == "__main__":
    #app.secret_key="dwqwfewfwqdqw"
    app.run(host="0.0.0.0", port="8222")
