from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def grant():
    return render_template('home.html')

@app.route("/viewrecords")
def view():
    return render_template('viewrecords.html')

