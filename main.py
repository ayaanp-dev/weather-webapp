from flask import Flask, render_template, request
from apihandler import return_weather
import requests

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/", methods=["POST"])
def weather_form():
	city = request.form["city"]
	units = request.form["units"]
	return render_template("index.html", weather=return_weather(city, units))

@app.route("/about")
def about():
	return "<h1>Im an 8th grader based in Phoenix, AZ, USA</h1>.<br><a href='/'>Home</a>"

if __name__ == '__main__':
	app.run(debug=True)