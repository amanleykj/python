from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "charge_of_everything"

total_now = 5

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/count', methods=['POST'])
def count():
    if request.button['action'] == "add":
        total_now = total_now + 1
        print("This is working +++")
        return redirect('/count')
    elif request.button['action'] == "substract":
        total_now = total_now - 1
        print("This is working ---")
        return redirect('/count')
    elif request.button['action'] == "reset":
        total_now = 0
        print("This is working RESET")
        return redirect('/count')
    else:
        return render_template('/count.html')


if __name__ == "__main__":
    app.run(debug=True)