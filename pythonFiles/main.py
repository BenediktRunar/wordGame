from flask import Flask, render_template
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
    return render_template('playerVsComputer.html')

if __name__ == '__main__':
    app.run(debug=True)