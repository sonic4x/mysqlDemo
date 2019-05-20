import mysql.connector

db = mysql.connector.connect(option_files="my.cnf", use_pure=True)  # use_pure means use pure python, no c extension
cursor = db.cursor()

# Define the query template and the parameters to submit with it.
sql = """
UPDATE world.city
SET population = %(population)s
WHERE name = %(name)s
AND countrycode = %(country)s
AND district = %(district)s
"""

params = (
    {
        "name":"Dimitrovgrad",
        "country":"RUS",
        "district":"Uljanovsk",
        "population":150000
    },
    {
        "name":"Lower Hutt",
        "country":"NZL",
        "district":"Wellington",
        "population":100000
    },
    {
        "name":"Wuhan",
        "country":"CHN",
        "district":"Hubei",
        "population":5000000
    },
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

db.rollback()
cursor.close()
db.close()
