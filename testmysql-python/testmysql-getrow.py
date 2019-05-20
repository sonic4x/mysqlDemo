import mysql.connector
import pprint
from mysql.connector.conversion import MySQLConverter

printer = pprint.PrettyPrinter(indent=1)


db = mysql.connector.connect(option_files="my.cnf", use_pure=True)
print(__file__+ " - single config file:")
print("MySQL connection ID of db: {0}".format(db.connection_id))

# if "can-consume-results" is false, you have to read all the rows before next query
print("MySQL connection property \"can-consume-results\": {0}".format(db.can_consume_results))

"""
Simple execution:  cmd_query, get_row
"""
# Execute a query
result = db.cmd_query(
    """select name, countrycode, population
        from world.city
        where population > 900000
        order by population desc"""
)

# Print the result dict
print("Result Dictionary\n" + "="*17)
printer.pprint(result)

converter = MySQLConverter(db.charset, True)  # Unicode is True
print(__file__ + " - Using get_row:")
print("")
print("{0:25s}    {1:7s}    {2:3s}".format("City","Country","Pop") )

(city, eof) = db.get_row()
while(not eof): #eof is none while there are more rows to read.
    values = converter.row_to_python(city, result["columns"])
    print(
        "{0:25s}    {1:^7s}    {2:4.1f}".format(
        values[0],
        values[1],
        values[2]/1000000.0
        )
    )
    (city,eof) = db.get_row()


db.close()