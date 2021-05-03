/*
Kayden Linner
05/02/2021
Module 10.3
*/

-- drop whatabook_user if they already exist
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- now create whatabook_user
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- whatabook_user gets all privileges
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';

-- remove foreign keys
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop the tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

-- create tables

CREATE TABLE store (
    store_id    INT    NOT NULL    AUTO_INCREMENT,
    locale    VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id    INT    NOT NULL    AUTO_INCREMENT,
    book_name    VARCHAR(200)    NOT NULL,
    author    VARCHAR(200)    NOT NULL,
    details    VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id    INT    NOT NULL    AUTO_INCREMENT,
    first_name    VARCHAR(75)    NOT NULL,
    last_name    VARCHAR(75)    NOT NULL,
    PRIMARY KEY(user_id)
);

CREATE TABLE wishlist (
    wishlist_id    INT    NOT NULL    AUTO_INCREMENT,
    user_id    INT    NOT NULL,
    book_id    INT    NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY(book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_id)
);

-- insert store
INSERT INTO store(locale)
    VALUES('2407 West 24th Street, Kearney, NE 68845');

-- insert book
INSERT INTO book(book_name, author)
    VALUES('The Push', 'Ashley Audrain');

INSERT INTO book(book_name, author)
    VALUES('A Crooked Tree', 'Una Mannion');
    
INSERT INTO book(book_name, author)
    VALUES('Let Me Tell You What I Mean', 'Joan Didion');

INSERT INTO book(book_name, author)
    VALUES('The Wife Upstairs', 'Rachel Hawkins');

INSERT INTO book(book_name, author)
    VALUES('Summerwater', 'Sarah Moss');

INSERT INTO book(book_name, author)
    VALUES('How the One-Armed Sister Sweeps Her House', 'Cherie Joines');

INSERT INTO book(book_name, author)
    VALUES('Life Amount the Terranauts', 'Caitlin Horrocks');

INSERT INTO book(book_name, author)
    VALUES('The Removed', 'Brandon Hobson');

INSERT INTO book(book_name, author)
    VALUES('Girl A', 'Abigail Dean');

-- insert users
INSERT INTO user(first_name, last_name)
    VALUES('Jon', 'Snow');

INSERT INTO user(first_name, last_name)
    VALUES('Brian', "O'Conner");

INSERT INTO user(first_name, last_name)
    VALUES('Bill', 'Gates');

-- insert wishlists
INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Jon'),
        (SELECT book_id FROM book WHERE book_name = 'The Removed')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Brian'),
        (SELECT book_id FROM book WHERE book_name = 'Girl A')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Bill'),
        (SELECT book_id FROM book WHERE book_name = 'Summerwater')
    );
