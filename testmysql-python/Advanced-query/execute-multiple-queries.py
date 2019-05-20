import mysql.connector

# Format strings
FMT_QUERY = "Query {0}:\n" + "-"*8
FMT_HEADER = "{0:18s}   {1:7s}  {2:3s}"
FMT_ROW = "{0:18s}   {1:^7s}  {2:4.1f}"

db = mysql.connector.connect(option_files="my.cnf")

# Define the queries
sql_select = """
select name, countrycode, population
from world.city
where countrycode = %s
order by population DESC
limit 3
"""

sql_do = "DO SLEEP(3)"

queries = [ sql_select, sql_do, sql_select]

# Execute the queries and obtain the iterator
# This way is error prone. Try use multiple single-query or use executemany()
cursor = db.cursor()
results = cursor.execute(
    ";".join(queries),
    params=("USA","IND"),
    multi = True
)

count = 0
for result in results:
    count = count + 1
    print(FMT_QUERY.format(count))
    if (result.with_rows):
        print(FMT_HEADER.format("City","Country","Pop"))
        city = cursor.fetchone()
        while city:
            print(FMT_ROW.format(city[0],city[1],city[2]/1000000))
            city = cursor.fetchone()
    else:
        # Not a select statement
        print("No result to print")
    print("")

cursor.close()
db.close()
