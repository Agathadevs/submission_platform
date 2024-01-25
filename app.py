import flask
from flask import (
    render_template,
    redirect
)

app=flask.Flask(__name__)

@app.route("/")
def register():
    return render_template("index.html")

@app.route("/register")
def register_():
    return render_template("register.html")

@app.route("/login")
def login_():
    return render_template("login.html")

@app.route("/contribute")
def contribute_():
    return render_template("Contribute.html")

if __name__ == '__main__':
    app.debug = True
    app.run()