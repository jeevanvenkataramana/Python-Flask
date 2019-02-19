from flask import Flask, render_template
app = Flask(__name__)
posts=[
	{
	'Name':'Jeevan Venkataramana',
	'Email':'jeevan.venkataramana@gmail.com'
	},
	{
	'Name':'Pavan',
	'Email':'pavan.haravu@gmail.com'
	}
	]
@app.route("/")
def grant():
    return render_template('home.html',posts=posts)

@app.route("/viewrecords")
def view():
    return render_template('viewrecords.html')

