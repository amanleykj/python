from flask_app.config.mysqlconnection import connectToMySQL


class Author:
    db = 'mydb'

    def __init__(self, data_row):
        self.id = data_row['id']
        self.name = data_row['name']
        self.created_at = data_row['created_at']
        self.updated_at = data_row['updated_at']
        self.favorite_books = []

    @classmethod
    def save(cls, data_row):
        query = """
        INSERT INTO authors (name) VALUES (%(name)s);
        """
        result = connectToMySQL(cls.db).query_db(query, data_row)
        print("AUTHOR SAVED!")
        print("AUTHOR SAVED!")
        print("AUTHOR SAVED!")
        print("AUTHOR SAVED!")
        print("AUTHOR SAVED!")
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(cls.db).query_db(query)
        all_authors = []
        for data_row in results:
            all_authors.append(cls(data_row))
        return all_authors

    @classmethod
    def get_one_author(cls, data_row):
        query = "SELECT * FROM authors WHERE id = %(id)s"
        result = connectToMySQL(cls.db).query_db(query, data_row)
        if result:
            return cls(result[0])
        return False

    @classmethod
    def destroy(cls, data_row):
        query = "DELETE FROM authors WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data_row)
        return result