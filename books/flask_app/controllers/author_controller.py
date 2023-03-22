from flask_app import app
from flask import session, redirect, render_template, request
from flask_app.models.author_model import Author
from flask_app.models.book_model import Book
from flask import flash

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    return render_template("index.html", authors = Author.get_all())


# all_books = Book.get_all_books()

@app.route('/create_author', methods=['POST'])
def create_author():
    data_row = {
        "id" : request.form['id'],
        "name" : request.form['name']
    }

    author_name = Author.save(data_row)
    author_num = request.form['id']
    session['author_name'] = author_name
    print("Author number would be: ", author_num)
    return redirect('/')

@app.route('/author_page/<int:id>')
def author_page(id):
    return render_template("author_page.html", author = Author.get_one_author({"id" : id}), all_books = Book.get_all_books())

@app.route('/delete_author/<int:id>')
def delete_author(id):
    Author.destroy({'id' : id})
    return redirect('/')

@app.route('/like_book', methods = ['POST'])
def like_book():
    