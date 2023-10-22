def register(users):
    while True:
        username = input("Enter a new username: ")
        password = input("Enter a password: ")

        if any(user.username == username for user in users):
            print("Username already exists. Please choose another username.")
        else:
            users.append(User(username, password))
            print("Registration successful!")
            break

def login(users):
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        for user in users:
            if user.username == username and user.password == password:
                print("Login successful!")
                return user

        print("Invalid username or password. Please try again.")


