from flask import Blueprint, render_template


books_ctrl = Blueprint("books", __name__)

@books_ctrl.route("/")
def list():
    return render_template("books/list.html")


@books_ctrl.route("/<int:id>")
def getItem(id:int):
    return render_template("books/detail.html", id=id)