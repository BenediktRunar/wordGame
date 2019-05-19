from flask import Flask, render_template, url_for, request, redirect
from letters import *
from computersTurn import *
from game import *

app = Flask(__name__)

# home site
@app.route("/")
def home():
    return "Hello from the pornvbspmdv"


#if __name__ == '__main__':
#    app.run(debug=True)