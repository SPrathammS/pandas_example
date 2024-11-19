import pandas as pd

df = pd.read_csv("results.csv")

# print (df.head(20))  # prints first 20 rows with headings
# print(df.info())  #* general data exploration and facts about the dataframe- rows, cols, datatype
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 45315 entries, 0 to 45314
# Data columns (total 9 columns):
#  #   Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
#  0   date        45315 non-null  object
#  1   home_team   45315 non-null  object
#  2   away_team   45315 non-null  object
#  3   home_score  45315 non-null  int64
#  4   away_score  45315 non-null  int64
#  5   tournament  45315 non-null  object
#  6   city        45315 non-null  object
#  7   country     45315 non-null  object
#  8   neutral     45315 non-null  bool
# dtypes: bool(1), int64(2), object(6)
# memory usage: 2.8+ MB
# None
#! qualitative data type- (nominal/ordinal)-- here nominal in football eg- team name, city
#! quantitative data type - (discrete/continuous/ratio/interval) -- here discrete{whole num- score}, ratio{ratio- True/False}    
# print(df.describe())    #* numerical col- descriptive stats- means, median, IQR
#          home_score    away_score
# count  45315.000000  45315.000000
# mean       1.739314      1.178241
# std        1.746904      1.392095
# min        0.000000      0.000000
# 25%        1.000000      0.000000
# 50%        1.000000      1.000000
# 75%        2.000000      2.000000
# max       31.000000     21.000000

print(df["home_score"].value_counts(normalize=True)*100)

mask = df["home_score"]<4

masked_df = df[mask]

print(masked_df["home_score"].mean())