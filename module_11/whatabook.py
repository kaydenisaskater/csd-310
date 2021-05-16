#Kayden Linner
#5/8/2021
#Module 11.2

import sys
import mysql.connector
from mysql.connector import errorcode

"""database config object"""
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

"""methods"""
def main_menu():
    print("\n  -- Main Menu --")

    print("  - 1. View Books")
    print("  - 2. View Store Locations")
    print("  - 3. View Account")
    print("  - 4. Quit")

    try:
        userInput = int(input("\n  Enter in an option: "))

        return userInput
    except:
        main_menu()

def view_books(_cursor):
    _cursor.execute("SELECT book_id, book_name, author, details from book")

    books = _cursor.fetchall()

    print("\n  -- Book Listing --")

    for book in books:
        print("  - BookName: {}\n  - Author: {}\n  - Details: {}\n".format(book[0], book[1], book[2]))

def view_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")

    allLocations = _cursor.fetchall()

    print("\n  -- All Store Locations --")

    for location in allLocations:
        print("  - Store Address: {}\n".format(location[1]))

def try_user():
    """verify that user is in database"""
    try: 
        userID = int(input("\n  Enter in your customer id: "))

        if userID < 0 or userID > 3:
            try_user()

        return userID
    except:
        """catch error"""
        main_menu()

def account_menu():
    """main menu for account"""

    try:
        print("\n  -- Account Menu --")
        print("  - 1. Wishlist")
        print("  - 2. Add Book")
        print("  - 3. Main Menu")
        accountMenuInput = int(input("\n  Enter in an option: "))

        if (accountMenuInput == 1, 2, 3):
            return accountMenuInput
        else:
            account_menu()
    except:
        account_menu()

def wishlist(_cursor, _userID):
    """get a specific user's wishlist"""
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " +
                    "FROM wishlist " +
                    "INNER JOIN user ON wishlist.user_id = user.user_id " +
                    "INNER JOIN book ON wishlist.book_id = book.book_id " +
                    "WHERE user.user_id = {}".format(_userID))

    wishlist = _cursor.fetchall()

    print("\n  -- Wishlisted Items --")

    for book in wishlist:
        print("  Book Name: {}\n  Author: {}\n".format(book[4], book[5]))

def add_book(_cursor, _userID):
    """check what books are in the wishlist already, show which books can be added to the wishlist"""
    query = ("SELECT book_id, book_name, author, details " 
            "FROM book " 
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_userID))

    _cursor.execute(query)

    books_available_to_add = _cursor.fetchall()

    print("\n  -- Books Available For Wishlist --")

    for book in books_available_to_add:
        print("  Book ID: {}\n  Book Name: {}\n".format(book[0], book[1]))

def add_to_wishlist(_cursor, _userID, _book_id):
    """add a book to the wishlist"""
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_userID, _book_id))

"""try catch block"""
try:
    """try/catch for mysql errors"""

    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    print("  -- Welcome to WhatABook --")

    userInput = main_menu()

    while userInput != 4:
        if userInput == 1:
            view_books(cursor)

        if userInput == 2:
            view_locations(cursor)
        
        if userInput == 3:
            selected_User_ID = try_user()
            account_menu_selection = account_menu()

            while account_menu_selection != 3:
                if account_menu_selection == 1:
                    wishlist(cursor, selected_User_ID)
                
                if account_menu_selection == 2:
                    add_book(cursor, selected_User_ID)

                    book_id = int(input("\n  Enter in a book id to add it to your wishlist: "))

                    add_to_wishlist(cursor, selected_User_ID, book_id)

                    db.commit()

                    print("\n  Book id: {} was added to the wishlist.".format(book_id))

                if account_menu_selection < 0 or account_menu_selection > 3:
                    print("\n  Invalid entry, try again")

                accountMenu = account_menu()

                break
                

        if userInput < 0 or userInput > 4:
            print("\n  Invalid entry, try again.")

        userInput = main_menu()

    print("\n  Program closed.")

except mysql.connector.Error as err:
    """errors"""
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database doesn't exist")

    else:
        print(err)

finally:
    """Close mysql connection"""
    db.close()