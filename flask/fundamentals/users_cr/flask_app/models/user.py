from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    db = 'mydb'

    def __init__(self, data_row):
        self.id = data_row['id']
        self.first_name = data_row['first_name']
        self.last_name = data_row['last_name']
        self.email = data_row['email']
        self.created_at = data_row['created_at']
        self.updated_at = data_row['updated_at']

    @classmethod
    def getAll(cls):
        query = "SELECT * FROM mydb.users;"
        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        all_users = []
        for data_row in results:
            all_users.append(cls(data_row))
        return all_users

    @classmethod
    def save(cls, data_row):
        query = """
        INSERT INTO mydb.users(first_name, last_name, email) 
        VALUES (%(first_name)s,%(last_name)s,%(email)s)
        """
        result = connectToMySQL(cls.db).query_db(query, data_row)
        print("THIS USER SAVED JUST FINE.")
        return result

    @classmethod
    def getOneByEmail(cls, data_row):
        query = "SELECT * FROM mydb.users WHERE email = %(email)s;"
        result = connectToMySQL(cls.db).query_db(query, data_row)
        if result:
            return cls(result[0])
        return False

    @classmethod
    def getOne(cls, data_row):
        query = "SELECT * FROM mydb.users WHERE id = %(id)s"
        result = connectToMySQL(cls.db).query_db(query, data_row)
        if result:
            return cls(result[0])
        return False

    @classmethod
    def update(cls, data_row):
        query = """
        UPDATE mydb.users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s
        WHERE id = %(id)s
        """
        result = connectToMySQL(cls.db).query_db(query, data_row)
        return result

    @classmethod
    def destroy(cls, data_row):
        query = "DELETE FROM mydb.users WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data_row)
        return result