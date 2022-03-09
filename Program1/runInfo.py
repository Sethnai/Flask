from flask import Flask, render_template
app=Flask(__name__)

@app.route("/info")
def homePage():
    return render_template("information.html",na="Shafeeq",addr="Manchester")
    
app.run()