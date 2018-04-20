import unicodedata
import pandas

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return name


@app.route('/')
def first():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def second():
    if request.method == 'POST':
        # extracting cigratePerDay by using request.form and converting it into string because request.form returns unicode
        homeTeam = request.form['homeTeam']
        awayTeam = request.form['awayTeam']
        city = request.form['city']
        tossWinner = request.form['tossWinner']
        tossDecision = request.form['tossDecision']

        print(homeTeam, awayTeam, city, tossWinner, tossDecision)
        # Prediction(homeTeam,awayTeam,city,tossWinner,tossDecision)
        return "ok"


if __name__ == '__main__':
    app.run()
