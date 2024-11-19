import pandas as pd

df = pd.read_csv("spotify_songs.csv")
# print(df)
import numpy as np

# print(df.shape) # returns size of df rows and cols
# (32833, 23)
my_tuple =("Katy", "Joe", "Ryan", "Prathamm", "Ron" )  
#! a tuple is like a 'list' which can't be changed; retains the same order;  

# print(df.columns)  #returns name of cols

# print(df.head())

# print(df["playlist_genre"].value_counts()) #returns num of unique rows and times appearance in cols
# playlist_genre
# edm      6043   # most counts- 'mode'-- descriptive stats
# rap      5746
# pop      5507
# r&b      5431
# latin    5155
# rock     4951
# Name: count, dtype: int64

# print(df["playlist_genre"].mode())
# 0    edm
# Name: playlist_genre, dtype: object  # returns 'series'
# print(df["playlist_genre"].mode()[0])  # index position [0]- gives actual 'mode'
# edm  - 'mode'

# find median- take a numerical col

# print(df["duration_ms"].sum())
# 216000.0  - 'median'
# 225799.811622453  - 'mean'
# 4000 - 'min'
# 517810 - 'max'
# 513810 - 'range'=(max-min)
# 7413685215 - 'sum'

#! Sorting
# print (df.sort_values(by=["duration_ms"]))  # sort by col or row; 
#!data sorts in ascending order by default
# print (df.sort_values(by=["duration_ms"], ascending=False)) #now shortest song is last

# print(df.groupby("playlist_genre")["duration_ms"].min())
# #* first grp the songs into their "playlist_genre", then put into '[duration_ms]' what we want to find or compare through these grps; here we want 'min' value
# playlist_genre
# edm      31429
# latin    45000
# pop      37640
# r&b      31893
# rap      29493
# rock      4000
# Name: duration_ms, dtype: int64
# print(df.groupby("playlist_genre")["duration_ms"].max())  # will give max duration song in genres
# playlist_genre
# edm      515703
# latin    517810
# pop      490057
# r&b      506200
# rap      499400
# rock     517125
# Name: duration_ms, dtype: int64

#! Queries
# print(df.query("track_artist=='Ricky Martin'"))
#                      track_id  ... duration_ms
# 16335  7MkFd0UDHlILDrhBjGZH5K  ...      218996
# 17512  3OK8WgNRmp4F3ahXe6XX6l  ...      307867
# 17517  61hJK3EfAd1LDk7x5OrCTc  ...      247867
# 17530  0loDvz6U86bm7sAemXpyxu  ...      218547
# 17630  7MkFd0UDHlILDrhBjGZH5K  ...      218996
# 18192  4Z8tegTDUNyO2giIkkOld7  ...      335493
# 18487  00i0O74dXdaKKdCrqHnfXm  ...      211680
# 18882  7MkFd0UDHlILDrhBjGZH5K  ...      218996
# 19286  7DM4BPaS7uofFul3ywMe46  ...      259196
# 19837  7DM4BPaS7uofFul3ywMe46  ...      259196
# 21198  00i0O74dXdaKKdCrqHnfXm  ...      211680

# [11 rows x 23 columns]

mean_val= df["duration_ms"].mean()
# print(mean_val)
# 225799.811622453

# print(df.query("duration_ms > @mean_val"))
#! as 'mean_val' is not part of df col; use '@' for query to look outside scope!
#                      track_id  ... duration_ms
# 9      1IXGILkPm0tOCNeq00kCPa  ...      253040
# 14     55nMnifaQWKe3f9cbwOXwx  ...      255238
# 38     6m8SIT10j41SPpPFOknTmP  ...      247385
# 41     6oJ6le65B3SEqPwMRNXWjY  ...      228267
# 51     5rxKInBVj0QE87KenyDiLf  ...      266719
# ...                       ...  ...         ...
# 32822  00UpV14MDfk4CvrMbFvqji  ...      298125
# 32824  3zKST4nk4QJE77oLjUZ0Ng  ...      255093
# 32829  5Aevni09Em4575077nkWHz  ...      353120
# 32831  2m69mhnfQ1Oq6lGtXuYhgX  ...      367432
# 32832  29zWqhca3zt5NsckZqDf6c  ...      337500

# [13812 rows x 23 columns]

#! print(df.query(f"duration_ms >= {mean_val}"))
# another way to read 'mean_val' variable to execute its function

