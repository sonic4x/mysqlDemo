import mysql.connector
import pprint
from mysql.connector.conversion import MySQLConverter

printer = pprint.PrettyPrinter(indent=1)


db = mysql.connector.connect(option_files="my.cnf", use_pure=True)
print(__file__+ " - single config file:")
print("MySQL connection ID of db: {0}".format(db.connection_id))

# if "can-consume-results" is false, you have to read all the rows before next query
print("MySQL connection property \"can-consume-results\": {0}".format(db.can_consume_results))

cursor = db.cursor(named_tuple=True)

# Execute a query
cursor.execute(
    """select name, countrycode, population
        from world.city
        where population > 900000
        order by population desc limit 3"""
)

print(__file__ + " - Using the default cursor:")
print("")
if (cursor.with_rows):
    print(cursor.column_names)
    print("{0:25s}    {1:7s}    {2:3s}".format("City","Country","Pop") )
    city = cursor.fetchone()
    #print(city)
    while (city):
        print(
            "{0:25s}    {1:^7s} {2:4.1f}".format(
                city.name,city.countrycode,city.population/1000000.0
            )
        )
        city = cursor.fetchone()



"""
user input
"""

print("Handle user input:\n" + '='*10)
input = "'Sydney' or True"
sql = """select * from world.city where name = {0}""".format(input)
cursor.execute(sql)
cursor.fetchall()
print("1: Statement: {0}".format(cursor.statement))
print("1: Row count:{0}\n".format(cursor.rowcount))

sql = """select * from world.city where name=%(name)s"""
params = {'name':input}
cursor.execute(sql, params=params)
cursor.fetchall()
print("2: Statement: {0}".format(cursor.statement))
print("2: Row count:{0}\n".format(cursor.rowcount))

cursor.close()
db.close()