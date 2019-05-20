import mysql.connector
import pprint
from mysql.connector.conversion import MySQLConverter

printer = pprint.PrettyPrinter(indent=0)

# connection way 1
# connect_args = {
#     "host":"127.0.0.1",
#     "port":3306,
#     "user":"root",
#     "password":"123456"
# }

# db1 = mysql.connector.connect(**connect_args)

# connection way 2
db = mysql.connector.connect(option_files="my.cnf", use_pure=True)
print(__file__+ " - single config file:")
print("MySQL connection ID of db1: {0}".format(db.connection_id))

"""
Simple execution:  cmd_query, get_rows, get_row
"""
# Execute a query
result = db.cmd_query(
    """select name, countrycode, population
        from world.city
        where population > 900000
        order by population desc"""
)
print(result )
# Fetch the rows
(cities,eof) = db.get_rows()

# Print the result dict
#print("Result Dictionary\n" + "="*17)
#printer.pprint(result)

# Print human readable rows way 1:
# print(__file__ + " - Using decode:")
# print("")
# print("{0:25s}    {1:7s}    {2:3s}".format("City","Country","Pop") )
# for city in cities:
#     print(
#         "{0:25s}    {1:^7s}    {2:4.1f}".format(
#         city[0].decode(db.python_charset),
#         city[1].decode(db.python_charset),
#         int(city[2].decode(db.python_charset))/1000000.0
#         )
#     )

# Print human readable rows way 2: use converter
converter = MySQLConverter(db.charset, True)  # Unicode is True
print(__file__ + " - Using converter:")
print("")
print("{0:25s}    {1:7s}    {2:3s}".format("City","Country","Pop") )
for city in cities:
    values = converter.row_to_python(city, result["columns"])
    print(
        "{0:25s}    {1:^7s}    {2:4.1f}".format(
        values[0],
        values[1],
        values[2]/1000000.0
        )
    )

print("\nEnd-of-file:")
for key in eof:
    print("{0:15s} = {1:2d}".format(key,eof[key]))


db.close()