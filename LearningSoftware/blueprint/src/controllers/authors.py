from flask import Blueprint, render_template


authors_ctrl = Blueprint("authors", __name__)

@authors_ctrl.route("/")
def list():
    return render_template("authors/list.html")


@authors_ctrl.route("/<int:id>")
def getItem(id:int):
    return render_template("authors/detail.html", id=id)