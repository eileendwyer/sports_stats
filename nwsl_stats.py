import psycopg2

connection = psycopg2.connect("dbname=womens_soccer user=Tootie")
cursor = connection.cursor()


def welcome():
    welcome = input("Welcome to the NWSL: Goalie Stats Database.\n"
                    "You can (S)earch or (A)dd a goalie to the database?").lower()
    if welcome == "s":
        search_data()
#    else:
#        add_data()


def search_data():
    search = input("Search by (P)layerName | (T)eamName | S(h)ots on Goal | S(a)ves").lower()
    if search == "p":
        name_search()
    elif search == "t":
        team_search()
    elif search == "h":
        shotsgoal_search()
    elif search == "a":
        saves_search()
    else:
        print("Incorrect search entry.")
        search_data()


def name_search():
    search = input("Enter a goalie name to search: ")
    cursor.execute("select * from goalie_stats where PlayerName = %s;", (search, ))
    result = cursor.fetchall()
    print(result)
    search_data()


def team_search():
    search = input("Enter a team name to search, eg. SEA: ")
    cursor.execute("select * from goalie_stats where TeamName = %s;", (search, ))
    result = cursor.fetchall()
    print(result)
    search_data()


def shotsgoal_search():
    cursor.execute("select PlayeName, ShotsonGoals from goalie_stats order by ShotsonGoal DESC ;")
    result = cursor.fetchall()
    print(result)
    search_data()


def saves_search():
    cursor.execute("select PlayerName, Saves from goalie_stats order by Saves DESC ;")
    result = cursor.fetchall()
    print(result)
    search_data()


welcome()


