# pylint: disable=print-statement

from flask import Flask, render_template, redirect, request, session, flash
import re, datetime

app = Flask(__name__)
app.secret_key = "Secret"
@app.route("/", methods = ["GET"])
def index():
    return render_template("registration_form.html")
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

@app.route("/process", methods = ["POST"])
def process():
    first_name = request.form["first_name"]
    print first_name
    first_name =str(first_name)
    print first_name
    last_name = request.form["last_name"]
    email = request.form["email"]
    password = request.form["password"]
    password = str(password)
    print type(password)
    password_confirm = request.form["password_confirm"]
    password_confirm = str(password_confirm)

    if len(request.form["first_name"]) < 1:
        flash("First Name cannot be empty,")
        # return redirect("/")
    if len(request.form["last_name"]) < 1: 
        flash("Last Name cannot be empty,")
        # return redirect("/")
    if len(request.form["email"]) < 1:
        flash("Email cannot be empty,")
        # return redirect("/")
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Email is Invalid,")
        # return redirect("/")
    if len(request.form["password"]) < 8:
        flash("Password Must Contain More than 8 Characters,")
        # return redirect("/")
    if len(request.form["password"]) < 1:
        flash("Password Cannot be Empty,")
        # return redirect("/")
    if request.form["password_confirm"] != request.form["password"]:
        flash("Passwords Do Not Match Re-enter,")
        # return redirect("/")
    if request.form["birthdate"] > datetime.datetime.now():
        flash("Cannot Enter Date Before Today")
    for i in range(0,len(first_name)):
        if first_name[i] == "1" or first_name[i] == "2" or first_name[i] == '3' or first_name[i] == '4' or first_name[i] == '5' or first_name[i] == '6' or first_name[i] == '7' or first_name[i] == '8' or first_name[i] == '9' or first_name[i] == '0':
            flash("First Name cannot contain numbers")
    for i in range(0,len(last_name)):
        if last_name[i] == "1" or last_name[i] == "2" or last_name[i] == '3' or last_name[i] == '4' or last_name[i] == '5' or last_name[i] == '6' or last_name[i] == '7' or last_name[i] == '8' or last_name[i] == '9' or last_name[i] == '0':
            flash("First and/or Last Name cannot contain numbers")
    for i in range(0,len(password)):
        if password[i] == "1" or password[i] == "2" or password[i] == '3' or password[i] == '4' or password[i] == '5' or password[i] == '6' or password[i] == '7' or password[i] == '8' or password[i] == '9' or password[i] == '0':
            flash("Password must have at least 1 Number")
    for i in range(0,len(password)):
        if password[i].isupper():
            flash("Password must have at Least 1 Uppercase Letter")
    return redirect("/")

app.run(debug=True)