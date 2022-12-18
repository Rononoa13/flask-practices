from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create a flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'test'
# Add database to app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# Initialize the Database
db = SQLAlchemy(app)

# Create Model
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200), nullable=False)
	email = db.Column(db.String(120), unique=True)
	date_added = db.Column(db.DateTime, default=datetime.utcnow)

	# Create a String
	def __repr__(self) -> str:
		  return '<Name %r>' % self.name

db.init_app(app)
with app.app_context():
    db.create_all()

# Create a User Form
class UserForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired()])
	email = StringField("Email", validators=[DataRequired()])
	submit = SubmitField("Submit")

# Create a FORM Class
class NameForm(FlaskForm):
    name = StringField("Enter your name", validators=[DataRequired()])
    submit = SubmitField('Submit')
    #  DateField
	# DateTimeField
	# DecimalField
	# FileField
	# HiddenField
	# MultipleField
	# FieldList
	# FloatField
	# FormField
	# IntegerField
	# PasswordField
	# RadioField
	# SelectField
	# SelectMultipleField
	# SubmitField
	# StringField
	# TextAreaField

	## Validators
	# DataRequired
	# Email
	# EqualTo
	# InputRequired
	# IPAddress
	# Length
	# MacAddress
	# NumberRange
	# Optional
	# Regexp
	# URL
	# UUID
	# AnyOf
	# NoneOf

'''
Search filters in jinja website.
safe
capitalize
lower
upper
title
trim
striptags
'''
# --------------------------------- Routes ------------------------------>

# Create a route decorator
@app.route("/")
def index():
    # first_name = "David"
    # bold_text = "strong tag gives a <strong>BOLD</strong> text"
    # favourite_pizza = ["margerita", "Pinapple", "Mushroom", 13]
	favorite_pizza = ["Pineapple", "Bacon"]
	flash("Welcome to our website!")
	return render_template("index.html", favorite_pizza=favorite_pizza)

# Create User page
@app.route("/user/add", methods=['GET', 'POST'])
def add_user():
	name = None
	form = UserForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is None:
			user = User(name=form.name.data, email=form.email.data)
			db.session.add(user)
			db.session.commit()
		name = form.name.data
		form.name.data = ''
		form.email.data = ''
		flash("User Added Successfully")
	our_users = User.query.order_by(User.date_added)
	return render_template("add_user.html", form=form, name=name, our_users=our_users)

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name)

# Create Name page
@app.route("/name", methods=['GET', 'POST'])
def name():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
		flash("Form Successfully Submitted!")
	return render_template("nameForm.html", form=form, name=name)

#  Create custom Error pages
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Internal server URL
@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500

if __name__ == '__main__':
    app.run(debug=True)

# Create a FORM Class
