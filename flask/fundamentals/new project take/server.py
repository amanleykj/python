from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "1_2_3---!"


# create a page that takes a user input number from 1 through 10, and then shows 
# a different color div that corresponds to a pre-set color for those 10

@app.route('/users', methods=['POST'])
def create_user():
    users_all = []
    if request.form['action'] == "register":
        user_data = {
            "id" : (len(users_all)+1),
            "name": request.form['name'],
            "email": request.form['email']
        }
        session['name'] = request.form['name']
        session['email'] = request.form['email']
        users_all.append(user_data)
        print("All good until here.")
        return redirect('/')
    
    else:
    
        return redirect('/wrong')

@app.route('/wrong')
def wrong_input():
    return render_template('wrong.html')

@app.route('/check_cookie', methods=['POST'])
def check_cookie():
    if request.form['name'] == session['name']:
        if request.form['email'] == session['email']:
     
            print(f"You input the name { 'name' } and email { 'email' } correctly.")
            return render_template("index.html")

    else:
        print("The name and email aren't right.")


    # print("Got Post Info")
    # session['name'] = request.form['name']
    # session['email'] = request.form['email']
    # return redirect('/show')


@app.route('/')
def index():
    return render_template("index.html")

    # return render_template("show.html", name = session['name'], email = session['email'])

if __name__ == "__main__":
    app.run(debug=True)