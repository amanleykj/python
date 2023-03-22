from flask_app import app
from flask import render_template, redirect, request, session, flash
from ..models.user_model import User
from ..models.tree_model import Tree

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/new_tree')
def new_tree():
    if "user_id" in session:
        return render_template("new_tree.html", user = User.get_one({"id":session['user_id']}))
    else:
        return redirect('/')
    
@app.route('/plant_tree', methods = ['post'])
def plant_tree():
    if request.form['action'] == 'plant_tree':

        if not Tree.validate_tree(request.form):
            return redirect('/new_tree')

        data_row = {
            'species' : request.form['species'],
            'location' : request.form['location'],
            'reason' : request.form['reason'],
            'date_planted' : request.form['date_planted'],
            'user_id' : session['user_id']
        }

        tree_exist = Tree.get_by_tree_name(data_row)
        if tree_exist:
            print("THAT TREE HAS ALREADY BEEN PLANTED ELSEWHERE.")
            flash("Sorry, but that tree has already been planted by someone else.")
            return redirect('/new_tree')

        tree_id = Tree.save(data_row)
        return redirect('/dashboard')
    
@app.route('/show_tree/<int:id>')
def show_tree(id):
    if "user_id" in session:
        return render_template("show_tree.html", tree = Tree.get_tree_with_creator({"id" : id}), user = User.get_one({"id" : session['user_id']}))
    else:
        return redirect('/')

@app.route('/edit_tree/<int:id>')
def edit_tree1(id):
    if 'user_id' in session:
        return render_template("edit_tree.html", tree = Tree.get_tree({"id" : id}), user = User.get_one({"id": session['user_id']}))
    else:
        return redirect('/')

@app.route('/edit_tree', methods = ['post'])
def edit_tree():
    if 'user_id' not in session:
        return redirect('/')
    if not Tree.validate_tree(request.form):
        flash("Please try your tree again.")
        return redirect('/dashboard')

    data_row = {
        'id' : request.form['id'],
        'species' : request.form['species'],
        'location' : request.form['location'],
        'reason' : request.form['reason'],
        'date_planted' : request.form['date_planted']
    }

    Tree.edit_tree(data_row)
    return redirect('/dashboard')


@app.route('/delete/<int:id>')
def delete(id):
    Tree.delete({'id' : id})
    return redirect('/dashboard')

@app.route('/delete2/<int:id>')
def delete2(id):
    Tree.delete({'id' : id})
    return redirect('/account')