import pandas as pd
pd.set_option('display.max_rows', 5)
reviews = pd.read_csv("reviews.csv", index_col=0)
reviews.head()

#EX1
desc = reviews.description
print(desc)

#EX2
first_description = reviews.description[1]
print(first_description)

#iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded
#loc, meanwhile, indexes inclusively

#EX3
first_row = reviews.iloc[1] #to print first row
print(first_row)

#EX4
first_descriptions = reviews.description[:11]
print(first_descriptions)

#EX5
sample_reviews = reviews.loc[[1, 2, 3, 5, 8]]
print(sample_reviews)

#EX6
df = reviews.loc[[1, 2, 8], ['country', 'province', 'region_1', 'region_2']]
print(df)

#EX7
dff = reviews.loc[0:7, ['country', 'designation']]
print(dff)

#EX8
italian_wines = reviews.loc[reviews.country == 'Italy']
print(italian_wines)

#EX9
top_oceania_wines = reviews.loc[(reviews.country.isin(['Australia', 'New Zealand'])) & (reviews.points >= 95)]
print(top_oceania_wines)