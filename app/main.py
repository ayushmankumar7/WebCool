from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_view():
	return "<h1>Yes! Ayush ! It's Working </h1>"
