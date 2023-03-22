from flask import Flask, render_template, request, redirect, session
from user import User

app = Flask(__name__)

app.secret_key = "reticulating_splines"

friends = []

@app.route('/')
def index():
    return render_template("index.html")

    # return render_template("show.html", name = session['name'], email = session['email'])

@app.route('/form_submit', methods=['POST'])
def form_submit():
    # this is the entire form below is being submitted from the index page
    if request.form['action'] == 'register':
        row = {
            # NO LONGER NECESSARY AFTER CONNECTING DATABASE "id" : (len(friends)+1),
            "first_name" : request.form['first_name'],
            "last_name" : request.form['last_name'],
            "email" : request.form['email'],
            "occupation" : request.form['occupation'],
            "password" : request.form['password']
        }

        User.save(row)
        # friends.append(row)
        # session['friend'] = row
        return redirect("/dashboard")

        # be sure to redirect here; this is the part where on an e-commerce website, someone could be charged multiple times

    else:
        for friend in friends:
            
            if request.form['email'] == friend['email']:

                if request.form['password'] == friend['password']:
                    print("Sucessful login done")
                    session['friend'] = friend
                    return redirect("/dashboard")
                else:
                    print("Wrong password")
                    return redirect("/")
            else:
                print("Wrong email")
                return redirect('/')

@app.route('/dashboard')
def dashboard():
    # if "friend" not in session:
    #     return redirect("/")
        return render_template("dashboard.html", friends=User.getAll())


# THIS BELOW WAS TOTALLY UNNEEDED; REFER TO NOTES ABOUT WHY THE RETURN WAS NOT NECESSARY
# @app.route('/form_submit', methods=['POST'])
# def form_submit():
#     print("Hey there")
#     return render_template("form_submit.html")

if __name__ == "__main__":
    app.run(debug=True)