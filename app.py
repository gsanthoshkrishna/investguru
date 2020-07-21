from flask import Flask, render_template, flash, request, url_for, redirect,session
from dbconnection import executeQuery
app = Flask(__name__)
@app.route("/")
def initial():
    res,short,lng=executeQuery()
    cur=[]
    sh=[]
    ln=[]
    avg_long=avg_short=0
    for i in res:
        cur.append([i[0].upper(),round(((i[1])/i[2])*100)])
    for i in short:
        avg_short+=((i[1])/i[2])*100
        sh.append([i[0].upper(),round(((i[1])/i[2])*100)])
    avg_short=round(avg_short/len(short))
    for i in lng:
        avg_long+=((i[1])/i[2])*100
        ln.append([i[0].upper(),round(((i[1])/i[2])*100)])
    avg_long=round(avg_long/len(lng))
    return render_template("index.html",cur=cur,len=len(cur),avg_lg=avg_long,avg_shr=avg_short,lg=ln,shr=sh)
if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port="8222")
