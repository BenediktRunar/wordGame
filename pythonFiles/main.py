from flask import Flask, render_template, url_for
from letters import *
app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html', title='Home')

@app.route("/twoPlayer")
def TwoPlayer():
    return render_template('twoPlayer.html', title='P vs P')

@app.route("/playerVsComputer")
def playerVsComputer():

    lettersChosen = letters()
    return render_template('playerVsComputer.html', title='P vs Ai', letters = lettersChosen)

if __name__ == '__main__':
    app.run(debug=True)