from flask import Flask , render_template,request , redirect,session
from db import Database
import myapi
from myapi import API

app = Flask(__name__)
app.secret_key = '1234'
dbo = Database() #database related code in this class in db file
api0 = API()

@app.route('/')
def index():
    return render_template('login.html')

@app.route("/Register")
def Register():
    return render_template('register.html')

@app.route("/perform_registration",methods=['post'])
def perform_registration():
    #accessing data from client using html form
    name = request.form.get('username')
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    #adding that data to data base (users.json)
    response = dbo.insert(name , email , password)
    #if registration success load the login page
    if response:
        return render_template('login.html',message = "Registration Successful.Kindly Login to proceed.")
    else:
        return render_template('register.html' , message = "User already exists with this email.")

@app.route('/perform_login' , methods = ['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    # checking that data in our database (users.json)
    response = dbo.check(email , password)
    if response:
        session['logged_in'] = 1
        return redirect('/profile')
    else:
        return render_template('login.html' , message = 'Incorrect Email Password')

@app.route('/profile')
def profile():
    if session:
        return render_template('profile.html')
    else:
        return redirect('/')

@app.route("/NER")
def ner():
    if session:
        return render_template('NER.html')
    else:
        return redirect('/')

@app.route("/perform_ner" ,methods = ['post'])
def perform_ner():
    if session:

        text = request.form.get('ner_text')
        response = api0.ner(text)
        return render_template('NER.html',result = response)
    else:
        return redirect('/')

app.run(debug = True)
