from flask_app import app
from flask import session, redirect, render_template, request
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template("read_all.html", all_users = User.getAll())

@app.route('/create')
def create():
    return render_template ("create.html")

@app.route('/create_user', methods=['POST'])
def create_user():
    # if request.form['action'] == ['create_user']: DON'T USE UNLESS ACTUALLY NEEDED TO DIFFERENTIATE
    data_row = {
            "first_name" : request.form["first_name"],
            "last_name" : request.form["last_name"],
            "email" : request.form["email"]
        }

    user_id = User.save(data_row)
    session['user_id'] = user_id
    return redirect('/')


@app.route('/user/<int:id>/show')
def show_user(id):
    return render_template("show.html", user = User.getOne({"id" : id}))

@app.route('/user/<int:id>/update_user')
def update_user(id):
    return render_template("update.html", user = User.getOne({"id" : id}))


@app.route("/user/<int:id>/update", methods=['POST'])
def update(id):
    data_row = {
            "id" : id,
            "first_name" : request.form['first_name'],
            "last_name" : request.form['last_name'],
            "email" : request.form['email']
    }
    
    get_id = data_row["id"]
    print(f"The ID of this guy is {get_id}, so let me know.")
    User.update(data_row)
    return redirect(f'/user/{get_id}/show')

@app.route("/user/<int:id>/destroy")
def destroy(id):
    User.destroy({'id' : id})
    return redirect('/')