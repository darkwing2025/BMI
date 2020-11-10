import flask
from flask import render_template, request
app = flask.Flask(__name__)

@app.route('/')
def root():
    return render_template("index.html")

@app.errorhandler(404)
def not_found(e):
    return "Oops, we cannot find the page you are lookig for"

@app.route('/calcbmi')
def calcbmi():
    name = request.args['name']
    height = float(request.args['height'])
    weight = float(request.args['weight'])
    bmi = round(weight/(height**2),1)
    return "{}'s BMI is {}.".format(name, bmi)
	
app.run(debug=True)
