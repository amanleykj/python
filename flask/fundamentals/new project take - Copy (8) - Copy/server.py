from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "1_2_3---!"


@app.route('/')
def index():
    render_template("index.html")

    # return render_template("show.html", name = session['name'], email = session['email'])

if __name__ == "__main__":
    app.run(debug=True)