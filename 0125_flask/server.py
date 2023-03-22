from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/coding'/'dojo'/'rules')          # The "@" decorator associates this route with the function immediately following
def hello_world(thing, written, here):
    return f"Hello Awesome Developer"



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.