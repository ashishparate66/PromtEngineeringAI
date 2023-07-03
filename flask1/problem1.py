from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask application!"

@app.route('/greet/<username>')
def greet(username):
    return f"Hello, {username}!"

@app.route('/farewell/<username>')
def farewell(username):
    return f"Goodbye, {username}!"

@app.route('/meeting/<username>')
def meeting(username):
    return f"I am in meeting, {username}!"

if __name__ == '__main__':
    app.run(port=8181)
