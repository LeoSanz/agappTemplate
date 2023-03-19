# Import the Flask class and the render_template function from the Flask package
from flask import Flask, render_template

# Create a new instance of the Flask class and assign it to the variable 'app'
app = Flask(__name__)

# Decorator that tells Flask to call the 'hello_world' function when a user visits the root URL ('/')
@app.route('/')
def hello_world():
    # Render the 'index.html' template file and return the resulting HTML to the user's web browser
    return render_template('index.html')

# Check whether the current module is being run as the main program
if __name__ == '__main__':
    # Start the Flask web server with debugging enabled and listen on all available network interfaces
    app.run(debug=True, host='0.0.0.0')
