from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "1_2_3---!"

@app.route('/')
def index():
    return render_template("index.html")

users_total = []

@app.route('/submit_me', methods=['POST'])
def submit_me():
    # this is the entire form below is being submitted from the index page
    if request.form['action'] == 'submit_me':
        row = {
            # NO LONGER NECESSARY AFTER CONNECTING DATABASE "id" : (len(friends)+1),
            "first_name" : request.form['first_name'],
            "last_name" : request.form['last_name'],
            "dojo_location" : request.form['dojo_location'],
            "fav_language" : request.form['fav_language'],
            "comments" : request.form['comments']
        }


        users_total.append(row)
        session['user'] = row
        session['users_total'] = users_total
        print("Got another one!")
        return redirect("/results")

        # be sure to redirect here; this is the part where on an e-commerce website, someone could be charged multiple times

@app.route('/results')
def results():
        return render_template("results.html", users_total = users_total)

if __name__ == "__main__":
    app.run(debug=True)