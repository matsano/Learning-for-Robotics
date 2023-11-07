from database import DataBase


if __name__ == "__main__":
    db = DataBase()

    while True:
        print("\nOptions:")
        print("1. Add new user")
        print("2. Show all the users")
        print("3. Search user by name")
        print("4. Exit")

        option = input("Choose an option: ")

        if option == '1':
            db.add_new_user()
        elif option == '2':
            db.get_all_users()
        elif option == '3':
            db.get_user()
        elif option == '4':
            break
