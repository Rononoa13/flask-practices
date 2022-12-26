import os

# from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

from flask_sqlalchemy import SQLAlchemy
# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
# ensure database sqlite 
app.config['SECRET_KEY'] = 'test'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///birthdays.db'
# Configure CS50 Library to use SQLite database
db = SQLAlchemy(app)
# db = SQL("sqlite:///birthdays.db")

# ------------------------------------------
# Models
#----------------------------------------------
class Birthdays(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    month = db.Column(db.Integer)
    day = db.Column(db.Integer)

    def __repr__(self) -> str:
        return f"Item {self.name}"

db.init_app(app)

with app.app_context():
    db.create_all()

# ------------------------------------------
# Routes
#----------------------------------------------

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database

        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html

        birthdays = Birthdays.query.all()
        return render_template("index.html", birthdays=birthdays)
