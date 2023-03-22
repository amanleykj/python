from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Ninja:
    db = 'D_J'

    def __init__(self, data_row):
        self.id = data_row['id']
        self.first_name = data_row['first_name']
        self.last_name = data_row['last_name']
        self.age = data_row['age']
        self.created_at = data_row['created_at']
        self.updated_at = data_row['updated_at']
        self.dojo_id = data_row['dojo_id']


    @classmethod
    def getAll(cls):
        query = "SELECT * FROM D_J.ninjas;"
        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        all_ninjas = []
        for data_row in results:
            all_ninjas.append(cls(data_row))
        return all_ninjas

    @classmethod
    def save(cls, data_row):
        query = """
        INSERT INTO D_J.ninjas (first_name, last_name, age, dojo_id) 
        VALUES (%(first_name)s,%(last_name)s,%(age)s, %(dojo_id)s)
        """
        result = connectToMySQL(cls.db).query_db(query, data_row)
        print("THIS USER SAVED JUST FINE.")
        return result

    @classmethod
    def getOneByAge(cls, data_row):
        query = "SELECT * FROM D_J.ninjas WHERE age = %(age)s;"
        result = connectToMySQL(cls.db).query_db(query, data_row)
        if result:
            return cls(result[0])
        return False

    @classmethod
    def getOne(cls, data_row):
        query = "SELECT * FROM D_J.ninjas WHERE id = %(id)s"
        result = connectToMySQL(cls.db).query_db(query, data_row)
        if result:
            return cls(result[0])
        return False

# NOT FINISHED YET
    @classmethod
    def getDojoID(cls, data_row):
        query = "SELECT dojo_id FROM D_J.ninjas WHERE id = %(id)s"
        result = connectToMySQL(cls.db).query_db(query, data_row)
        if result:
            return cls(result[0])
        return False
# NOT FINISHED YET

    @classmethod
    def update(cls, data_row):
        query = """
        UPDATE D_J.ninjas SET first_name=%(first_name)s,last_name=%(last_name)s,age=%(age)s
        WHERE id = %(id)s
        """
        result = connectToMySQL(cls.db).query_db(query, data_row)
        return result

    @classmethod
    def destroy(cls, data_row):
        query = "DELETE FROM D_J.ninjas WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data_row)
        return result

    @classmethod
    def getOnebyDojoID(cls, id):
        query = """
        SELECT * FROM D_J.ninjas LEFT JOIN D_J.dojos ON ninjas.dojo_id = 
        dojos.id WHERE ninjas.id = %(id)s;
        """
        result = connectToMySQL(cls.db).query_db(query, id)
        if result:
            return cls(result[0])
        return False

    @classmethod
    def destroy_in_dojo(cls, data_row):
        query = "DELETE FROM D_J.ninjas WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data_row)
        return result