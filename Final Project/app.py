import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash
from helpers import login_required
from datetime import date

# Configure application
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///Reservations.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    today = date.today()
    if request.method == "POST":
        notes = request.form.get('message')
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        subject = request.form.get('subject')
        if not name:
            error_statement = "please enter your name"
            return render_template("form.html", error_statement = error_statement, name=name, email=email, phone=phone, subject=subject, notes=notes)
        if not email:
            error_statement = "please enter your email"
            return render_template("form.html", error_statement = error_statement, name=name, email=email, phone=phone, subject=subject, notes=notes)
        if not phone:
            error_statement = "please enter your phone number"
            return render_template("form.html", error_statement = error_statement, name=name, email=email, phone=phone, subject=subject, notes=notes)
        if not subject:
            error_statement = "please enter the subject"
            return render_template("form.html", error_statement = error_statement, name=name, email=email, phone=phone, subject=subject, notes=notes)
        db.execute("INSERT INTO contact (name, email, phone, subject, notes, date) VALUES (?,?,?,?,?,?)  ",  name, email, phone, subject, notes, today)
        return redirect('/confirmation')
    else:
        return render_template("contact.html")

@app.route("/contact", methods=["POST"])
def form():
    today = date.today()
    if request.method == "POST":
        notes = request.form.get('message')
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        subject = request.form.get('subject')
        if not name:
            error_statement = "Please enter your name"
            return render_template("form.html", error_statement = error_statement, name=name, email=email, phone=phone, subject=subject, notes=notes)
        if not email:
            error_statement = "Please enter your email"
            return render_template("form.html", error_statement = error_statement, name=name, email=email, phone=phone, subject=subject, notes=notes)
        if not phone:
            error_statement = "Please enter your phone number"
            return render_template("form.html", error_statement = error_statement, name=name, email=email, phone=phone, subject=subject, notes=notes)
        if not subject:
            error_statement = "Please enter the subject"
            return render_template("form.html", error_statement = error_statement, name=name, email=email, phone=phone, subject=subject, notes=notes)
        db.execute("INSERT INTO contact (name, email, phone, subject, notes, Date) VALUES (?,?,?,?,?,?) ",  name, email, phone, subject, notes, today)
        return redirect('/confirmation')
    else:
        return render_template("contact.html")

@app.route("/confirmation")
def confirm():
    return render_template("confirmation.html")

@app.route("/reserve", methods=["GET", "POST"])
def reserve():
    today = date.today()
    if request.method == "POST":
        Date = request.form.get('date')
        title = request.form.get('title')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        time = request.form.get('time')
        email = request.form.get('email')
        phone = request.form.get('phone')
        party = request.form.get('party')
        notes = request.form.get('notes')
        if not Date:
            error_statement = "Please enter a date"
            return render_template("form1.html", error_statement = error_statement, title=title, fname=fname, lname=lname, time = time, email=email, phone=phone, party=party, notes=notes)
        if Date == "None":
            error_statement = "Please enter a date"
            return render_template("form1.html", error_statement = error_statement, title=title, fname=fname, lname=lname, time = time, email=email, phone=phone, party=party, notes=notes)
        if not time:
            error_statement = "Please enter a time"
            return render_template("form1.html", error_statement = error_statement, title=title, fname=fname, lname=lname, time = time, email=email, phone=phone, party=party, notes=notes)
        if not fname:
            error_statement = "Please enter your first name"
            return render_template("form1.html", error_statement = error_statement, title=title, fname=fname, lname=lname, time = time, email=email, phone=phone, party=party, notes=notes)
        if not lname:
            error_statement = "Please enter your last name"
            return render_template("form1.html", error_statement = error_statement, title=title, fname=fname, lname=lname, time = time, email=email, phone=phone, party=party, notes=notes)
        if not email:
            error_statement = "Please enter your email"
            return render_template("form1.html", error_statement = error_statement, title=title, fname=fname, lname=lname, time = time, email=email, phone=phone, party=party, notes=notes)
        if not phone:
            error_statement = "Please enter your phone number"
            return render_template("form1.html", error_statement = error_statement, title=title, fname=fname, lname=lname, time = time, email=email, phone=phone, party=party, notes=notes)
        if not party:
            error_statement =  "Please enter the number of people in your party"
            return render_template("form1.html", error_statement = error_statement, title=title, fname=fname, lname=lname, time = time, email=email, phone=phone, party=party, notes=notes)
        db.execute("INSERT INTO reservation (today, date, time, title, first_name, last_name, email, phone, party, notes) VALUES (?,?,?,?,?,?,?,?,?,?)", today, Date, time, title, fname, lname, email, phone, party, notes)
        return redirect('/confirmation')
    else:
        return render_template("reserve.html")

