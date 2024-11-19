import pandas as pd
from ydata_profiling import ProfileReport

# df = pd.read_csv("results.csv")

# profile = ProfileReport(df, title = "International Results")

# profile.to_file('results_report.html')

# df = pd.read_csv("shootouts.csv")

# profile = ProfileReport(df, title = "Shootout Results")

# profile.to_file('shootouts_report.html')

df = pd.read_csv("spotify_songs.csv")
print(df)
# profile = ProfileReport(df, title = "Spotify Results")

# profile.to_file('spotify_report.html')