import sqlite3
import pandas

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute("SELECT * FROM countries WHERE area >= 2000000")
rows = cur.fetchall()
conn.close()

df = pandas.DataFrame.from_records(rows)
df.columns = ["Rank", "Country", "Areas", "Population"]
df.to_csv("countries_big_areas.csv", index=False)
