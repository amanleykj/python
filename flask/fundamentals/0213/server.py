from flask import Flask, render_template, request, redirect, session
from user import User

app = Flask(__name__)

app.secret_key = "reticulating_splines"

friends = []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/form_submit', methods=['POST'])
def form_submit():
    if request.form['action'] == 'register':
        row = {
            "first_name" : request.form['first_name'],
            "last_name" : request.form['last_name'],
            "email" : request.form['email'],
            "occupation" : request.form['occupation'],
            "password" : request.form['password']
        }

        friend_id = User.save(row)
        print(f"The friend id is {friend_id}.")
        session['friend_id'] = friend_id
        
        return redirect("/dashboard")

    else:

        this_friend = User.getOneByEmail(request.form)
        print("This is the friend.")
        print(this_friend)
        if this_friend:
            if request.form['password'] == this_friend.password:
                session['friend_id'] = this_friend.id
                return redirect('/dashboard')
            else:
                return redirect('/')

@app.route('/dashboard')
def dashboard():
        return render_template("dashboard.html", friends = User.getAll())

@app.route('/home')
def home():
        return render_template("home.html", friends = User.getAll())

@app.route('/friends/<int:id>/edit')
def updateView(id):
    return render_template("update.html", friend = User.getOne({'id' : id}))

@app.route("/friends/<int:id>/update", methods=['POST'])
def update(id):
    row = {
            "id" : id,
            "first_name" : request.form['first_name'],
            "last_name" : request.form['last_name'],
            "email" : request.form['email'],
            "occupation" : request.form['occupation'],
            "password" : request.form['password']
    }
    
    User.update(row)
    return redirect('/dashboard')

@app.route("/friends/<int:id>/destroy")
def destroy(id):
    User.destroy({'id' : id})
    return redirect('/dashboard')

@app.route("/create_friend", methods=["POST"])
def create_friend():

    row = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "occupation" : request.form["occupation"]
    }

    User.save1(row)
    print("This worked.")
    return redirect("/home")

if __name__ == "__main__":
    app.run(debug=True)