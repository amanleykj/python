from flask_app import app
from flask import render_template, redirect, request, session, flash
from ..models.user_model import User
from ..models.recipe_model import Recipe

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/new_recipe')
def new_recipe():
    if "user_id" in session:
        return render_template("new_recipe.html", user = User.get_one({"id":session['user_id']}))
    else:
        return redirect('/')

@app.route('/create_recipe', methods = ['post'])
def create_recipe():
    if request.form['action'] == 'create_recipe':

        if not Recipe.validate_recipe(request.form):
            return redirect('/new_recipe')

        data_row = {
            'name' : request.form['name'],
            'description' : request.form['description'],
            'under_30' : request.form['under_30'],
            'date_made' : request.form['date_made'],
            'instructions' : request.form['instructions'],
            'user_id' : session['user_id']
        }

        recipe_exist = Recipe.get_by_recipe_name(data_row)
        if recipe_exist:
            flash("Sorry, but that recipe is already submitted by another user.")
            return redirect('/new_recipe')

        Recipe.save(data_row)
        return redirect('/dashboard')
    

@app.route('/recipe_show/<int:id>')
def recipe_show(id):
    if "user_id" in session:
        return render_template("recipe_show.html", recipe = Recipe.get_user_with_recipes({"id" : id}), user = User.get_one({"id": session['user_id']}))
    else:
        return redirect('/')

@app.route('/edit_recipe/<int:id>')
def edit_recipe1(id):
    if "user_id" in session:
        return render_template("recipe_edit.html", recipe = Recipe.get_by_id({"id" : id}))
    else:
        return redirect('/')

@app.route('/edit_recipe', methods = ['post'])
def update_recipe():
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.validate_recipe(request.form):
        return redirect('/dashboard')
    
    data_row = {
            'id' : request.form['id'],
            'name' : request.form['name'],
            'description' : request.form['description'],
            'under_30' : request.form['under_30'],
            'date_made' : request.form['date_made'],
            'instructions' : request.form['instructions']
        }

    Recipe.update_recipe(data_row)
    return redirect('/dashboard')

@app.route('/my_recipes')
def my_recipes():
    if "user_id" in session:
        return render_template("my_recipes.html", all_my_recipes = Recipe.get_recipes_of_one_user_id({"id":session['user_id']}),
        user = User.get_one({"id": session['user_id']}))
    else:
        return redirect('/')
    
@app.route('/delete/<int:id>')
def delete(id):
    Recipe.delete({'id' : id})
    return redirect('/dashboard')