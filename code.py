class Book:
    def __init__(self, title, author, available_copies):
        self.title = title
        self.author = author
        self.available_copies = available_copies

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Available Copies: {book.available_copies}")

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


def main():
    users = [User("user1", "pass1"), User("user2", "pass2")]
    logged_in_user = None

    while True:
        if logged_in_user is None:
            print("\nLibrary Management System")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                register(users)
            elif choice == '2':
                logged_in_user = login(users)
            elif choice == '3':
                print("Goodbye!")
                break
        else:
            print(f"\nWelcome, {logged_in_user.username}!")
            print("1. Add Book")
            print("2. Display Books")
            print("3. Logout")
            choice = input("Enter your choice: ")

            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter author: ")
                available_copies = int(input("Enter available copies: "))
                book = Book(title, author, available_copies)
                library.add_book(book)
                print("Book added successfully!")

            elif choice == '2':
                library.display_books()

            elif choice == '3':
                logged_in_user = None

if __name__ == "__main__":
    library = Library()
    main()
    
    