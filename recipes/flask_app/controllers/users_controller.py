from flask_app import app
from flask import render_template, redirect, request, session, flash
from ..models.user_model import User
from ..models.recipe_model import Recipe

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return redirect("/login")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/create_user', methods = ['post'])
def create_user():
    if request.form['action'] == 'create_user':

        if not User.validate_user(request.form):
            return redirect('/')

        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print("THIS IS THE HASH BELOW: ")
        print(pw_hash)

        data_row = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'password' : pw_hash
        }

        user_in_db = User.get_by_email(data_row)
        if user_in_db:
            print("SEATS TAKEN")
            flash("Sorry, but that email is taken.")
            return redirect('/')

        user_id = User.save(data_row)
        session['user_id'] = user_id
        return redirect('/dashboard')

# session- it's a form of state that persists that does not do so past the user using the application.

@app.route('/user_login', methods = ['post'])
def user_login():
    if request.form['action'] == 'user_login':
        data_row = {
            'email' : request.form['email']
        }
        user_in_db = User.get_by_email(data_row)

        if not user_in_db:
            flash("Invalid Email/Password.")
            return redirect('/')
        if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
            flash("Invalid Email/Password.")
            return redirect('/')

    session['user_id'] = user_in_db.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if "user_id" in session:
        return render_template("dashboard.html", user = User.get_one({"id": session['user_id']}), 
        all_recipes = Recipe.get_all_recipes_with_creator())
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    print(session)
    session.clear()
    print("Session has been cleared.")
    return redirect('/')