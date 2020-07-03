from flask import Flask, render_template, flash, request, url_for, redirect,session
from dbconnection import executeQuery
app = Flask(__name__)
app.config['SECRET_KEY']='sample'
@app.route("/")
def initial():
    res=executeQuery()
    cur=round(((res[0][1])/res[0][3])*100)
    return render_template("index.html",cur=cur)
if __name__ == "__main__":
    app.secret_key="dwqwfewfwqdqw"
    app.run(debug=True)