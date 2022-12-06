from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from os import path


DB_NAME = "database.db"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_test.db'
db = SQLAlchemy(app)


# -----------------------------------------
# Models
# -----------------------------------------

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

def create_database(app):
        db.create_all()
        print("Database Created")

# -----------------------------------------
# Home
# -----------------------------------------

@app.route("/")
def home():
    return render_template("home.html")

# -----------------------------------------
# Authentication
# -----------------------------------------

@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    return "<h1> Logout </h1>"

@app.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater that 3 characters', category='error')
        elif len(first_name) < 2:
            flash('First must be greater that 1 characters', category='error')
        elif password1 != password2:
            flash('Password don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            # Add user to the database
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            
            db.session.add(new_user)
            db.session.commit()
            
            flash('Account Created!', category='success')
            return redirect(url_for('home'))
    return render_template("sign_up.html")

if __name__ == "__main__":
    app.run(debug=True)
    