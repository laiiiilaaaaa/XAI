import pandas as pd
pd.set_option('display.max_rows', 5)
reviews = pd.read_csv("reviews.csv", index_col=0)

#EX1
reviews_written = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()
print(reviews_written)

#EX2
best_rating_per_price = reviews.groupby('price').points.max()
print(best_rating_per_price)

#EX2
price_extremes = reviews.groupby(['country']).price.agg(['min', 'max'])
print(price_extremes)

#EX3
sorted_countries = reviews.groupby(['country']).price.agg(['min', 'max']).sort_values(by = ['min', 'max'], ascending = False)
print(sorted_countries)

#EX4
reviewer_mean_ratings = reviews.groupby('taster_name')['points'].mean()
print(reviewer_mean_ratings)

#EX5
country_variety_counts = reviews.groupby(['country', 'taster_name']).size().sort_values(ascending=False)
print(country_variety_counts)