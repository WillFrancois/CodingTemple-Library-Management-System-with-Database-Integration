# Library Management System

# This code is not suitable for production due to a hard-coded password and root access by default. This is only test code for the Coding Temple assignment "Library Management System with Database Integration".

## How to Run
To run this program, install python on your machine and ensure you are able to run it in your terminal/command line. Navigate to the root of this project and run the main.py file.

## Features
### User creation and display:
Users of this program will be able to add library users and display the information needed to connect books to the library users' accounts.
### Book creation and borrowing:
Users of this program will be able to create, borrow, and link borrowed books to users with existing library IDs. Book borrowing is still functional without a library ID, but that book cannot be linked to a user until it is returned.
### Author creation and display:
Users of this program will be able to add authors and display their optional biographies.

## Usage with MySQL
MySQL should be running on its default port (3306) and the password for the root should be set to "my-secret-pw", which is the default set-up for the docker container version that was used to bugfix this application. This will allow the database to make the necessary changes to the correct tables.

## Contributing
Each piece of functionality (adding users, adding authors, listing books) is in its own function. The BookInfo folder holds all files related to book information (Books and Authors). All other files are located in the root directory. All menu functionality is located in the MenuUI file.

Database handling is all processed by the DBManager class in DB_Manager.py. This class handles database errors as well as well as handles general query behavior. run_std_query runs a query that does not expect a return value while run_return_query keeps the cursor alive for the developer to get data back from the database.
