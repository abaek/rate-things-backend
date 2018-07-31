# Connect to the database.
import pymysql
conn = pymysql.connect(
    db='example',
    user='root',
    passwd='hello123',
    host='localhost')
c = conn.cursor()

# Insert some example data.
c.execute("INSERT INTO movies VALUES ('Game Night', 10)")
conn.commit()

