import pymongo
from pymongo import MongoClient
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
import datetime
import pytz

app = Flask(__name__)
app.config['SECRET_KEY']='586cf3dd15dd5dd52a77ea3c1604ddf1'

posts=list()




bdb_root_url = 'http://localhost:9984'
bdb = BigchainDB(bdb_root_url)
client = pymongo.MongoClient()
db=client.user_data


posts=list()

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/view")
def view():
    return render_template('view.html',title='View Page')

@app.route("/dashboard")
def dashboard():
    return render_template('userdashboard.html',title='Your Dashboard', posts=posts)

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        sample=generate_keypair()
        private=sample.private_key
        public=sample.public_key
        transactions_created=list()
        transactions_owned=list()
        data={'username':form.username.data,'email':form.email.data,'password':form.password.data,'private':private,'public':public,'transactions_created':transactions_created,'transactions_owned':transactions_owned}
        flash(f'Account created for {form.username.data}!', 'success')
        result=db.reg_details.insert_one(data)
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        records=db.reg_details.find( { "$and": [ {"email":form.email.data},{"password":form.password.data} ] } )
        if(records.count()==1):
            flash('You have been logged in!', 'success')
            posts.clear()
            temp=dict()
            temp.clear()
            temp['type']='Transactions Created'
            for record in records:
                temp['ids']=list()
                for i in range(len(record['transactions_created'])):
                    temp['ids'].append(record['transactions_created'][i])
                posts.append(temp)
                print(posts)
            temp2=dict()
            temp2.clear()
            temp2['type']='Transactions Owned'
            for record in records:
                temp2['ids']=list()
                for i in range(len(record['transactions_owned'])):
                    temp2['ids'].append(record['transactions_owned'][i])
            posts.append(temp2)
            print(posts)
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__=='__main__':
    app.run(debug=True)
