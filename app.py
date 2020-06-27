from flask import Flask, render_template, flash, request, url_for, redirect,session
app = Flask(__name__)
app.config['SECRET_KEY']='sample'
@app.route("/")
def initial():
    return render_template("index.html")
if __name__ == "__main__":
    app.secret_key="dwqwfewfwqdqw"
    app.run(debug=True)