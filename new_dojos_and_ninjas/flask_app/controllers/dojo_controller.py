from flask_app import app
from flask import session, redirect, render_template, request
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo
from flask import flash

@app.route('/')
def index():
    return render_template("dojos.html", all_ninjas = Ninja.getAll(), all_dojos = Dojo.getAll())

@app.route("/dojo/<int:id>/destroy")
def destroy_dojo(id):
    
    Dojo.destroy({'id' : id})
    return redirect('/')

@app.route('/set_dojo', methods=['POST'])
def set_dojo():
    data_row = {
            "name" : request.form["name"]
        }

    if not request.form['name']:
        flash("Put in something in the field.")
        return redirect('/')
    else:
        dojo_id = Dojo.save(data_row)
        session['dojo_id'] = dojo_id
        return redirect('/')

@app.route('/homepage_dojo/<int:id>/show')
def homepage_dojo(id):
    row = {
        "id" : id
    }
    return render_template("homepage_dojo.html", final = Dojo.get_first_and_last(row))

@app.route('/confirm_destroy_dojo', methods=['POST'])
def dojo_destroy():
    
    
    
    Dojo.destroy({'id' : id})
    return redirect('/')
