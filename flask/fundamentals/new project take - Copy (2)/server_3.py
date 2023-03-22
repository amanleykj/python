from server_1 import *
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "1_2_3---!"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/redirect')
def redirect():
    return render_template("/redirect.html")


if __name__ == "__main__":
    app.run(debug=True)