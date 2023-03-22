from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from ..models import user_model

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Tree:

    db = "exam"

    def __init__( self, data_row ):
        self.id = data_row['id']
        self.species = data_row['species']
        self.location = data_row['location']
        self.reason = data_row['reason']
        self.date_planted = data_row['date_planted']
        self.created_at = data_row['created_at']
        self.updated_at = data_row['updated_at']
        self.creator = None


    @classmethod
    def get_all_trees_with_creator(cls):
        query = "SELECT * FROM trees JOIN users ON trees.user_id = users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        all_trees = []
        for data_row in results:
            single_tree = cls(data_row)
            single_tree_user_info = {
                'id' : data_row['users.id'],
                'species' : data_row['species'],
                'location' : data_row['location'],
                'reason' : data_row['reason'],
                'date_planted' : data_row['date_planted'],
                'first_name' : data_row['first_name'],
                'last_name' : data_row['last_name'],
                'email' : data_row['email'],
                'password' : data_row['password'],
                'created_at' : data_row['users.created_at'],
                'updated_at' : data_row['users.updated_at']
            }

            tree_creator = user_model.User(single_tree_user_info)
            single_tree.creator = tree_creator
            all_trees.append(single_tree)
        return all_trees
    
    @classmethod
    def save( cls, data_row ):
        query = """
        INSERT INTO trees (species, location, reason, date_planted, user_id)
        VALUES (%(species)s, %(location)s, %(reason)s, %(date_planted)s, %(user_id)s);
        """

        tree_name = data_row['species']
        results = connectToMySQL(cls.db).query_db( query, data_row)
        
        print(f"The tree {tree_name} is planted; may it grow forever and forever.")
        return results
    
    @classmethod
    def get_by_tree_name( cls, data ):
        query = "SELECT * FROM trees WHERE species = %(species)s;"
        results = connectToMySQL( cls.db ).query_db(query,data)
        if len(results) < 1:
            return False
        print(results)
        return cls(results[0])
    
    @classmethod
    def get_tree_with_creator(cls,data):
        query = """
        SELECT * FROM trees LEFT JOIN users ON trees.user_id = users.id WHERE trees.id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        tree = cls(results[0])

        user_data = {
            'id' : results[0]['users.id'],
            'first_name' : results[0]['first_name'],
            'last_name' : results[0]['last_name'],
            'email' : results[0]['email'],
            'password' : results[0]['password'],
            'created_at' : results[0]['users.created_at'],
            'updated_at' : results[0]['users.updated_at']
        }
        tree.creator = user_model.User(user_data)
        print("Tree is as follows: ", tree)
        return tree


    @classmethod
    def get_one( cls, data ):
        query = """
        SELECT * FROM trees WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def get_tree(cls,data):
        query = "SELECT * FROM trees LEFT JOIN users ON trees.user_id = users.id WHERE trees.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def edit_tree(cls,data):
        query = """
                UPDATE trees SET id = %(id)s, species = %(species)s, location = %(location)s, reason = %(reason)s,
                date_planted = %(date_planted)s WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.db).query_db(query,data)
        return results

    @classmethod
    def delete(cls, data_row):
        query = """
                DELETE FROM trees WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.db).query_db(query, data_row)
        return results
    
    @classmethod
    def get_trees_of_one_user(cls,data):
        query = """
        SELECT * FROM trees WHERE user_id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        return results


    @staticmethod
    def validate_tree(form):
        is_valid = True
        if len(form['species']) < 5:
            is_valid = False
            flash("Tree species must be at least five characters.")
        if len(form['location']) < 2:
            is_valid = False
            flash("The location must be at least two characters.")
        if len(form['reason']) > 50:
            is_valid = False
            flash("Please give your reason in under 50 words.")
        if form['date_planted'] == '':
            is_valid = False
            flash("Please select when you planted this tree.")
        return is_valid