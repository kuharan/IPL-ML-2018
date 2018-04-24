import pandas as pd
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
import csv


def pred(home_team, away_team, city, toss_winner, toss_decision):
    matches_cleaned_data = pd.read_csv('./Dataset/matches_cleaned.csv')
    matches_df = matches_cleaned_data[['team1', 'team2', 'city', 'toss_winner', 'toss_decision', 'winner']]

    # Split-out validation dataset
    array = matches_df.values
    x = array[:, 0:5]
    y = array[:, 5]
    validation_size = 0.10
    seed = 7
    x_train, x_validation, y_train, y_validation = model_selection.train_test_split(x, y, test_size=validation_size,
                                                                                    random_state=seed)

    # Test options and evaluation metric
    knn = DecisionTreeClassifier()
    knn.fit(x_train, y_train)
    results = converter(home_team, away_team, city, toss_winner, toss_decision)
    predictions = knn.predict([results])
    team = ''
    if predictions[0] == '6':
        team = 'KKR'
    if predictions[0] == "5":
        team = 'RCB'
    if predictions[0] == "9":
        team = 'CSK'
    if predictions[0] == "10":
        team = 'RR'
    if predictions[0] == "7":
        team = 'DD'
    if predictions[0] == "8":
        team = 'KXIP'
    if predictions[0] == "1":
        team = 'SRH'
    if predictions[0] == "2":
        team = 'MI'
    print(team)

    return team


def converter(home_team, away_team, city, toss_winner, toss_decision):
    list = []
    if home_team == 'Kolkata':
        list.append(6)
    if home_team == "Bangalore":
        list.append(5)
    if home_team == "Pune":
        list.append(9)
    if home_team == "Jaipur":
        list.append(10)
    if home_team == "Delhi":
        list.append(7)
    if home_team == "Dharamshala":
        list.append(8)
    if home_team == "Hyderabad":
        list.append(1)
    if home_team == "Mumbai":
        list.append(2)

    if away_team == "Kolkata":
        list.append(6)
    if away_team == "Bangalore":
        list.append(5)
    if away_team == "Pune":
        list.append(9)
    if away_team == "Jaipur":
        list.append(10)
    if away_team == "Delhi":
        list.append(7)
    if away_team == "Dharamshala":
        list.append(8)
    if away_team == "Hyderabad":
        list.append(1)
    if away_team == "Mumbai":
        list.append(2)

    if city[6:] == "Kolkata":
        list.append(7)
    if city[6:] == "Bangalore":
        list.append(5)
    if city[6:] == "Pune":
        list.append(2)
    if city[6:] == "Jaipur":
        list.append(11)
    if city[6:] == "Delhi":
        list.append(8)
    if city[6:] == "Dharamshala":
        list.append(24)
    if city[6:] == "Hyderabad":
        list.append(1)
    if city[6:] == "Mumbai":
        list.append(6)

    if toss_winner == "KKR":
        list.append(6)
    if toss_winner == "RCB":
        list.append(5)
    if toss_winner == "CSK":
        list.append(9)
    if toss_winner == "RR":
        list.append(10)
    if toss_winner == "DD":
        list.append(7)
    if toss_winner == "KXIP":
        list.append(8)
    if toss_winner == "SRH":
        list.append(1)
    if toss_winner == "MI":
        list.append(2)

    if toss_decision == "Bat":
        list.append(2)
    if toss_decision == "Field":
        list.append(1)
    print(list)

    return list


# OUTPUT # Kolkata Mumbai City: Kolkata KKR Bat

# prediction from site scrape data
def calculate_ef_score(home, away):
    data = pd.read_csv('./Dataset/_team_rank.csv')
    home_score = data.loc[data['Team'] == home]['sum']
    away_score = data.loc[data['Team'] == away]['sum']

    print(home_score, '\n', away_score)


calculate_ef_score('Royal Challengers Bangalore', 'Mumbai Indians')
