# Pearle Shah
# July 23, 2023

# bookstore.py
import csv
import os
import pandas as pd
import sys

# Go one level up in directory/path
PARENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Create CSV inside a data folder
DATA_DIR = os.path.join(PARENT_DIR, "data")
CSV_FILE = os.path.join(DATA_DIR, "database.csv")
FIELDS = ["ISBN", "Title", "Author", "Publisher", "Year", "Quantity"]       # Header fields for CSV


# Bookstore Database Management 
class Bookstore:

    def __init__(self):
        # Check if the "data" directory exists, and create it if not
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        # Create file if the CSV file does not exist
        if not os.path.exists(CSV_FILE):
            with open(CSV_FILE, "w", newline="") as i:
                writer = csv.writer(i)
                writer.writerow(FIELDS)     # Add header fields

    # Adding Books to the Bookstore
    def addBook(self, book_data):
        isbn = book_data[0]
        df = pd.read_csv(CSV_FILE, index_col='ISBN', header=0)  # Specify header=0 to use the first row as column names

        if isbn in df.index:
            # Book with the same ISBN already exists, update its quantity
            existing_quantity = df.loc[isbn, 'Quantity']
            new_quantity = int(existing_quantity) + int(book_data[5])
            df.loc[isbn, 'Quantity'] = new_quantity

            # Save the changes to the CSV file without writing the index
            df.to_csv(CSV_FILE, index=False)
            print("\nBook quantity updated successfully!\n")
        else:
            # Book with the given ISBN is not present, add a new entry
            if int(book_data[5]) < 0:
                raise ValueError("Invalid quantity. Quantity must be a non-negative integer.")
            
            with open(CSV_FILE, "a", newline="") as i:
                writer = csv.writer(i)
                writer.writerow(book_data)
                print("\nBook was added successfully to the bookstore!\n")


    # Removing Books by ISBN
    def removeBook(self, isbn):
        try:
            isbn = int(isbn) 

        except ValueError:
            raise ValueError("Invalid ISBN format. Please enter a valid integer.")  # Error message to re-enter valid ISBN

        df = pd.read_csv(CSV_FILE, index_col='ISBN')

        # Remove all rows that have matching ISBN numbers
        if isbn in df.index:
            df = df.drop(isbn)
            df.to_csv(CSV_FILE, index=True)
            print('\nBook removed!\n')

        # Print error message if no books exact with that ISBN 
        else:
            print('\nBook with the given ISBN not found.\n')


    # Searching for Books by Specified Keyword
    def searchBooks(self, keyword, searchTerm):
        try:
            # Allow user to search by ISBN
            if keyword == "1":
                df = pd.read_csv(CSV_FILE, index_col='ISBN')
                isbn = int(searchTerm) 
                df2=df.query(f"ISBN == {isbn}")

                # Print all books found by that ISBN or print message saying none found
                if df2.empty:
                    print("\nNo books found by that ISBN. Please try again.\n")
                else:
                    print(df2)
                    print("\n")

            # Allow user to search by title
            elif keyword == "2":
                df = pd.read_csv(CSV_FILE, index_col='Title')
                title = searchTerm  
                df2=df.query(f"Title == {title}")

                # Print all books found by that title or print message saying none found
                if df2.empty:
                    print("\nNo books found by that title. Please try again.\n")
                else:
                    print(df2)
                    print("\n")

            # Allow user to search by author
            elif keyword == "3":
                df = pd.read_csv(CSV_FILE, index_col='Author')
                author = searchTerm  
                df2=df.query(f"Author == {author}")

                # Print all books found by that title or print message saying none found
                if df2.empty:
                    print("\nNo books found by that author. Please try again.\n")
                else:
                    print(df2)
                    print("\n")

        except ValueError:
            print("\nInvalid input. Please try again.\n")


    # Listing all Books in Bookstore 
    def listBooks(self):
        try:
            df = pd.read_csv(CSV_FILE)

            if df.empty:
                print("\nNo books found. Please try again.\n")
                
            else:
                print("\n")
                print(df)
                print("\n")
            return df
        
        except pd.errors.EmptyDataError:
            # Handle the case when there are no books in the bookstore yet
            return pd.DataFrame()
        
        



            