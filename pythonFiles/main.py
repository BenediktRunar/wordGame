from flask import Flask, render_template
import letters
app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    print('<p>letters</p>')
    return render_template('home.html')

@app.route("/twoPlayer")
def TwoPlayer():
    return render_template('twoPlayer.html')

@app.route("/playerVsComputer")
def playerVsComputer():
    return render_template('playerVsComputer.html')

if __name__ == '__main__':
    app.run(debug=True)