@app.route("/reserve", methods=["POST"])
def form1():
        today = date.today()
        Date = request.form.get('date')
        title = request.form.get('title')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        time = request.form.get('time')
        email = request.form.get('email')
        phone = request.form.get('phone')
        party = request.form.get('party')
        notes = request.form.get('notes')
        if not Date:
            error_statement = "Please enter a date"
            return render_template("form1.html", error_statement = error_statement, title=title, fname=fname, lname=lname, time = time, email=email, phone=phone, party=party, notes=notes)
        if Date =="None":
            error_statement = "Please enter a date"
            return render_template("form1.html", error_statement = error_statement, title=title, fname=fname, lname=lname, time = time, email=email, phone=phone, party=party, notes=notes)
        if not time:
            error_statement = "Please enter a time"
            return render_template("form1.html", error_statement = error_statement, title=title, fname=fname, lname=lname, time = time, email=email, phone=phone, party=party, notes=notes)
        if not fname:
            error_statement = "Please enter your first name"
            return render_template("form1.html", error_statement = error_statement, title=title, fname=fname, lname=lname, time = time, email=email, phone=phone, party=party, notes=notes)
        if not lname:
            error_statement = "Please enter your last name"
            return render_template("form1.html", error_statement = error_statement, title=title, fname=fname, lname=lname, time = time, email=email, phone=phone, party=party, notes=notes)
        if not email:
            error_statement = "Please enter your email"
            return render_template("form1.html", error_statement = error_statement, title=title, fname=fname, lname=lname, time = time, email=email, phone=phone, party=party, notes=notes)
        if not phone:
            error_statement = "Please enter your phone number"
            return render_template("form1.html", error_statement = error_statement, title=title, fname=fname, lname=lname, time = time, email=email, phone=phone, party=party, notes=notes)
        if not party:
            error_statement =  "Please enter the number of people in your party"
            return render_template("form1.html", error_statement = error_statement, title=title, fname=fname, lname=lname, time = time, email=email, phone=phone, party=party, notes=notes)
        db.execute("INSERT INTO reservation (today, date, time, title, first_name, last_name, email, phone, party, notes) VALUES (?,?,?,?,?,?,?,?,?,?)", today, Date, time, title, fname, lname, email, phone, party, notes)
        return redirect('/confirmation')

@app.route("/login", methods=["GET", "POST"])
def login():
     session.clear()
     if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return ("must provide username", 403)
        # Ensure password was submitted
        elif not request.form.get("password"):
            return ("must provide password", 403)
        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return ("invalid username and/or password", 403)
        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        return redirect("/reservations")
     else:
        return render_template("login.html")

@app.route("/dashboard")
@login_required
def dashboard():
    contacts = db.execute("SELECT * FROM contact ORDER BY DATE DESC")
    return render_template("dashboard.html", contacts = contacts)

@app.route("/reservations")
@login_required
def reservations():
    reservations = db.execute("SELECT * FROM reservation ORDER BY today DESC")
    return render_template("reservation.html", reservations = reservations)