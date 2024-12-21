from database.database import DatabaseManager
from menu.console_menu import Menu


def main() -> None:
    with DatabaseManager('history.sqlite3') as db:


        menu = Menu(db=db)
        menu.show_menu()


if __name__ == "__main__":
    main()
