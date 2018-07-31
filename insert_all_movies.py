import json
import pymysql

conn = pymysql.connect(
    db='example',
    user='root',
    passwd='hello123',
    host='localhost')
c = conn.cursor()

with open('movies.json', 'r') as f:
    movies = json.load(f)
    for m in movies:
        c.execute("INSERT INTO movies VALUES ('{}', {})".format(m["title"].replace("'", "''"), m["rating"]))
conn.commit()

# Print the contents of the database.
c.execute("SELECT * FROM movies")
print([(r[0], r[1]) for r in c.fetchall()])

