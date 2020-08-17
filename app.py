
from flask import Flask, render_template, request

#import model
import json
import base64
from urllib.parse import unquote

app = Flask(__name__)

@app.route("/")
def root():
	return render_template("index.html")

@app.route("/index")
def index():
	return render_template("index.html")


@app.route("/buscar")
def buscar():
	return render_template("buscar.html")


if __name__ == "__main__":
	app.run(host='0.0.0.0',ssl_context='adhoc',debug = True)
1