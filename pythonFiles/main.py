from flask import Flask, render_template
from letters import *
from computersTurn import *
app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html')


@app.route("/twoPlayer")
def TwoPlayer():
    return render_template('twoPlayer.html')


@app.route("/playerVsComputer")
def playerVsComputer():
    l = letters()
    w = computersTurn((''.join(l)).lower())
    return render_template('playerVsComputer.html', l = l, word = w)

if __name__ == '__main__':
    app.run(debug=True)