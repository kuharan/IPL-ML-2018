from Prediction import pred
from flask import Flask, render_template, request,flash


app = Flask(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route('/', methods=['POST', 'GET'])
def second():
    if request.method == 'POST':
        home_team = request.form['homeTeam']
        away_team = request.form['awayTeam']
        city = request.form['city']
        toss_winner = request.form['tossWinner']
        toss_decision = request.form['selector1']
        print(home_team, away_team, city, toss_winner, toss_decision)
        winner_team=pred(home_team, away_team, city, toss_winner, toss_decision)
        flash("winning team=="+winner_team)
    return render_template('index.html')


# Kolkata Mumbai City: Kolkata KKR Bat

if __name__ == '__main__':
    app.run()
