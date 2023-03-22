from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard_one():
    return render_template("checker.html", row = 8, col = 8)

@app.route('/<int:row>')
def checkerboard_two(row):
    return render_template("checker.html", row = row, col = 8)

@app.route('/<int:row>/<int:col>')
def checkerboard_three(row, col):
    return render_template("checker.html", row = row, col = col)

@app.route('/<int:row>/<int:col>/<string:color1>')
def checkerboard_four(row, col, color1):
    return render_template("checker.html", row = row, col = col, color1 = color1)

@app.route('/<int:row>/<int:col>/<string:color1>/<string:color2>')
def checkerboard_five(row, col, color1, color2):
    return render_template("checker.html", row = row, col = col, color1 = color1, color2 = color2)


if __name__=="__main__":
    app.run(debug=True)