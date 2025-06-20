import pandas as pd
pd.set_option('display.max_rows', 5)
reviews = pd.read_csv("reviews.csv", index_col=0)
reviews.head()

#EX1
median_points = reviews.points.median()
print(median_points)

#EX2
countries = reviews.country.unique()
print(countries)

#EX3
reviews_per_country = reviews.country.value_counts()
print(reviews_per_country)

#EX4
centered_price = reviews.price - reviews.price.mean()
print(centered_price)

#EX5
bargain_wine = reviews.loc[(reviews.points / reviews.price).idxmax(), 'designation']
print(bargain_wine)

#EX6
n_troop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_troop, n_fruity], index=['tropical', 'fruity'])
print(descriptor_counts)

#EX7
def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(stars, axis='columns')
print(star_ratings)