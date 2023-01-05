# server.py
from flask import Flask, render_template
from src.controllers.books import books_ctrl
from src.controllers.authors import authors_ctrl

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

app.register_blueprint(books_ctrl, url_prefix="/books")
app.register_blueprint(authors_ctrl, url_prefix="/authors")

if __name__ == "__main__":
    app.run(debug=True)