import pandas
from matplotlib import pyplot as plt
data = pandas.read_csv("countries-by-area.txt")
data["density"] = data["population_2013"] / data["area_sqkm"]
data = data.sort_values(by="density", ascending=False)

for index, row in data[:5].iterrows():
    print(row["country"] )
