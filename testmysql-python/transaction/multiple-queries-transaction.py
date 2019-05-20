import mysql.connector

db = mysql.connector.connect(option_files="my.cnf", autocommit=True)

cursor = db1.cursor(dictionary=True)

queries=[
    """
    update world.city
    set population = population + 1
    where id = 130
    """,
    """
    update world.country
    set population = population + 1
    where code = 'AUS'
    """,
]

# Start a transaction
db.start_transaction()

tests = cursor.execute(
    ";".join(queries), multi=True
)

for test in tests:
    pass

db.rollback()

cursor.close()
db.close()

