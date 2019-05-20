import mysql.connector

db = mysql.connector.connect(option_files="my.cnf", use_pure=True)  # use_pure means use pure python, no c extension
cursor = db.cursor()

# Create a temporary table for this example
cursor.execute("""
    CREATE TEMPORARY TABLE world.t1 (
        id int unsigned NOT NULL,
        val varchar(10),
        PRIMARY KEY(id)
    )""")


# Define the query template and the parameters to submit with it.
sql = """
INSERT INTO world.t1 VALUES (%s,%s)
"""

params = (
    (1,"abc"),
    (2,"edf"),
    (3,"dff")
)

# Get the previous number of questions asked to mysql by the session
cursor.execute("""
    SELECT VARIABLE_VALUE
    FROM performance_schema.session_status
    WHERE VARIABLE_NAME = 'questions'"""
)
tmp = cursor.fetchone()
question_before = int(tmp[0])

# Execute the queries
cursor.executemany(sql, params)
print("Row count: {0}".format(cursor.rowcount))
print("Last statement: {0}".format(cursor.statement))

# Get the previous number of questions asked to mysql by the session
cursor.execute("""
    SELECT VARIABLE_VALUE
    FROM performance_schema.session_status
    WHERE VARIABLE_NAME = 'questions'"""
)
tmp = cursor.fetchone()
question_after = int(tmp[0])

print("Difference in number of" 
+ " questions: {0}".format(question_after-question_before))

cursor.close()
db.close()
