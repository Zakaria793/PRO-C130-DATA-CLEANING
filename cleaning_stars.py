import pandas as pd
import csv
df = pd.read_csv("final_stars.csv")
print (df.columns)
del df["Unnamed: 6"]
del df["Unnamed: 0"]
del df["Star_name.1"]
del df["Distance.1"]
del df["Mass.1"]
del df["Radius.1"]
df.to_csv("finalstarscleaned.csv")