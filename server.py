import flask
from flask import render_template, request
app = flask.Flask(__name__)

@app.route('/')
def root():
    return render_template("index.html")

@app.errorhandler(404)
def not_found(e):
    return "Oops, we cannot find the page you are lookig for"

@app.route('/calcbmi', methods=['GET', 'POST'])
def calcbmi():
    name = request.form.get('name')
    height = float(request.form.get('height'))
    weight = float(request.form.get('weight'))
    bmi = round(weight/(height**2),1)
    return "{}'s BMI is {}.".format(name, bmi)
	
app.run(debug=True)
