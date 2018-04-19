import pandas as pd
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier

matches_cleaned_data=pd.read_csv('./matches_cleaned.csv')
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

predictions = knn.predict([[2, 3, 6, 3, 2]])
print(predictions)
