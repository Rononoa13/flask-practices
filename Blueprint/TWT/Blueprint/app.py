from flask import Flask, render_template

from second import second

app = Flask(__name__)
app.register_blueprint(second, url_prefix="")

@app.route("/")
def index():
    return "<h1> Test </h1>"

# Some Models Here


# Routes related to core functionalities


# Routes related to Profile Page


# Routes related to Products Page


# Routes related to Blog Page


# Routes related to Admin Page

if __name__ == "__main__":
    app.run(debug=True)