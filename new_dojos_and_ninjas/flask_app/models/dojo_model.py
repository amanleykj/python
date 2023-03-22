from flask_app.config.mysqlconnection import connectToMySQL
from .ninja_model import Ninja

class Dojo:
    db = 'D_J'

    def __init__(self, data_row):
        self.id = data_row['id']
        self.name = data_row['name']
        self.created_at = data_row['created_at']
        self.updated_at = data_row['updated_at']
        self.ninjas = []

    @classmethod
    def save(cls, data_row):
        query = """
        INSERT INTO D_J.dojos (name) VALUES (%(name)s)
        """
        result = connectToMySQL(cls.db).query_db(query, data_row)
        print("THIS DOJO HAS SAVED!")
        return result

    @classmethod
    def getAll(cls):
        query = "SELECT * FROM D_J.dojos;"
        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        all_dojos = []
        for data_row in results:
            all_dojos.append(cls(data_row))
        return all_dojos

    @classmethod
    def getOnebyDojoID(cls, data_row):
        query = """
        SELECT * FROM D_J.ninjas LEFT JOIN D_J.dojos ON ninjas.dojo_id = 
        dojos.id WHERE ninjas.id = %(id)s;
        """
        result = connectToMySQL(cls.db).query_db(query, data_row)
        if result:
            return cls(result[0])
        return False
# I'm not sure if this is going to work.

    @classmethod
    def getOne(cls, data_row):
        query = "SELECT * FROM D_J.dojos WHERE id = %(id)s"
        result = connectToMySQL(cls.db).query_db(query, data_row)
        if result:
            return cls(result[0])
        return False
    
    @classmethod
    def destroy(cls, data_row):
        query = "DELETE FROM D_J.dojos WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data_row)
        return result

    @classmethod
    def get_first_and_last(cls, row):
        query = """
        SELECT * FROM D_J.dojos LEFT JOIN D_J.ninjas 
        ON D_J.dojos.id = D_J.ninjas.dojo_id WHERE dojos.id = %(id)s;
        """
        result = connectToMySQL(cls.db).query_db(query, row)
        dojo = cls(result[0])
        for row in result:
            final = {
            'id': row['ninjas.id'],
            'first_name': row['first_name'],
            'last_name': row['last_name'],
            'age': row['age'],
            'dojo_id' : row['dojo_id'],
            'created_at': row['ninjas.created_at'],
            'updated_at': row['ninjas.updated_at'] 
            }
            dojo.ninjas.append( Ninja(final) )
        return dojo

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = """
        SELECT * FROM D_J.dojos LEFT JOIN D_J.ninjas.id ON ninjas.dojo_id = D_J.dojos.id 
        WHERE D_J.dojos.id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db( query, data)
        dojo = cls(results[0])
        for row_for_db in results:
            ninja_data = {
                "id" : row_for_db['ninjas.id'],
                "first_name" : row_for_db['first_name'],
                "last_name" : row_for_db['last_name'],
                "age" : row_for_db['age'],
                "created_at" : row_for_db['ninjas.created_at'],
                "updated_at" : row_for_db['ninjas.updated_at']
            }
            dojo.ninjas.append(data.Ninja(ninja_data))

        return dojo