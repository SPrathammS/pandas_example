import pandas as pd

#! first dataset ----------------------------------------

# df = pd.read_excel("results2024-11-25-1439.xlsx")
# # print(df.info()) 
# # print (df.columns)
# # print(df['Upload (Mb/s)'].max())
# print(df.sort_values(by="Upload (Mb/s)")) # Upload ascending sort
# print(df.sort_values(by="Upload (Mb/s)", ascending=False))  # Upload descending sort (ascending=False)
# print(df.describe())   # returns all descriptive stats
# print(df['Download (Mb/s)']>df['Download (Mb/s)'].mean())

#! group dataset  ----------------------------------------

df2= pd.read_excel("group_results.xlsx")
# print(df2)  # named the dataframe as "df2"
# print(df2.info())
print(df2.describe())   # gives all the descriptive data, with means, medians and IQRs of group data
# print(df2.columns)

print(df2["Median Upload"].mean())  #> 28.44416179882511
print(df2["Median Download"].mean()) #> 89.44838951397493

df2=df2.set_index("Entry")

print(df2)