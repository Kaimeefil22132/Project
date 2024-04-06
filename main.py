from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/sea')
def index_one():
    return render_template('sea.html')
@app.route('/weather')
def index_two():
    return render_template('weather.html')
@app.route('/global')
def index_three():
    return render_template('global.html')
@app.route('/tree')
def index_four():
    return render_template('tree.html')
@app.route('/gaz')
def index_five():
    return render_template('gaz.html')
@app.route('/car')
def index_six():
    return render_template('car.html')
 
app.run(debug=True)