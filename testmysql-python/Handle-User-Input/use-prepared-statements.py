import mysql.connector

# Format strings
FMT_QUERY = "Query {0}:\n" + "-"*8
FMT_HEADER = "{0:18s}   {1:7s}  {2:3s}"
FMT_ROW = "{0:18s}   {1:^7s}  {2:4.1f}"

# Define the queries
SQL = """
select name, countrycode, population
from world.city
where countrycode = %s
order by population DESC
limit 3
"""

db = mysql.connector.connect(option_files="my.cnf", use_pure=True)

cursor = db.cursor(prepared=True)

# Execute the query finding the top 3 populous cities in the USA and India
count = 0
for country in ("USA", "IND"):
    count = count + 1
    print(FMT_QUERY.format(count))

    cursor.execute(SQL, (country,))
    if (cursor.with_rows):
        print(FMT_HEADER.format("City","Country","Pop"))
        city = cursor.fetchone()
        while city:
            print(FMT_ROW.format(city[0],city[1],city[2]/1000000))
            city = cursor.fetchone()
    print("")
cursor.close()
db.close()
