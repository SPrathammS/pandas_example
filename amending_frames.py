import pandas as pd

languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])
rankings = pd.Series([3,1,2,4])

df = pd.DataFrame({
    "Languages": languages,
    "Ranking": rankings
})
# print (df)
#     Languages  Ranking
# 0      Python        3
# 1  JavaScript        1
# 2        HTML        2
# 3         SQL        4

df.loc[4] = ["PHP", 11]
# print(df)
#     Languages  Ranking
# 0      Python        3
# 1  JavaScript        1
# 2        HTML        2
# 3         SQL        4
# 4         PHP       11

# df.loc[3.5]= ["KESL", 20]
# # print(df)
# #       Languages  Ranking
# # 0.0      Python        3
# # 1.0  JavaScript        1
# # 2.0        HTML        2
# # 3.0         SQL        4
# # 4.0         PHP       11
# # 3.5        KESL       20

# df = df.sort_index()
# # print(df)
# #       Languages  Ranking
# # 0.0      Python        3
# # 1.0  JavaScript        1
# # 2.0        HTML        2
# # 3.0         SQL        4
# # 3.5        KESL       20
# # 4.0         PHP       11

# # df = df.reset_index()
# # print(df)
# #    index   Languages  Ranking
# # 0    0.0      Python        3
# # 1    1.0  JavaScript        1
# # 2    2.0        HTML        2
# # 3    3.0         SQL        4
# # 4    3.5        KESL       20
# # 5    4.0         PHP       11

# df = df.reset_index(drop=True) #* drop old index and renumber new index
# print (df)
# #     Languages  Ranking
# # 0      Python        3
# # 1  JavaScript        1
# # 2        HTML        2
# # 3         SQL        4
# # 4        KESL       20
# # 5         PHP       11

#------------------------------------------------
# print(df)

# Activity 1

new_data = pd.DataFrame({
    "Languages": [ "Java", "TypeScript"],
    "Ranking": [ 7,5]
})

# df = pd.concat([df, new_data])
# print(df)
#     Languages  Ranking
# 0      Python        3
# 1  JavaScript        1
# 2        HTML        2
# 3         SQL        4
# 4         PHP       11
# 0         PHP       11
# 1        Java        7
# 2  TypeScript        5

df = pd.concat([df, new_data], ignore_index = True)
# print(df)
#     Languages  Ranking
# 0      Python        3
# 1  JavaScript        1
# 2        HTML        2
# 3         SQL        4
# 4         PHP       11
# 5        Java        7
# 6  TypeScript        5

#* adding just like dictionary; 
df ["Ranking 2022"]= [4,1,2,3,10,6,5]  
# print(df)
#    Languages  Ranking  Ranking 2022
# 0      Python        3             4
# 1  JavaScript        1             1
# 2        HTML        2             2
# 3         SQL        4             3
# 4         PHP       11            10
# 5        Java        7             6
# 6  TypeScript        5             5
#! (line 32, 33 in Katy's code, using concat and horizontal axis column pasting )

# Activity 2

df ["Ranking 2020"] = [4,1,2,3,8,5,9]
df ["Ranking 2019"] = [4,1,2,3,8,5,10]
# print(df)
#    Languages  Ranking  Ranking 2022  Ranking 2020  Ranking 2019
# 0      Python        3             4             4             4 
# 1  JavaScript        1             1             1             1 
# 2        HTML        2             2             2             2 
# 3         SQL        4             3             3             3 
# 4         PHP       11            10             8             8 
# 5        Java        7             6             5             5 
# 6  TypeScript        5             5             9            10 
df.insert(3, "Ranking 2021", [3,1,2,4,11,5,7])
# print(df)
# Languages  Ranking  Ranking 2022  Ranking 2021  Ranking 2020  Ranking 2019
# 0      Python        3             4             3             4             4
# 1  JavaScript        1             1             1             1             1
# 2        HTML        2             2             2             2             2
# 3         SQL        4             3             4             3             3
# 4         PHP       11            10            11             8             8
# 5        Java        7             6             5             5             5
# 6  TypeScript        5             5             7             9            10

# df.rename(1 "Ranking":"Ranking 2023", [] ) #! error
df.rename(columns={"Ranking":"Ranking 2023"}, inplace=True)
# print(df)
#     Languages  Ranking 2023  Ranking 2022  Ranking 2021  Ranking 2020  Ranking 2019
# 0      Python             3             4             3             4             4     
# 1  JavaScript             1             1             1             1             1     
# 2        HTML             2             2             2             2             2     
# 3         SQL             4             3             4             3             3     
# 4         PHP            11            10            11             8             8     
# 5        Java             7             6             5             5             5     
# 6  TypeScript             5             5             7             9            10 
df = df.set_index("Languages")
print (df)