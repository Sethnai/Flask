from flask import Flask

app = Flask(__name__)

@app.route("/aboutus")
def message():
    return "Hello My Friends"

@app.route("/nbs")
def boom():
    return "Welcome to NBS"

app.run()