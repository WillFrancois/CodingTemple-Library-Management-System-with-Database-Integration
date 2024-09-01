import random

def add_user(db):
    name = input("User's name?: ")
    library_id = input ("Library id for this user's library?: ")
    print()
    db.run_std_query("insert into users(name, library_id) values(%s, %s)", [name, library_id])

def user_details(db):
    usr_name = input("Which user would you like the details of?: ")
    print()

    user_list = db.run_return_query("select * from users where name = %s", [usr_name], "Could not find users from the database.")

    for user in user_list:
        _, name, lib_id = user
        print("Name: " + name)
        print("Library ID: " + lib_id)
        print()
        return
    print("No user with that id was found!")
    print()

    db.conn.commit()
    user_list.close()

def display_users(db):
    users_list = db.run_return_query("select * from users", [], "Could not find users from the database.")

    for user in users_list.fetchall():
        id, name, lib_id = user
        print("ID: " + str(id))
        print("Name: " + str(name))
        print("Library ID: " + str(lib_id))
        print()

    db.conn.commit()
    users_list.close()
