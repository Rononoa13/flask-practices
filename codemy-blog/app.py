from flask import Flask, render_template

# Create a flask instance
app = Flask(__name__)

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

#  Create custom Error pages


# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Internal server URL
@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500
