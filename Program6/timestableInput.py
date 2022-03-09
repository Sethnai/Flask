from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def homePage():

    return render_template("inputForm.html")

@app.route("/data", methods=["POST"])
def process():

    A=int(request.form["num1"])
    B=int(request.form["num2"])

    return render_template("timestable.html",T=A,R=B)

app.run(debug=True)