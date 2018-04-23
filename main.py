from prediction import pred
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def second():
    if request.method == 'POST':
        home_team = request.form['homeTeam']
        away_team = request.form['awayTeam']
        city = request.form['city']
        toss_winner = request.form['tossWinner']
        toss_decision = request.form['selector1']
        print(home_team, away_team, city, toss_winner, toss_decision)
        winner_team = pred(home_team, away_team, city, toss_winner, toss_decision)
        print("Winning Team is -> " + winner_team)

    return render_template('index.html')


# Kolkata Mumbai City: Kolkata KKR Bat

if __name__ == '__main__':
    app.run()
