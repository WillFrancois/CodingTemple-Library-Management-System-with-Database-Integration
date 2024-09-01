import mysql.connector

class DBManager:

    def __init__(self, username, password, host, database):
        try:
            self.conn = mysql.connector.connect(user=username, password=password, host=host, database=database)

        except Exception as e:
            print("Could not connect to the database!")
            exit()

    def run_std_query(self, query, args, should_print=True):
        try:
            cursor = self.conn.cursor()
            data = cursor.execute(query, args)
            self.conn.commit()
            if should_print: print("Database updated successfully!")
            return data
        except Exception as e:
            print("Unable to run query in database!")
            print(e)
            return []
        finally:
            print()

    def run_return_query(self, query, args, error):
        cursor = self.conn.cursor()

        try:
            cursor.execute(query, args)
        except Exception as e:
            print(error)
            print(e)

        return cursor
