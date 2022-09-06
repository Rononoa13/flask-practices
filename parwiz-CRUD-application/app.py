from crypt import methods
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'Secret Key'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



db = SQLAlchemy(app)

class Employee(db.Model):
    __tablename__ = "employee"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

@app.route("/")
def index():
    all_data = Employee.query.all()
    return render_template("index.html", employees=all_data)

@app.route('/insert', methods=["POST"])
def insert():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
    
    my_employee = Employee(name, email, phone)
    db.session.add(my_employee)
    db.session.commit()

    flash('Employee added successfully')
    return redirect(url_for('index'))

# Update employee
@app.route('/update', methods=["GET", "POST"])
def update():
    if request.method == "POST":
        update_employee = Employee.query.get(request.form.get('id'))
        # print(update_employee)
        update_employee.name = request.form['name']
        update_employee.email = request.form['email']
        update_employee.phone = request.form['phone']

        db.session.commit()
        flash('Employee updated successfully')

        return redirect(url_for('index'))
        
# delete employee
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Employee.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash('Employee deleted successfully')
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
