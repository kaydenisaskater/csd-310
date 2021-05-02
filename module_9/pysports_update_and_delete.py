#Kayden Linner
#05/02/2021
#Module 9.2

import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "pysports_user",
    "password": "MySQLTestingPython190!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

def show_players(cursor, title):
    """ inner join method and display results"""
    #inner join
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    #cursor results
    players = cursor.fetchall()

    print("\n  -- {} --".format(title))

    #loop through players
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))
        
try:
    """try catch block for error handling"""
    #database connection
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    #insert statement
    add_player = ("INSERT INTO player(first_name, last_name, team_id) VALUES(%s, %s, %s)")

    #values to input
    player_data = ("Smeagol", "Shire Folk", 1)

    #execute the insert statement/add_player
    cursor.execute(add_player, player_data)

    #commits the insert
    db.commit()

    #display new list
    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    #update statement
    update_player = ("UPDATE player SEt team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    #execute the update statement
    cursor.execute(update_player)
    
    #display new list
    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    #delete statement
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")

    #execute delete statement
    cursor.execute(delete_player)

    #show final list
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

except mysql.connector.Error as err:
    """ on error code """
    
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database doesn't exist")
    
    else:
        print(err)

finally:
    """ close the connection to MySQL """
    db.close()