import User
import datetime

def create_book(db):
    title = input("What is the title of this book?: ")
    author = input("What is the author ID of this book's writer?: ")
    genre = input("What is the genre of this book?: ")
    publication_date = input("What is the publication date of this book?: ")
    isbn = input("What is the ISBN number of this book?: ")

    db.run_std_query("insert into books(title, author_id, isbn, publication_date) values(%s, %s, %s, %s)", [title, author, isbn, publication_date])
    print()

def borrow_book(db):
    book_to_borrow = input("Which book would you like to borrow?: ")
    borrowing_user = input("Who is the user who will be borrowing?: ")

    db.run_std_query("update books set availability = 0 where title = %s", [book_to_borrow], False)
    try:
        data = db.run_return_query("select id from books where title = %s", [book_to_borrow], "Could not find book!")
        id = data.fetchone()[0]
        db.conn.commit()
        data.close()

        usr_data = db.run_return_query("select id from users where name = %s", [borrowing_user], "Could not find user!")
        usr_id = usr_data.fetchone()[0]
        db.conn.commit()
        usr_data.close()

        db.run_std_query("insert into borrowed_books(user_id, book_id, borrow_date) values (%s, %s, %s)", [usr_id, id, datetime.datetime.now().strftime("%Y-%m-%d")])
    except Exception as e:
        print("Could not borrow book!")
        print(e)


def return_book(db):
    book_to_return = input("Which book would you like to return?: ")

    db.run_std_query("update books set availability = 1 where title = %s", [book_to_return], False)
    data = db.run_return_query("select id from books where title = %s", [book_to_return], "Could not find book!")
    try:
        id = data.fetchone()[0]
        db.run_std_query("delete from borrowed_books where book_id = %s", [id])
    except Exception as e:
        print("Could not return book!")
    finally:
        db.conn.commit()
        data.close()

def search_books(db):
    book_search = input("Which book would you like to search for?: ")
    print()

    book_list = db.run_return_query("select * from books inner join authors where authors.id = books.author_id and title = %s", [book_search], "Could not find book from the database.")
    book_query_return = book_list.fetchall()

    for book in book_query_return:
        id, title, author_id, isbn, publication_date, availability, _, author_name, _ = book
        print("Title: " + title)
        print("Author: " + author_name)
        print("Publication Date: " + str(publication_date))
        print("ISBN: " + str(isbn))
        print("Available: " + ("Yes" if availability == 1 else "No"))

        print()

    if len(book_query_return) == 0:
        print("Invalid book name!")

    db.conn.commit()
    book_list.close()
    print()

def display_all_books(db):
    book_list = db.run_return_query("select * from books inner join authors where authors.id = books.author_id", [], "Could not find books from the database.")

    for book in book_list.fetchall():
        id, title, author_id, isbn, publication_date, availability, _, author_name, _ = book
        print("Title: " + title)
        print("Author: " + author_name)
        print("Publication Date: " + str(publication_date))
        print("ISBN: " + str(isbn))
        print("Available: " + ("Yes" if availability == 1 else "No"))
        print()

    db.conn.commit()
    book_list.close()
    print()
