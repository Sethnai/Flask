from flask import Flask

app = Flask(__name__)

@app.route("/")
def homePage():
    return "<h1> Welcome To My Home Page </h1>"

@app.route("/aboutus")
def message():
    return "<B> Hello</b> <u>My Friends</u>"

@app.route("/nbs")
def boom():
    return "Welcome to NBS"

app.run()