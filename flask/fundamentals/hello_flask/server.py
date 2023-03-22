from flask import Flask, render_template
app = Flask(__name__)


# @app.route('/')
# def hello_world(phrase):
#     return render_template("hello.html", phrase="Hello", times=5)

@app.route('/')
def checkerboard_one():
    return render_template("checker.html", num1 = 8, num2 = 8)

@app.route('/<int:num1>')
def checkerboard_two(num1):
    return render_template("checker.html", num1 = num1, num2 = 8)

@app.route('/<int:num1>/<int:num2>')
def checkerboard_three(num1, num2):
    return render_template("checker.html", num1 = num1, num2 = num2)

@app.route('/<int:num1>/<int:num2>/<string:color1>')
def checkerboard_four(num1, num2, color1):
    return render_template("checker.html", num1 = num1, num2 = num2, color1 = color1)

@app.route('/<int:num1>/<int:num2>/<string:color1>/<string:color2>')
def checkerboard_five(num1, num2, color1, color2):
    return render_template("checker.html", num1 = num1, num2 = num2, color1 = color1, color2 = color2)


# @app.route('/play')
# def squares_one():
#     return render_template("hello.html", num = 3, color = "blue")

# @app.route('/play/<int:num>')
# def squares_two(num):
#     return render_template("hello.html", num = num, color = "blue")

# @app.route('/play/<int:num>/<string:color>')
# def squares_three(num, color):
#     return render_template("hello.html", num = num, color = color)

# @app.route('/play/<int:x>')
# def level_one(x):
#     return render_template("hello.html", x = x)

# @app.route('/play/<int:x>/<string:color>')
# def level_one(x, color):
#     return render_template("hello.html", x = x, color = color)

# @app.route('/repeat/<int:num>/<string:word>')
# def repeater(num, word):
#     return f"Hello {num * word}

# @app.route('/hello/<name>/<id>')
# def hello(name, id):
#     return f"Hello {name}! Your ID is {id}."

if __name__=="__main__":
    app.run(debug=True)