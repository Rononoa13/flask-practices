from flask import Blueprint, render_template

# Define a blueprint
second = Blueprint(
    "second", __name__,
    template_folder="templates",
    static_folder="static"
)

@second.route("/home")
def home():
    return render_template("home.html")