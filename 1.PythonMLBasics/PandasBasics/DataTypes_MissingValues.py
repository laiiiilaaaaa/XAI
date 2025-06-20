import pandas as pd
pd.set_option('display.max_rows', 5)
reviews = pd.read_csv("reviews.csv", index_col=0)

#EX1
dtype = reviews.points.dtype
print(dtype)

#EX2
point_strings = reviews.points.astype('str')
print(point_strings.dtype)

#EX3
n_missing_prices = reviews['price'].isnull().sum()
print(n_missing_prices)

#EX4
reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)
print(reviews_per_region)