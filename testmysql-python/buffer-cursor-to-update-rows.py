import mysql.connector
from math import ceil

SQL_UPDATE = """
    UPDATE world.city 
    SET population = %(new_population)s
    WHERE id = %(city_id)s"""

# Function to increase the population with 10%
def new_population(old_population):
    return int(ceil(old_population * 1.10))


db = mysql.connector.connect(option_files="my.cnf")

cursor1 = db.cursor(buffered=True, dictionary=True)
cursor2 = db.cursor()

# Execute the query to get the Australian cities
cursor1.execute(
    """SELECT ID, Population
        FROM world.city
        WHERE countrycode = %s""",
    params= ("AUS",)
)

city = cursor1.fetchone()

while (city):
    old_pop = city["Population"]
    new_pop = new_population(old_pop)
    print("ID, Old => New: " 
    + "{0}, {1} => {2}".format(
        city["ID"], old_pop, new_pop
    ))

    cursor2.execute(SQL_UPDATE, params={
        "city_id": city["ID"],
        "new_population": new_pop        
    })

    print("statement:{0}".format(cursor2.statement))
    city = cursor1.fetchone()

db.rollback()
db.close()