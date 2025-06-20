import pandas as pd
reviews = pd.read_csv("reviews.csv", index_col=0)
test = pd.read_csv("test.csv", index_col = 0)

#EX1
renamed = reviews.rename(columns = {'region_1': 'region', 'region_2': 'locale'})

#EX2
reindex = reviews.rename(index = {'name': 'wine'})

#EX3
combined_files = pd.concat([reviews, test])
print(combined_files)

#EX4
'''powerlifting_combined = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))
combining two tables into one'''