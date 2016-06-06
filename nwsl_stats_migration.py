import psycopg2
connection = psycopg2.connect("dbname=womens_soccer user=Tootie")

cursor = connection.cursor()
cursor.execute("DROP TABLE if exists goalie_stats;")


table_create_command = """CREATE TABLE goalie_stats (
    PlayerName varchar(30),
    TeamName varchar(30),
    GamesPlayed FLOAT (3),
    MinutesPlayed FLOAT (4),
  ShotsonGoal FLOAT (3),
  Saves FLOAT (3),
  GA FLOAT (3),
  GAA FLOAT (6),
  SHO FLOAT (2)
  );"""

cursor.execute(table_create_command)

# for row in results:
#    PlayerName = ()
#    print(row[0])
#    TeamName = ()
#    print(row[1])
#    GamesPlayed = ()
#    print(row[2])
#    Minutes = ()
#    print(row[3])
#    ShotsOnGoal = ()
#    print(row[4])
#    Saves = ()
#    print(row[5])
#    GA = ()
#    print(row[6])
#    GAA = ()
#    print(row[7])
#    SHO = ()
#    print(row[8])

#cursor.execute("INSERT INTO goalie_stats VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s,);",
#                   (PlayerName, TeamName, GamesPlayed, Minutes, ShotsOnGoal, Saves, GA, GAA, SHO))

cursor.execute("INSERT INTO goalie_stats VALUES"
               "('Michele Dalton', 'CHI', 12, 1080, 113, 47, 11, 0.917, 5),"
               "('Nicole Barnhart', 'KC', 17, 1530, 179, 54, 16, 0.941, 8),"
               "('Haley Kopmeyer', 'SEA', 11, 990, 107, 41, 11, 1.000, 4),"
               "('Caroline Stanley', 'SEA', 1, 90, 6, 1, 1, 1.000, 0),"
               "('Hope Solo', 'SEA', 8, 720, 56, 19, 9, 1.125, 1),"
               "('Bianca Hanninger', 'HOU', 10, 868, 132, 34, 11, 1.141, 4),"
               "('Michelle Belos', 'POR', 14, 1260, 130, 45, 18, 1.266, 2),"
               "('Ashlyn Harris', 'WAS', 9, 810, 126, 47, 12, 1.333, 1),"
               "('Katelyn Rowland', 'KC', 3, 270, 29, 13, 4, 1.333, 1),"
               "('Brittany Cameron', 'NJ', 20, 1792, 263, 87, 27, 1.356, 4);")

connection.commit()

cursor.execute(" SELECT * FROM goalie_stats")
results = cursor.fetchall()
for row in results:
    print(row)


cursor.close()
connection.close()
