from prediction import predict
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'defaultkey'


@app.route('/', methods=['POST', 'GET'])
def get_data():
    return render_template('index.html')


@app.route('/submit', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        home_team = request.form['homeTeam']
        away_team = request.form['awayTeam']
        city = request.form['city']
        toss_winner = request.form['tossWinner']
        toss_decision = request.form['selector1']
        print(home_team, away_team, city, toss_winner, toss_decision)
        winner_team = predict(home_team, away_team, city, toss_winner, toss_decision).__str__()
        print("Winning Team is -> " + winner_team)
        home_team_name = convert_back_to_team_names(home_team).__str__()
        away_team_name = convert_back_to_team_names(away_team).__str__()
        flash("Match Prediction between " + home_team_name + " and " + away_team_name + " is higher for: " + winner_team)
    return render_template('index.html')
    # return render_template('results.html')


def convert_back_to_team_names(team):
    team_name = ""

    if team == 'Kolkata':
        team_name = "KKR"
    if team == "Bangalore":
        team_name = "RCB"
    if team == "Pune":
        team_name = "CSK"
    if team == "Jaipur":
        team_name = "RR"
    if team == "Delhi":
        team_name = "DD"
    if team == "Dharamshala":
        team_name = "KXIP"
    if team == "Hyderabad":
        team_name = "SRH"
    if team == "Mumbai":
        team_name = "MI"

    return team_name


if __name__ == '__main__':
    app.run()
