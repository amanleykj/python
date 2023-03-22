from mysqlconnection import connectToMySQL

class User:
    db = 'first_flask'

    def __init__(self, row):
        self.id = row['id']
        self.first_name = row['first_name']
        self.last_name = row['last_name']
        self.email = row['email']
        self.occupation = row['occupation']
        self.password = row['password']
        self.created_at = row['created_at']
        self.updated_at = row['updated_at']

    @classmethod
    def getAll(cls):
        query = "SELECT * FROM first_flask.friends;"
        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        all_friends = []
        for row in results:
            all_friends.append(cls(row))
        return all_friends

    @classmethod
    def save(cls,row):
        query = "INSERT INTO first_flask.friends(first_name, last_name, email, occupation, password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(occupation)s,%(password)s)"
        result = connectToMySQL(cls.db).query_db(query,row)
        return result