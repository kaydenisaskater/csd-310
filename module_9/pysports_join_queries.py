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

try:
    """try catch block for error handling"""
    #database connection
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    #inner join statement
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    #cursor results
    players = cursor.fetchall()

    print("\n  -- DISPAYING PLAYER RECORDS --")

    #loop through players
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key to continue... ")

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