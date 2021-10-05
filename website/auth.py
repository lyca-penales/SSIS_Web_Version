from flask import Blueprint
from flask import redirect, url_for, render_template

#Create a Blueprint Instance
auth = Blueprint('auth', __name__)

#Create a route decorator
@auth.route("/login/<name>")
def login(name):
    return render_template("login.html", content = "Testing")
