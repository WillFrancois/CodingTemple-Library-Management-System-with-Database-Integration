import MenuUI
import DB_Manager

def main():
    db = DB_Manager.DBManager("root", "my-secret-pw", "localhost", "Library_Management_System")
    ui = MenuUI.MenuUI(db)

if __name__ == "__main__":
    main()
