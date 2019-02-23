from flask import Flask, render_template, url_for, flash, redirect
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
def view():
    return render_template('view.html',title='Jeevan')


@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
    	flash(f'Account created for {form.username.data}!', 'success')
    	return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__=='__main__':
    app.run(debug=True)
