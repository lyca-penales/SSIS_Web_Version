from flask import Blueprint
from flask import redirect, url_for, render_template


#Create a Blueprint Instance
views = Blueprint('views', __name__)

#Create a route decorator
@views.route('/')
def ssis():
    return render_template("ssis.html", content = "Testing")

@views.route('/student')
def student():
    return render_template("student.html", content = "Testing")


@views.route('/course')
def course():
    return render_template("course.html", content = "Testing")   

@views.route('/college')
def college():
    return render_template("college.html", content = "Testing")   