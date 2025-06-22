import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

iowa_file_path = 'home_data.csv'
home_data = pd.read_csv(iowa_file_path)

print(home_data.columns)
y = home_data.SalePrice

feature_names = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[feature_names]
print(X.describe())
print(X.head())

iowa_model = DecisionTreeRegressor(random_state = 1)
iowa_model.fit(X, y)

predictions = iowa_model.predict(X)
print("Predictions are: " + str(predictions))

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

iowa_model = DecisionTreeRegressor(random_state = 1)
iowa_model.fit(train_X, train_y)

val_predictions = iowa_model.predict(val_X)

# print the top few validation predictions
print(val_predictions[:5])
# print the top few actual prices from validation data
print(val_y.head())

val_mae = mean_absolute_error(val_predictions, val_y)
print(val_mae)

def get_mae(max_leaf_nodes, trained_X, value_X, trained_y, value_y):
    model = DecisionTreeRegressor(max_leaf_nodes = max_leaf_nodes, random_state = 0)
    model.fit(trained_X, trained_y)
    prediction_val = model.predict(value_X)
    mae = mean_absolute_error(value_y, prediction_val)
    return mae

candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate_max_leaf_nodes}

best_tree_size = min(scores, key = scores.get)
print(best_tree_size)

final_model = DecisionTreeRegressor(max_leaf_nodes = best_tree_size, random_state = 1)
final_model.fit(X, y)