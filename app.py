from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
