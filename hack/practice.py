from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
import csv

engine = create_engine('sqlite:///database.db', echo=True)

app = Flask(__name__)

with open('test.csv', mode = 'r') as infile:
    reader = csv.reader(infile)
    with open('dictionary.csv', mode ='w') as outfile:
        writer = csv.writer(outfile)
        dictionary = {rows[0]:rows[2] for rows in reader}

global userstate


def isLoggedIn():
    if session.get('logged_in'):
        return True
    else:
        return False
    
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('home.html')
 
@app.route('/111')
def intro():
    if isLoggedIn():
        return render_template('csc111Home.html')
    else:
        return "Sorry! You aren't enrolled in that class."

@app.route('/212')
def dataStructures():
    if isLoggedIn():
        return render_template('csc212Home.html')
    else:
        return "Sorry! You aren't enrolled in that class."

@app.route('/231')
def microprocessors():
    if isLoggedIn():
        return render_template('csc231Home.html')
    else:
        return "Sorry! You aren't enrolled in that class."

@app.route('/250')
def theory():
    if isLoggedIn():
        return render_template('csc250Home.html')
    else:
        return "Sorry! You aren't enrolled in that class."

@app.route('/homeMenu')
def homeMenu():
    if isLoggedIn():
        return render_template('home.html')
    else:
        return "Sorry! You aren't enrolled in that class."

@app.route('/noTAs')
def noTas():
    if isLoggedIn():
        return render_template('pageError.html')
    else:
        return "Sorry! You aren't enrolled in that class."

@app.route('/alternateTAs')
def alternateTas():
    if isLoggedIn():
        return render_template('pageError2.html')
    else:
        return "Sorry! You aren't enrolled in that class."

@app.route('/contacts')
def contacts():
    if isLoggedIn():
        return render_template('contacts.html')
    else:
        return "Sorry! You aren't enrolled in that class."


@app.route('/login', methods=['POST'])
def do_admin_login():

    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
    POST_ACTIVITY = "admin"

    Session = sessionmaker(bind=engine)
    s = Session()

    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
    result = query.first()

    if(dictionary.get(POST_USERNAME) == 'admin'):
        userstate = "admin"
    else:
        userstate = "student"
    
    if result:
        session['logged_in'] = True
        if(userstate == "admin"):
            print("admin!!!")
        else:
            print("not admin...")

    else:
        flash('wrong password!')
    return home()
 
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
    
