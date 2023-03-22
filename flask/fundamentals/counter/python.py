from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

app.secret_key = "reticulating_____splines!"

@app.route("/")
def index():
    if "num_count" not in session:
        session["num_count"] = 0
    else:
        session["num_count"] += 1
    return render_template("index.html")

@app.route("/double")
def double():
    if "num_count" in session:
        session["num_count"] += 2
    return render_template("index.html")

@app.route("/custom_value", methods=["POST"])
def custom_value():
    if request.form['action'] == "custom_value":
        print("Try hard.")
        session["num_count"] += request.form[int('custom_value')]
    return redirect("index.html")

@app.route("/destroy_session")
def destroy_session():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)