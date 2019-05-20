import mysql.connector
import datetime

db = mysql.connector.connect(option_files="my.cnf", use_pure=False)

# if "can-consume-results" is false, you have to read all the rows before next query
print("MySQL connection property \"can-consume-results\": {0}".format(db.can_consume_results))

cursor = db.cursor()

# Create temporary table
sql = """
create temporary table world.tmp_person(
    name varchar(50) not null,
    birthday date not null,
    PRIMARY KEY (name)
)"""
cursor.execute(sql)

sql = """
insert into world.tmp_person
values(%s,%s)
"""
params = ("John Doe", datetime.date(1970,10,31))            # tuple

cursor.execute(sql, params=params)

print("statement:\n {0}".format(cursor.statement))

"""
way 2 to param ( more readable and verbose)
"""
# input = "'Sydney' or True"
# sql = """select * from world.city where name=%(name)s"""   
# params = {'name':input}                                   # Dict
# cursor.execute(sql, params=params)
# cursor.fetchall()


cursor.close()
db.close()

