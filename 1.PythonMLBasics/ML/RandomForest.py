import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

iowa_file_path = 'home_data.csv'
home_data = pd.read_csv(iowa_file_path)

y = home_data.SalePrice

feature_names = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[feature_names]

rf_model = RandomForestRegressor()

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

rf_model.fit(val_X, val_y)

rf_val_predictions = rf_model.predict(val_X)

rf_val_mae = mean_absolute_error(rf_val_predictions, val_y)

print(rf_val_mae)