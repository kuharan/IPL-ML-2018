import unicodedata
import pandas
from Prediction import pred
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# @app.route('/success/<name>')
# def success(name):
#     return name

@app.route('/', methods=['POST', 'GET'])
def second():
    if request.method == 'POST':
        # extracting cigratePerDay by using request.form and converting it into string because request.form returns unicode
        homeTeam = request.form['homeTeam']
        awayTeam = request.form['awayTeam']
        city = request.form['city']
        tossWinner = request.form['tossWinner']
        tossDecision = request.form['selector1']

        print(homeTeam,awayTeam,city,tossWinner,tossDecision)
        pred(homeTeam,awayTeam,city,tossWinner,tossDecision)
    return render_template('index.html')


# Kolkata Mumbai City: Kolkata KKR Bat


if __name__ == '__main__':
    app.run()
