import mysql.connector
from mysql.connector.errors import PoolError

# Create a pool and return the first connection
db1 = mysql.connector.connect(
    option_files="my.cnf",
    pool_size=2,
    pool_name="test",
)

# Get a second conection in the same pool
db2 = mysql.connector.connect(pool_name="test")

print("Connection IDs\n")
print("db1  db2")
print("-"*15)
print("{0:3d}   {1:3d}".format(
    db1.connection_id,
    db2.connection_id
))

db1.close()
db2.close()