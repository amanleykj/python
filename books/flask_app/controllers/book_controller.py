from flask_app import app
from flask import session, redirect, render_template, request
from flask_app.models.author_model import Author
from flask_app.models.book_model import Book
from flask import flash

@app.route('/books')
def books():
    return render_template("books.html", all_books = Book.get_all_books())

@app.route('/create_book', methods=['POST'])
def create_book():
    data_row = {
        "title" : request.form['title'],
        "num_of_pages" : request.form['num_of_pages']
    }

    book_name = Book.save(data_row)
    session['book_name'] = book_name
    return redirect('/books')