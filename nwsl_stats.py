import psycopg2

connection = psycopg2.connect("dbname=womens_soccer user=Tootie")
cursor = connection.cursor()


def welcome():
    welcome = input("Welcome to the NWSL: Goalie Stats Database.\n"
                    "You can (S)earch or (A)dd a goalie to the database?").lower()
    if welcome == "s":
        search_data()
    if welcome == "a":
        add_data()


def search_data():
    search = input("Search by (P)layerName, (T)eamName, S(h)ots On Goal, Sa(v)es").lower()
    if search == "p":
        name_search()
    elif search == "t":
        team_search()
    elif search == "h":
        shots_on_goal_search()
    else:
        if search == "v":
            saves_search()
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


def shots_on_goal_search():
    cursor.execute("select PlayerName, ShotsOnGoal from goalie_stats order by ShotsOnGoal DESC ;")
    result = cursor.fetchall()
    print(result)
    search_data()


def saves_search():
    cursor.execute("select PlayerName, Saves from goalie_stats order by Saves DESC ;")
    result = cursor.fetchall()
    print(result)
    search_data()

def add_data():
    PlayerName = input("Enter the player's name: ")
    TeamName = input("Enter the team name, example, SEA: ")
    GamesPlayed = input("Enter the number of games played: ")
    Minutes = input("Enter the number of minutes played, example, 180: ")
    ShotsOnGoal = input("Enter the number of shots on goal: ")
    Saves = input("Enter the number of saves: ")
    GA = input("Enter the number of goals against: ")
    GAA = input("Enter the average number of goals against: ")
    SHO = input("Enter the number of shutouts: ")

    cursor.execute("INSERT INTO goalie_stats VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);",\
                   (PlayerName, TeamName, GamesPlayed, Minutes, ShotsOnGoal, Saves, GA, GAA, SHO))

    connection.commit()
    print("Your goalie data has been added to the database.")
    search_data()


welcome()

cursor.close()
connection.close()


