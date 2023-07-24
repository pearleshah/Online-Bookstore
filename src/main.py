# Pearle Shah
# July 23, 2023

# main.py

from bookstore import Bookstore

def main():

    # Create instance
    bookstore = Bookstore()

    flag = True     # To break out of bookstore if user wants to exit

    print("\nWelcome to the bookstore!\n")

    # Keep prompting user to interact with bookstore until they choose to exit
    while flag:

        # Print options for user to select from 
        print("1) Add Book")
        print("2) Remove Books")
        print("3) Search Books")
        print("4) List Books")
        print("5) Exit Bookstore")

        choice = input("\nPick Your Choice (1-5): " + "\n")

        # Adding New Books
        if choice == "1":

            # ISBN Entry 
            # Should be numeric and only 13 digits long
            while True:
                try:
                    isbn = (input("Enter ISBN-13: "))
                    if ((len(str(isbn)) != 13) or (not(isbn.isnumeric()))):
                        raise ValueError
                except ValueError:
                    print("\nInvalid ISBN-13 entered. ISBN-13 numbers must be 13 digits long and all characters must be numeric. Please try again.\n")
                else:
                    break

            # Title Entry 
            # User should enter a string more than 0 characters long 
            while True:
                try:
                    title = str(input("Enter Title: "))
                    if (len(str(title)) == 0):
                        raise ValueError
                except ValueError:
                    print("\nPlease enter a valid book title.\n")
                else:
                    break
            
            # Author Entry
            # User should enter a string more than 0 characters long 
            while True:
                try:
                    author = str(input("Enter Author: "))
                    if (len(str(author)) == 0):
                        raise ValueError
                except ValueError:
                    print("\nPlease enter a valid author name.\n")
                else:
                    break

            # Publisher Entry
            # User should enter a string more than 0 characters long 
            while True:
                try:
                    publisher = str(input("Enter Publisher: "))
                    if (len(str(publisher)) == 0):
                        raise ValueError
                except ValueError:
                    print("\nPlease enter a valid publisher name.\n")
                else:
                    break

            # Publication Year Entry
            # Entry should be numeric and exactly 4 digits long
            while True:
                try:
                    publicationYear = (input("Enter Year of Publication (4 digits): "))
                    if (not(publicationYear.isnumeric()) or (not(len(str(publicationYear)) == 4))):
                        raise ValueError
                except ValueError:
                    print("\nPlease enter valid Year of Publication.\n")
                else:
                    break

            # Quantity of Books in Stock Entry
            # Entry should be 0 or more and numeric
            while True:
                try:
                    quantity = (input("Enter Quantity in Stock: "))
                    if ((not(quantity.isnumeric())) or (int(quantity) < 0)):
                        raise ValueError
                except ValueError:
                    print("\nPlease enter valid quanitity in stock.\n")
                else:
                    break

            # Call function to add book with based on user inputs
            book_data = [isbn, title, author, publisher, publicationYear, quantity]
            bookstore.addBook(book_data)

            # Print success message
            print("\nBook was added successfully to the bookstore!\n")

        # Removing Books
        elif choice == "2":
            isbn = input("\nEnter ISBN of book to remove: ")
            bookstore.removeBook(isbn)

        # Searching for Books
        # Allow user to select how they want to search for a book. Must be exact match for results to pop up.
        elif choice == "3":
            keyword = input("\nPick a number to select a keyword to search by: \n 1) ISBN \n 2) Title \n 3) Author\n")
            if keyword == "1":
                isbn = input("\nEnter ISBN of book to search for: ")
                bookstore.searchBooks(keyword, isbn)

            elif keyword == "2":
                title = input("\nEnter title of book to search for: ")
                bookstore.searchBooks(keyword, title)

            elif keyword == "3":
                author = input("\nEnter author of book to search for: ")
                bookstore.searchBooks(keyword, author)

        # Listing All Books in Bookstore
        elif choice == "4":
            bookstore.listBooks()

        # Exiting the Bookstore
        elif choice == "5":
            print("\nThank you. Exiting bookstore...\n")
            flag = False

        # Invalid Input Error Message
        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
