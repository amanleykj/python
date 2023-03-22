from flask_app.config.mysqlconnection import connectToMySQL

class Book:
    db = 'mydb'

    def __init__(self, data_row):
        self.id = data_row['id']
        self.title = data_row['title']
        self.num_of_pages = data_row['num_of_pages']
        self.created_at = data_row['created_at']
        self.updated_at = data_row['updated_at']

    @classmethod
    def save(cls, data_row):
        query = """
        INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);
        """
        result = connectToMySQL(cls.db).query_db(query, data_row)
        print("BOOK SAVED!")
        print("BOOK SAVED!")
        print("BOOK SAVED!")
        print("BOOK SAVED!")
        print("BOOK SAVED!")
        return result

    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(cls.db).query_db(query)
        all_books = []
        for data_row in results:
            all_books.append(cls(data_row))
        return all_books