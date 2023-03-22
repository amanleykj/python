from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import tree_model

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:

    db = "exam"

    def __init__( self, data_row ):
        self.id = data_row['id']
        self.first_name = data_row['first_name']
        self.last_name = data_row['last_name']
        self.email = data_row['email']
        self.password = data_row['password']
        self.created_at = data_row['created_at']
        self.updated_at = data_row['updated_at']
        self.my_trees = []

    @classmethod
    def save(cls, data_row):
        query = """
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """

        user_first_name = data_row['first_name']
        results = connectToMySQL(cls.db).query_db( query, data_row)
        print(f"The user {user_first_name} has saved.")
        return results
    

    @classmethod
    def get_by_email( cls, data ):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL( cls.db ).query_db(query,data)
        if len(results) < 1:
            return False
        print(results)
        return cls(results[0])
    
    
    @classmethod
    def get_one( cls, data):
        query = """SELECT * FROM users WHERE id = %(id)s;"""
        results = connectToMySQL( cls.db ).query_db(query, data)
        if results:
            return cls(results[0])
        return False


    @classmethod
    def get_all_my_trees(cls,data):
        query = """
        SELECT * FROM users LEFT JOIN trees ON users.id = trees.user_id WHERE users.id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        print("HAHAHHAHAA")
        print("HAHAHHAHAA")
        print("HAHAHHAHAA")
        print(results)
        if results:
            this_user = cls(results[0])
            for data_row in results:
                if data_row['user_id'] == None:
                    break
                this_user.my_trees.append(tree_model.Tree(data_row))
            return this_user
        return False


    @staticmethod
    def validate_user(form):
        is_valid = True
        if len(form['first_name']) < 2:
            is_valid = False
            flash("Your first name must be two characters or more.")
        if len(form['last_name']) < 2:
            is_valid = False
            flash("Your last name must be two characters or more.")
        if not EMAIL_REGEX.match(form['email']):
            is_valid = False
            flash("Your email address must be in a valid format.")
        if len(form['password']) < 8:
            is_valid = False
            flash("Your password must be eight characters or more.")
        if not form['password'] == form['confirm_password']:
            is_valid = False
            flash("Your passwords must match.")
        return is_valid