from flask import Flask, render_template, redirect, session, request
import random
app = Flask(__name__)

app.secret_key = "reticulating__1__splines!"

@app.route('/')
def randomize():
    if "random_num" not in session:
        session['random_num'] = random.randint(1,100)
        print(session['random_num'])
    return render_template("index.html")


@app.route('/guessed_low', methods=['POST'])
def guessed_low():
    return render_template("guessed_low.html")

    if request.form['value'] == session['random_num']:
        return render_template("got_it.hmtl")
    else:
        return render_template("guessed_lot.html")


@app.route('/guessed_high', methods=['POST'])
def guessed_high():
    return render_template("guessed_low.html")


# @app.route("/double")
# def double():
#     if "num_count" in session:
#         session["num_count"] += 2
#     return render_template("index.html")

# @app.route("/custom_value", methods=["POST"])
# def custom_value():
#     if request.form['action'] == "custom_value":
#         print("Try hard.")
#         session["num_count"] += request.form[int('custom_value')]
#     return redirect("index.html")

# @app.route("/destroy_session")
# def destroy_session():
#     session.clear()
#     return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)