import pandas as pd

df = pd.read_excel("dev_rankings.xlsx")
# print(df)
df = df.set_index("Languages")
# print(df)
# print(df["Ranking 2019"])
# print (df[["Ranking 2022", "Ranking 2021"]])  #! outer brac- 'reference'; inner sq brac- 'list'

# print(df.loc["HTML"]) # location of " " in all columns 
# slice notation- start, stop, step

# print (df.loc["Python":"HTML":1, "Ranking 2023":"Ranking 2019":2])

# print (df.iloc[3])

# print (df.at["HTML", "Ranking 2019"])

print (df.head(6))