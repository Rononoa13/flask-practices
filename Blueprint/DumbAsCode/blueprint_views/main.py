from flask import Flask, render_template
from home import home

app = Flask(__name__)
app.register_blueprint(home)

app.route('/user')
def user():
    return render_template('user.html')

if __name__ == "__main__":
    app.run(debug=True)