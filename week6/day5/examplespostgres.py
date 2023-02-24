import psycopg2
import psycopg2.extras
import fake2db


from secrets import host, user, password

database = "day6"

connect = psycopg2.connect(host=host, database=database, user=user, password=password)

if connect.closed == 0:
    print("Connection is open")
else:
    print("Connection is closed")


# Create a fake2db object
f = fake2db.Fake2db()

# Populate a postgres database "day6" with 100 rows of data
f.populate_db("postgres", "day6", 100)

connect.close()
