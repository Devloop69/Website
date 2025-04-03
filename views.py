from flask import Blueprint, render_template, request, flash

views = Blueprint(__name__,"views")
@views.route('/')

def home():
    flash("Login")
    return render_template("Web.html")


@views.route('/profile', methods=["POST","GET"])
def profile():
    try:
        username = str(request.form['Username'])
        flash('Hi ' + username + '!')
    except:
        flash("Hi again!")
    return render_template("Profile.html")

@views.route('/calc')
def calculator():
    flash("Calculator")
    return render_template("a.html")

@views.route('/todo')
def todo():
    return render_template("Todo.html")

@views.route('/rotate')
def rotate():
    return render_template("rotate.html")