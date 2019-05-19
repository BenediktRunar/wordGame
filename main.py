from flask import Flask, render_template, url_for, request, redirect
import os
from letters import *
from computersTurn import *
from game import *

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')

# home site
@app.route("/")
def home():
    return "Hello from the pornvbspmdv"


#if __name__ == '__main__':
#    app.run(debug=True)