import pandas as pd  # import whole library, panda= pd, python= py

# languages = pd.Series(["Python", "Javascript", "HTML", "SQL"])
# # #* variable = pandas. Series 'Class' (["string",""])
# # print(languages)
# # # 0        Python   # 0= index position
# # # 1    Javascript
# # # 2          HTML
# # # 3           SQL
# # # dtype: object  # object= strings or mix of data type 
# # #! cant find [median and mean] of 'text based objects'

# sec = pd.Series([3,1,2,4])  
# # #* variable = panda 'Series' Class ([integer, integer])
# # print(sec)
# # # 0    3
# # # 1    1
# # # 2    2
# # # 3    4
# # # dtype: int64  # int64= 64-bits wide integer, as there are diff types of integer. (any integer upto 2**63) 

# # combine 2 series (1D) into table(2D)- Dataframe 'spreadsheets version'

# # table_name = pd.DataFrame([("Anne", 30), ("Bill", 27), ("charlie", 55)])
# # #* variable = pandas. Class 'DataFrame' [list("Tuple- russian doll")]
# # print(table_name)
# # #          0   1
# # # 0     Anne  30
# # # 1     Bill  27
# # # 2  charlie  55
# #* tabular str has been formed

# #! columns need names -- , columns = ["Name", "Age"]
# # table_name = pd.DataFrame([("Anne", 30), ("Bill", 27), ("charlie", 55)], columns=["Name", "Age"])
# # print(table_name)
# # #       Name  Age
# # # 0     Anne   30
# # # 1     Bill   27
# # # 2  charlie   55
# # #* we have positional and key arguments, here when assigning 'name and age' to columns

# #! 1st method- 'dictionary' way of making dataframe from series

# # df = pd.DataFrame({
# #     "Languages": languages,
# #     "Rankings": sec
# # })
# # #* using a dictionary like key: value format to make a table from series
# # print(df)
# # #     Languages  Rankings
# # # 0      Python         3
# # # 1  Javascript         1
# # # 2        HTML         2
# # # 3         SQL         4


# #! 2nd method - 'concat'

# df = pd.concat([languages,sec], axis=1)  
# #* axis- 'parameter', 1 - keyword argument for columns to be horizontally arranged, default is vertical- meaning it stacks all columns
# #! variable = panda. 'concat' function ([ , ], parameter = 'keyword' )
# # 0        Python
# # 1    Javascript
# # 2          HTML
# # 3           SQL
# # 0             3
# # 1             1
# # 2             2
# # 3             4
# # dtype: object

# #             0  1
# # 0      Python  3
# # 1  Javascript  1
# # 2        HTML  2
# # 3         SQL  4

# df.columns=["Languages", "Rankings"]
# print(df)
# #     Languages  Rankings
# # 0      Python         3
# # 1  Javascript         1
# # 2        HTML         2
# # 3         SQL         4

#--------------------------------------------------------------

# df = pd.read_csv("speeds.csv")
# # variable = pandas. 'read_csv' function ("filename.csv")
# print(df)

df = pd.read_excel("speeds.xlsx")
print(df)
#! Error: install 'openpyxl'
# pip install openpyxl
 