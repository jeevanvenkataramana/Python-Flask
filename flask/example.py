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
def view():
    return render_template('view.html',posts=posts, title='View')

@app.route("/accesscontrol")
def access():
    return render_template('accesscontrol.html',title='Jeevan')

