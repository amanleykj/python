from flask_app import app
from flask import session, redirect, render_template, request
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo
from flask import flash

@app.route('/create_ninja')
def ninja():
    return render_template ("create_ninja.html", all_dojos = Dojo.getAll())

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    data_row = {
            "first_name" : request.form["first_name"],
            "last_name" : request.form["last_name"],
            "age" : request.form["age"],
            "dojo_id" : request.form["dojo_id"]
        }

    ninja_id = Ninja.save(data_row)
    dojo_id = data_row['dojo_id']
    session['ninja_id'] = ninja_id
    return redirect(f'/homepage_dojo/{dojo_id}/show')

@app.route('/ninja/<int:id>/show')
def show_ninja(id):
    return render_template("show.html", ninja = Ninja.getOne({"id" : id}))

@app.route('/ninja/<int:id>/update_ninja')
def view_ninja(id):
    ninja = Ninja.getOne({"id" : id})
    print("Ninja", ninja.dojo_id)

    return render_template("update_ninja.html", ninja = ninja) 

@app.route("/ninja/<int:id>/update", methods=['POST'])
def update_ninja(id):
    print("Inside update: ")
    print(request.form)
    data_row = {
            "id" : id,
            "first_name" : request.form['first_name'],
            "last_name" : request.form['last_name'],
            "age" : request.form['age'],
            "dojo_id" : request.form['dojo_id']
    }
    
    get_id = data_row["id"]
    d_id = data_row["dojo_id"]
    print(f"The ID of this ninja is {get_id}, so let me know.")
    Ninja.update(data_row)
    return redirect(f'/homepage_dojo/{d_id}/show')

@app.route("/ninja/<int:id>/destroy")
def destroy_ninja(id):
    Ninja.destroy({'id' : id})
    return redirect('/')