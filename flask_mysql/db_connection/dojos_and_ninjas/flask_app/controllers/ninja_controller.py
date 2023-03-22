from flask_app import app
from flask import session, redirect, render_template, request
from flask_app.models.ninja_model import Ninja

@app.route('/')
def index():
    return render_template("index.html", all_ninjas = Ninja.getAll())

@app.route('/create')
def create():
    return render_template ("create.html")

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    # if request.form['action'] == ['create_ninja']: DON'T USE UNLESS ACTUALLY NEEDED TO DIFFERENTIATE
    data_row = {
            "first_name" : request.form["first_name"],
            "last_name" : request.form["last_name"],
            "age" : request.form["age"]
        }

    ninja_id = Ninja.save(data_row)
    session['ninja_id'] = ninja_id
    return redirect('/')


@app.route('/ninja/<int:id>/show')
def show_ninja(id):
    return render_template("show.html", ninja = Ninja.getOne({"id" : id}))

@app.route('/ninja/<int:id>/update_ninja')
def update_ninja(id):
    return render_template("update.html", ninja = Ninja.getOne({"id" : id}))

@app.route("/ninja/<int:id>/update", methods=['POST'])
def update(id):
    data_row = {
            "id" : id,
            "first_name" : request.form['first_name'],
            "last_name" : request.form['last_name'],
            "age" : request.form['age']
    }
    
    get_id = data_row["id"]
    print(f"The ID of this ninja is {get_id}, so let me know.")
    Ninja.update(data_row)
    return redirect(f'/ninja/{get_id}/show')

@app.route("/ninja/<int:id>/destroy")
def destroy(id):
    Ninja.destroy({'id' : id})
    return redirect('/')