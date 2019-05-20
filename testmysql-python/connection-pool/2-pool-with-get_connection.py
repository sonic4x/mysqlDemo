from mysql.connector import pooling
from mysql.connector import errors

pool = pooling.MySQLConnectionPool(
    option_files = "my_usedinpool.cnf",  # Here the password must be a string
    pool_name="test",
    pool_size=2 # default is 5
)

db = pool.get_connection()
db2 = pool.get_connection()
try:
    db3 = pool.get_connection()
except errors.PoolError as err:
    print("Unable to fetch connection: {0}".format(err))
else:
    print("get_connection successfully")

db2.close()

try:
    db3 = pool.get_connection()
except errors.PoolError as err:
    print("Unable to fetch connection: {0}".format(err))
else:
    print("get_connection successfully")

cursor = db.cursor( named_tuple = True)
cursor.execute("""
SELECT Name, CountryCode, Population
FROM world.city
WHERE CountryCode = %s LIMIT 3""", ("AUS",))

if (cursor.with_rows):
    print("{0:15s}  {1:7s}  {2:10s}".format(
        "City","Country", "Population"
    ))
    city = cursor.fetchone()
    while city:
        print("{0:15s}  {1:^7s}  {2:8d}".format(
            city.Name,
            city.CountryCode,
            city.Population
        ))
        city = cursor.fetchone()

cursor.close()
db.close()
