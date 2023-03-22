from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from ..models import user_model

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Sighting:

    db = "exam_2"

    def __init__( self, data_row ):
        self.id = data_row['id']
        self.location = data_row['location']
        self.what_happened = data_row['what_happened']
        self.date_sighting = data_row['date_sighting']
        self.num_sasquatches = data_row['num_sasquatches']
        self.created_at = data_row['created_at']
        self.updated_at = data_row['updated_at']
        self.creator = None


    @classmethod
    def get_all_sightings_with_creator(cls):
        query = "SELECT * FROM sightings JOIN users ON sightings.user_id = users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        all_sightings = []
        for data_row in results:
            single_sighting = cls(data_row)
            single_sighting_user_info = {
                'id' : data_row['users.id'],
                'location' : data_row['location'],
                'what_happened' : data_row['what_happened'],
                'date_sighting' : data_row['date_sighting'],
                'num_sasquatches' : data_row['num_sasquatches'],
                'first_name' : data_row['first_name'],
                'last_name' : data_row['last_name'],
                'email' : data_row['email'],
                'password' : data_row['password'],
                'created_at' : data_row['users.created_at'],
                'updated_at' : data_row['users.updated_at']
            }

            sighting_creator = user_model.User(single_sighting_user_info)
            single_sighting.creator = sighting_creator
            all_sightings.append(single_sighting)
        return all_sightings
    
    @classmethod
    def save( cls, data_row ):
        query = """
        INSERT INTO sightings (location, what_happened, date_sighting, num_sasquatches, user_id)
        VALUES (%(location)s, %(what_happened)s, %(date_sighting)s, %(num_sasquatches)s, %(user_id)s);
        """

        sighting_name = data_row['location']
        results = connectToMySQL(cls.db).query_db( query, data_row)
        
        print(f"The sighting {sighting_name} has been recorded; let's see if others have the same sighting.")
        return results
    
    @classmethod
    def get_sighting_with_creator(cls,data):
        query = """
        SELECT * FROM sightings LEFT JOIN users ON sightings.user_id = users.id WHERE sightings.id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        sighting = cls(results[0])

        user_data = {
            'id' : results[0]['users.id'],
            'first_name' : results[0]['first_name'],
            'last_name' : results[0]['last_name'],
            'email' : results[0]['email'],
            'password' : results[0]['password'],
            'created_at' : results[0]['users.created_at'],
            'updated_at' : results[0]['users.updated_at']
        }
        sighting.creator = user_model.User(user_data)
        print("Sighting is as follows: ", sighting)
        return sighting

    @classmethod
    def get_sighting(cls,data):
        query = "SELECT * FROM sightings LEFT JOIN users ON sightings.user_id = users.id WHERE sightings.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def edit_sighting(cls,data):
        query = """
                UPDATE sightings SET id = %(id)s, location = %(location)s, what_happened = %(what_happened)s, date_sighting = %(date_sighting)s,
                num_sasquatches = %(num_sasquatches)s WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.db).query_db(query,data)
        return results

    @classmethod
    def delete(cls, data_row):
        query = """
                DELETE FROM sightings WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.db).query_db(query, data_row)
        return results

    @staticmethod
    def validate_sighting(form):
        is_valid = True
        if form['location'] == '':
            is_valid = False
            flash("Please provide a location.")
        if form['what_happened'] == "":
            is_valid = False
            flash("Please explain what happened.")
        if form['date_sighting'] == '':
            is_valid = False
            flash("Please include date of sighting.")
        if form['num_sasquatches'] == "0":
            is_valid = False
            flash("You must include at least one sighting.")
        return is_valid