from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY']='586cf3dd15dd5dd52a77ea3c1604ddf1'


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


@app.route("/register")
def register():
	form = RegistrationForm()
	return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
        form = LoginForm()
        return render_template('login.html', title='Login', form=form)

