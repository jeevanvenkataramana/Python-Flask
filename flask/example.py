from flask import Flask, render_template, url_for
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
def home():
    return render_template('home.html',posts=posts)

@app.route("/view")
def access():
    return render_template('view.html',title='Jeevan')

