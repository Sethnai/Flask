from flask import Flask

app = Flask(__name__)

@app.route("/")
def homePage():
    return """
    <html>
    <center><h1> Welcome To The NBS Home Page </h1>
    <br>
    We are longest running building society in the UK</center>
    <br>
    <br>
    <a href="http://localhost:5000/team"><center> Who we are </center></a> <br>
    <a href="http://localhost:5000/services"><center> Our Services </center></a> <br>
    </html>
    """

@app.route("/team")
def message():
    return """
    <html>

    <h2><B><center><u>Meet Our Team</u></center></B></h2>
    <br>
    <h2> Introducing our lovely champions: </h2>
    <br>
    <ul>
        <li> Laura </li>
        <li> Hadyn </li>
        <li> Mimi </li>
    </ul>
    <br>
    <a href="http://localhost:5000"> Home </a>
    </html>
    """

@app.route("/services")
def boom():
    return """
    <html>
    <h1><center> Welcome to NBS </center></h1>
    <h2> We provide the following services: </h2>
    <br>
    <ul>
        <li> Open Account </li>
        <li> Deposit Money </li>
        <li> Withdraw Money </li>
    </ul>
    <br>
    <a href="http://localhost:5000"> Home </a>
    </html>
    """

app.run()