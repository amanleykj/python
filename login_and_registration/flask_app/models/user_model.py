from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# ABOVE - we are creating an object called bcrypt, 
# which is made by invoking the function Bcrypt with our app as an argument


class User:

    db = "mydb"

    def __init__( self, data_row ):
        self.id = data_row['id']
        self.first_name = data_row['first_name']
        self.last_name = data_row['last_name']
        self.email = data_row['email']
        self.password = data_row['password']
        self.created_at = data_row['created_at']
        self.updated_at = data_row['updated_at']

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
    def get_one( cls, data_row):
        query = """
        SELECT * FROM users WHERE id = %(id)s;
        """
        results = connectToMySQL( cls.db ).query_db( query, data_row )
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_by_email( cls, data ):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL( cls.db ).query_db(query,data)
        if len(results) < 1:
            return False
        print(results)
        return cls(results[0])

    @classmethod
    def get_id_by_email( cls, data ):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL( cls.db ).query_db(query, data)
        if results:
            return cls(results[0])
        return False

    @staticmethod
    def validate_user(form):
        is_valid = True
        if len(form['first_name']) < 3:
            is_valid = False
            flash("Your first name must be longer than two characters.")
        if not form['first_name'].isalpha():
            is_valid = False
            flash("Only characters are allowed for first name.")
        if len(form['last_name']) < 3:
            is_valid = False
            flash("Your last name must be longer than two characters.")
        if not form['last_name'].isalpha():
            is_valid = False
            flash("Only characters are allowed for last name.")
        if len(form['email']) < 3:
            flash("Your email address must be longer than two characters.")
        if not EMAIL_REGEX.match(form['email']):
            is_valid = False
            flash("Your email address must be in a valid format.")
        if len(form['password']) < 8:
            is_valid = False
            flash("Your password must be at least eight characters long.")
        if not any(char.isdigit() for char in form['password']):
            is_valid = False
            flash('Password should have at least one number.')
        if not any(char.isupper() for char in form['password']):
            is_valid = False
            flash('Password should have at least one uppercase letter.')
        if not form['password'] == form['confirm_password']:
            is_valid = False
            flash("Your passwords must match.")
        return is_valid