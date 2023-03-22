from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from ..models import user_model

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Recipe:

    db = "recipes_db"

    def __init__( self, data_row ):
        self.id = data_row['id']
        self.name = data_row['name']
        self.description = data_row['description']
        self.under_30 = data_row['under_30']
        self.date_made = data_row['date_made']
        self.instructions = data_row['instructions']
        self.created_at = data_row['created_at']
        self.updated_at = data_row['updated_at']
        self.creator = None
        self.all_recipes = []

# 
    @classmethod
    def get_user_with_recipes( cls, data ):
        query = """
        SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s;
        """
        results = connectToMySQL( cls.db ).query_db( query, data )
        print("These are the results below: ")
        print(results)
        recipe = cls(results[0])
# 
        user_data = {
            "id" : results[0]['users.id'],
            "first_name" : results[0]['first_name'],
            'last_name' : results[0]['last_name'],
            'email' : results[0]['email'],
            'password' : results[0]['password'],
            'created_at' : results[0]['users.created_at'],
            'updated_at' : results[0]['users.updated_at']
            }

        recipe.creator = user_model.User(user_data)
        print("Recipe is: ", recipe)
#
        return recipe

    @classmethod
    def save( cls, data_row ):
        query = """
        INSERT INTO recipes (name, description, under_30, date_made, instructions, user_id)
        VALUES (%(name)s, %(description)s, %(under_30)s, %(date_made)s, %(instructions)s, %(user_id)s);
        """

        recipe_name = data_row['name']
        results = connectToMySQL(cls.db).query_db( query, data_row)
        
        print(f"The recipe {recipe_name} is saved, and sure looks GOOD!")
        return results
    
    @classmethod
    def update_recipe(cls,data_row):
        query = """
                UPDATE recipes SET id = %(id)s, name = %(name)s, description = %(description)s, under_30 = %(under_30)s,
                date_made = %(date_made)s, instructions = %(instructions)s WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.db).query_db( query, data_row)
        return results

    @classmethod
    def get_all_recipes_with_creator(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        all_recipes = []
        for data_row in results:
            single_recipe = cls(data_row)
            single_recipe_user_info = {
                'id' : data_row['users.id'],
                'name' : data_row['name'],
                'description' : data_row['description'],
                'first_name' : data_row['first_name'],
                'last_name' : data_row['last_name'],
                'email' : data_row['email'],
                'password' : data_row['password'],
                'created_at' : data_row['users.created_at'],
                'updated_at' : data_row['users.updated_at']
            }

            recipe_creator = user_model.User(single_recipe_user_info)
            single_recipe.creator = recipe_creator
            all_recipes.append(single_recipe)
        return all_recipes


    @classmethod
    def get_one( cls, data ):
        query = """
        SELECT * FROM recipes WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        print("HEREHERHER")
        print(results)
        return cls(results[0])

    @classmethod
    def get_by_recipe_name( cls, data ):
        query = "SELECT * FROM recipes WHERE name = %(name)s;"
        results = connectToMySQL( cls.db ).query_db(query,data)
        if len(results) < 1:
            return False
        print(results)
        return cls(results[0])

    @classmethod
    def get_recipes_of_one_user_id( cls, data):
        query = """
        SELECT * FROM recipes WHERE user_id = %(id)s;
        """
        results = connectToMySQL( cls.db ).query_db( query, data)
        return results

# NOT MADE BY ME ADJUST BELOW
    @classmethod
    def get_by_id(cls,data):
        query = """
                SELECT * FROM recipes
                JOIN users ON recipes.user_id = users.id
                WHERE recipes.id = %(id)s;
                """
        results = connectToMySQL(cls.db).query_db(query,data)
        if not results:
            return False

        results = results[0]
        this_recipe = cls(results)
        user_data = {
                "id": results['users.id'],
                "first_name": results['first_name'],
                "last_name": results['last_name'],
                "email": results['email'],
                "password" : results['password'],
                "created_at": results['users.created_at'],
                "updated_at": results['users.updated_at']
        }
        this_recipe.creator = user_model.User(user_data)
        return this_recipe

    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM recipes;
        """
        results = connectToMySQL(cls.db).query_db(query)
        all_recipes = []
        for data_row in results:
            all_recipes.append(cls(data_row))
        return all_recipes
    
    @classmethod
    def delete(cls, data_row):
        query = """
                DELETE FROM recipes WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.db).query_db(query, data_row)
        return results


    @staticmethod
    def validate_recipe(form):
        is_valid = True
        if len(form['name']) < 2:
            is_valid = False
            flash("Recipe name must be at least three characters.")
        if len(form['description']) < 2:
            is_valid = False
            flash("The description must be at least three characters.")
        if 'under_30' not in form:
            is_valid = False
            flash("You need to select whether or not it can be cooked in under 30 minutes.")
        if form['date_made'] == '':
            is_valid = False
            flash("Please include the date made.")
        if len(form['instructions']) < 2:
            is_valid = False
            flash("The instructions must be at least three characters.")
        return is_valid