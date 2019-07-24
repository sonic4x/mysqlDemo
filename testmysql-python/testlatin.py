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


sql = """
insert into newdb.account (userName) values(%s)
"""
binaryName = '\x23\x99\x09\xFF\xA0'
print(type(binaryName))
binaryN = binaryName.encode('latin1')
print(type(binaryN), binaryN)
params = (('ab',),(binaryN,))
cursor.executemany(sql, params)

print("!!!")
# Execute a query
cursor.execute(
    """select userName
        from newdb.account
    """
)

print(__file__ + " - Using the default cursor:")
print("")
if (cursor.with_rows):
    print(cursor.column_names)
    print("{0:25s}".format("City") )
    res = cursor.fetchone()
    print(res)
    while (res):
        print(
            "{0:25s}".format(
                res.userName
            )
        )
        res = cursor.fetchone()

cursor.close()
db.close()