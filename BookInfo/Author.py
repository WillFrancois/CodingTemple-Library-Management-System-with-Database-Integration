def create_author(db):
    name = input("Author name?: ")
    biography = input("Add a biography?: ")

    try:
        db.run_std_query("insert into authors(name, biography) values(%s, %s)", [name, biography])
        print("Author added successfully!")
    except Exception:
        print("Unable to add author!")
    finally:
        print()

def detail_author(db):
    name = input("Provide a name for the author you would like the details of: ")
    print()

    author_list = db.run_return_query("select * from authors where name = %s", [name], "Could not find authors from the database.")

    for author in author_list:
        _, name, bio = author
        print("Name: " + name)
        print("Biography: " + bio)
        print()
        return
    print("No author with that name was found!")
    print()

    db.conn.commit()
    author_list.close()

def display_authors(db):
    author_list = db.run_return_query("select * from authors", [], "Could not find authors from the database.")

    for author in author_list.fetchall():
        id, name, bio = author
        print("ID: " + str(id))
        print("Name: " + name)
        print("Biography: " + bio)
        print()

    db.conn.commit()
    author_list.close()
