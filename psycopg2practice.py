import psycopg2
connection = psycopg2.connect("dbname=learning_sql user=dbperson")

cursor = connection.cursor()
#cursor.execute("select * from person_data;")
cursor.execute("DROP TABLE IF EXISTS person_data;") - this process simialr
to the "w" w/ csv removes the data then recreate
## this is the migration.py
 ### create scaffolding as
#  template so anyone can run the migration
    ####DO THIS
###close the cursor and connection as soon as opened and put code in
#between =>=>=> heres scaffolding
table_create_command = """CREATE TABLE person_data (
paste table data from the platform then );"""
cursor.execute("INSERT INTO person_data VALUES "('Joel Taddei', )")
### this is called FIXTURE DATA
#run program should give no results
***CURSOR.EXECUTE(TABLE_CREATE_COMMAND) - DO NOT USE .FORMAT
 "INSERT INTO PER_DATA VALUES ( %s, %s %s);", (NAME, BESTIE, AGE YEAR)
()



cursor.execute
connection.commit()
cursor.close()
connection.close()

### use 8 players create table
### LAND MINE - SQL INJECTIONS - VIA WEB HACKERS CAN DESTROY YOUR DATA
see *** above