from flask import Flask, render_template, url_for
from letters import *
from computersTurn import *
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

    l = letters()
    temp = [i[0] for i in l]
    w = computersTurn((''.join(temp)).lower())
    return render_template('playerVsComputer.html', l = l, word = w, title='P vs Ai')

if __name__ == '__main__':
    app.run(debug=True)