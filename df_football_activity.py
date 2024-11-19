import pandas as pd
df= pd.read_csv("results.csv")
# print(df)

# #diff kinds of tournaments played amd matches under each tournament
# print(df["tournament"].value_counts())
#? print (df["tournament"].unique())

# # most reported home team and away team
# print(df["home_team"].value_counts())
# print(df["home_team"].mode()[0])

# print(df["away_team"].value_counts())
# print(df["away_team"].mode()[0])


# least reported home team and away team

print(df["away_team"].value_counts())