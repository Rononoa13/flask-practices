from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Create a flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'test'

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


# Create a route decorator
@app.route("/")
def index():
    first_name = "David"
    bold_text = "strong tag gives a <strong>BOLD</strong> text"
    favourite_pizza = ["margerita", "Pinapple", "Mushroom", 13]
    return render_template(
        "index.html",
        first_name=first_name,
        bold_text=bold_text,
        favourite_pizza=favourite_pizza)


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name)

# Create Name page
@app.route("/name", methods=['GET', 'POST'])
def name():
    name = None
    form = NameForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('nameForm.html', name=name, form=form)


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
