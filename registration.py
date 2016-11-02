from flask import Flask, render_template, request, flash, redirect
import re

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASS_REGEX = re.compile(r'.*[A-Z].*[0-9].*|.*[0-9].*[A-Z]')
BDAY_REGEX = re.compile(r'[0-9]{2}/[0-9]{2}/[0-9]{4}')
@app.route("/")
def registration_form():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit_form():
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    password = request.form['password']
    confirmation = request.form['confirm']
    birthdate = request.form["birthdate"]
    canGoOn = True
    if (len(email) < 1):
        flash("Email cannot be empty!")
        canGoOn = False
    if (not EMAIL_REGEX.match(request.form['email'])):
        flash("Not a real email address!")
        canGoOn = False
    if (len(first_name) < 1):
        flash("First Name cannot be empty!")
        canGoOn = False
    if (not first_name.isalpha()):
        flash("First Name cannot contain numbers!")
        canGoOn = False
    if (not last_name.isalpha()):
        flash("Last Name cannot contain numbers!")
        canGoOn = False
    if (len(last_name) < 1):
        flash("Last Name cannot be empty!")
        canGoOn = False
    if (len(password) == 0):
        flash("Password cannot be empty!")
        canGoOn = False
    if (len(password) < 8):
        flash("Password cannot be less than 8 characters!")
        canGoOn = False
    if (not PASS_REGEX.match(password)):
        flash("Password needs to have an uppercase and number")
    if (len(confirmation) < 1):
        flash("Password Confirmation cannot be empty!")
        canGoOn = False
    if (confirmation != password):
        flash("Passwords don't match!")
        canGoOn = False
    if (not BDAY_REGEX.match(birthdate)):
        flash("Not a valid birthdate!")
        canGoOn = False
    if (BDAY_REGEX.match(birthdate)):
        bday = birthdate.split("/")
        year = int(bday[len(bday) - 1])
        print year
        if (year > 2016):
            flash("Not a valid birthdate!")
            canGoOn = False
    if (canGoOn == False):
        return redirect("/")
    else:
        flash("Success!")
        return redirect("/")

app.run(debug=True)
