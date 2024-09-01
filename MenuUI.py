import User
from BookInfo import Book
from BookInfo import Author

class MenuUI:
    __main_menu_str = "Welcome to the Library Management System!\n\nMain Menu:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit\n\n"
    __book_menu_str = "Book Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books\n6. Quit\n\n"
    __user_menu_str = "User Operations:\n1. Add a new user\n2. View user details\n3. Display all users\n4. Quit\n\n"
    __author_menu_str = "Author Operations:\n1. Add a new author\n2. View author details\n3. Display all authors\n4. Quit\n\n"

    def __init__(self, db):

        self.db = db

        while True:
            menu_inp = input(self.get_main_menu_str())
            try:
                menu_inp = int(menu_inp)
                print()
            except Exception:
                print("Improper input! Please try again!\n")
                print()
                continue

            match menu_inp:
                case 1:
                    self.book_menu(self.db)
                    continue
                case 2:
                    self.user_menu(self.db)
                    continue
                case 3:
                    self.author_menu(self.db)
                    continue
                case 4:
                    exit()
                case _:
                    print("Invalid number input. Please try again!\n")
                    continue

    def book_menu(self, db):
        while True:
            menu_inp = input(self.get_book_menu_str())
            try:
                menu_inp = int(menu_inp)
                print()
            except Exception:
                print("Improper input! Please try again!\n")
                print()
                continue

            match menu_inp:
                case 1:
                    Book.create_book(db)
                    continue
                case 2:
                    Book.borrow_book(db)
                    continue
                case 3:
                    Book.return_book(db)
                    continue
                case 4:
                    Book.search_books(db)
                    continue
                case 5:
                    Book.display_all_books(db)
                    continue
                case 6:
                    return
                case _:
                    print("Invalid number input. Please try again!\n")
                    continue

    def user_menu(self, db):
        while True:
            menu_inp = input(self.get_user_menu_str())
            try:
                menu_inp = int(menu_inp)
                print()
            except Exception:
                print("Improper input! Please try again!\n")
                print()
                continue

            match menu_inp:
                case 1:
                    User.add_user(db)
                    continue
                case 2:
                    User.user_details(db)
                    continue
                case 3:
                    User.display_users(db)
                    continue
                case 4:
                    return
                case _:
                    print("Invalid number input. Please try again!\n")
                    continue

    def author_menu(self, db):
        while True:
            menu_inp = input(self.get_author_menu_str())
            try:
                menu_inp = int(menu_inp)
                print()
            except Exception:
                print("Improper input! Please try again!\n")
                print()
                continue

            match menu_inp:
                case 1:
                    Author.create_author(db)
                    continue
                case 2:
                    Author.detail_author(db)
                    continue
                case 3:
                    Author.display_authors(db)
                    continue
                case 4:
                    return
                case _:
                    print("Invalid number input. Please try again!\n")
                    continue

    def get_main_menu_str(self):
        return self.__main_menu_str

    def get_book_menu_str(self):
        return self.__book_menu_str

    def get_user_menu_str(self):
        return self.__user_menu_str

    def get_author_menu_str(self):
        return self.__author_menu_str
