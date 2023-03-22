from flask_app import app
from flask import render_template, redirect, request, session, flash
from ..models.user_model import User
from ..models.sighting_model import Sighting

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/new_sighting')
def new_sighting():
    if "user_id" in session:
        return render_template("new_sighting.html", user = User.get_one({"id":session['user_id']}))
    else:
        return redirect('/')
    
@app.route('/report_sighting', methods = ['post'])
def report_sighting():
        if not Sighting.validate_sighting(request.form):
            return redirect('/new_sighting')

        data_row = {
            'location' : request.form['location'],
            'what_happened' : request.form['what_happened'],
            'date_sighting' : request.form['date_sighting'],
            'num_sasquatches' : request.form['num_sasquatches'],
            'user_id' : session['user_id']
        }

        sighting_id = Sighting.save(data_row)
        return redirect('/dashboard')
    
@app.route('/show_sighting/<int:id>')
def show_sighting(id):
    if "user_id" in session:
        return render_template("show_sighting.html", sighting = Sighting.get_sighting_with_creator({"id" : id}), user = User.get_one({"id" : session['user_id']}))
    else:
        return redirect('/')

@app.route('/edit_sighting/<int:id>')
def edit_sighting(id):
    if 'user_id' in session:
        return render_template("edit_sighting.html", sighting = Sighting.get_sighting({"id" : id}), user = User.get_one({"id": session['user_id']}))
    else:
        return redirect('/')

@app.route('/edit_sighting', methods = ['post'])
def edit_sighting1():
    if 'user_id' not in session:
        return redirect('/')
    if not Sighting.validate_sighting(request.form):
        sighting_id = request.form['id']
        flash("Please edit your sighting again.")
        return redirect(f'/edit_sighting/{sighting_id}')

    data_row = {
        'id' : request.form['id'],
        'location' : request.form['location'],
        'what_happened' : request.form['what_happened'],
        'date_sighting' : request.form['date_sighting'],
        'num_sasquatches' : request.form['num_sasquatches']
    }

    Sighting.edit_sighting(data_row)
    return redirect('/dashboard')


@app.route('/delete/<int:id>')
def delete(id):
    Sighting.delete({'id' : id})
    return redirect('/dashboard')

@app.route('/believe', methods = ['POST'])
def believe():
    Sighting.believe({'id' : id})
    return redirect