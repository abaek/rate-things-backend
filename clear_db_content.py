# Connect to the database.
import pymysql
conn = pymysql.connect(
    db='example',
    user='root',
    passwd='hello123',
    host='localhost')
c = conn.cursor()

# Insert some example data.
c.execute("DELETE FROM movies")
conn.commit()

# Print the contents of the database.
c.execute("SELECT * FROM movies")
print([(r[0], r[1]) for r in c.fetchall()])

