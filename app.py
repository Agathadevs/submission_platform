import flask
from flask import (
    render_template,
    redirect,
    request
)

import sqlite3

try:
    db = sqlite3.connect('customers.db')
    cursor = db.cursor()

except Exception as e:
    print(e)

app=flask.Flask(__name__)

@app.route("/")
def register():
    return render_template("index.html")

@app.route("/register.html",methods=['GET', 'POST'])
def register_():

    if request.method=="POST":
        return '恭喜{}註冊成功!'.format(request.values['email'])
    
    return render_template("register.html")

@app.route("/login.html",methods=['GET', 'POST'])
def login_():

    if request.method=="POST":
        return '恭喜{}註冊成功!'.format(request.values["email"])
    
    return render_template("login.html")

@app.route("/Contribute.html",methods=['GET', 'POST'])
def contribute_():
    return render_template("Contribute.html")

if __name__ == '__main__':
    app.debug = True
    app.run()