from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "1_2_3---!"

users_total = []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    if request.form['action'] == "register":
        data = {
            "id" : (len(users_total)+1),
            "name": request.form['name'],
            "email": request.form['email']
        }

        users_total.append(data)
        print(users_total)
        return redirect('/')
    else:
        return redirect('/show')

    #     return redirect("/")
    
    # else:
    #     return redirect("/show")    
    
    # print("Got Post Info")
    # session['name'] = request.form['name']
    # session['email'] = request.form['email']
    # return redirect('/show')


@app.route('/show')
def show_user():
    render_template("show.html")
    
    
    return render_template("show.html", name = session['name'], email = session['email'])

if __name__ == "__main__":
    app.run(debug=True)