
import numpy as np
import pandas as pd

file_path = "./IMDB-Movie-Data.csv"
data = pd.read_csv(file_path)

print(data.info())
print(data.head(1))
print(type(data["Runtime (Minutes)"].values))