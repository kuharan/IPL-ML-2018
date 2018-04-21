import pandas as pd
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier

def pred(homeTeam,awayTeam,city,tossWinner,tossDecision):
    matches_cleaned_data=pd.read_csv('./Dataset/matches_cleaned.csv')
    # print(matches_cleaned_data)

    matches_df = matches_cleaned_data[['team1', 'team2', 'city', 'toss_winner', 'toss_decision', 'winner']]
    # print(matches_df)

    # Split-out validation dataset
    array = matches_df.values
    X = array[:, 0:5]
    Y = array[:, 5]
    validation_size = 0.10
    # print(X)
    # print(Y)
    seed = 7
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
    # Test options and evaluation metric
    seed = 7
    scoring = 'accuracy'
    models = [('CART', DecisionTreeClassifier())]

    results = []
    names = []

    knn = DecisionTreeClassifier()
    knn.fit(X_train, Y_train)
    results=converter(homeTeam,awayTeam,city,tossWinner,tossDecision)
    # l=[]
    # l.append(results)
    predictions = knn.predict([results])
    print(predictions)
    return predictions
def converter(homeTeam,awayTeam,city,tossWinner,tossDecision):
    list=[]
    if(homeTeam=="Kolkata"):
        list.append(6)
    if (homeTeam == "Bangalore"):
        list.append(5)
    if (homeTeam == "Pune"):
        list.append(9)
    if (homeTeam == "Jaipur"):
        list.append(10)
    if (homeTeam == "Delhi"):
        list.append(7)
    if (homeTeam == "Dharamshala"):
        list.append(8)
    if (homeTeam == "Hyderabad"):
        list.append(1)
    if (homeTeam == "Mumbai"):
        list.append(2)
    if (awayTeam == "Kolkata"):
        list.append(6)
    if (awayTeam == "Bangalore"):
        list.append(5)
    if (awayTeam == "Pune"):
        list.append(9)
    if (awayTeam == "Jaipur"):
        list.append(10)
    if (awayTeam == "Delhi"):
        list.append(7)
    if (awayTeam == "Dharamshala"):
        list.append(8)
    if (awayTeam == "Hyderabad"):
        list.append(1)
    if (awayTeam == "Mumbai"):
        list.append(2)

    if (city[6:] == "Kolkata"):
        list.append(7)
    if (city[6:] == "Bangalore"):
        list.append(5)
    if (city[6:] == "Pune"):
        list.append(2)
    if (city[6:] == "Jaipur"):
        list.append(11)
    if (city[6:] == "Delhi"):
        list.append(8)
    if (city[6:] == "Dharamshala"):
        list.append(24)
    if (city[6:] == "Hyderabad"):
        list.append(1)
    if (city[6:] == "Mumbai"):
        list.append(6)



    if (tossWinner == "KKR"):
        list.append(6)
    if (tossWinner == "RCB"):
        list.append(5)
    if (tossWinner == "CSK"):
        list.append(9)
    if (tossWinner == "RR"):
        list.append(10)
    if (tossWinner == "DD"):
        list.append(7)
    if (tossWinner == "KXIP"):
        list.append(8)
    if (tossWinner == "SRH"):
        list.append(1)
    if (tossWinner == "MI"):
        list.append(2)

    if (tossDecision == "Bat"):
        list.append(2)
    if (tossDecision == "Field"):
        list.append(1)
    print(list)
    return list

# Kolkata Mumbai City: Kolkata KKR Bat






