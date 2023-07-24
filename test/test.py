""" 
@file Online Bookstore Inventory Management System
@author Pearle Shah <shahpearle@outlook.com>
@date July 23, 2023
@description

Test file that can be run to check the validity of the source code using a few unit test cases. 
It tests for valid and invalid inputs for adding and removing books from the online bookstore. 
"""

import unittest
import os
import sys

# Go to directory one level up from current directory
PARENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add 'src' folder path to the sys.path list to allow relative imports
SRC_DIR = os.path.join(PARENT_DIR, "src")
sys.path.append(SRC_DIR)

# Relatively import bookstore
from bookstore import Bookstore  

# Test Cases
class TestMain(unittest.TestCase):

    # Set up instance for bookstore
    def setUp(self):
        self.bookstore = Bookstore()

    # Assumption: User entered 3 valid inputs into the database
    # Expected Output: Database should update with all three books
    def test_add_book_valid_input(self):
        # Valid input data for a new book
        valid_book_data = ["1234567890123", "Book 1", "Author 1", "Publisher 1", "2023", "5"]

        # Check if the book is added successfully without any errors
        self.bookstore.addBook(valid_book_data)

        # Valid input data for a second new book
        valid_book_data = ["1234567890124", "Book 2", "Author 2", "Publisher 2", "2022", "1"]

        # Check if the book is added successfully without any errors
        self.bookstore.addBook(valid_book_data)

        # Valid input data for a third new book
        valid_book_data = ["8172392748271", "Book 3", "Author 3", "Publisher 3", "1999", "3"]

        # Check if the book is added successfully without any errors
        self.bookstore.addBook(valid_book_data)


    # Assumption: User entered an invalid input (negative quantity of books)
    # Expected Output: Database should not update with these user inputs in the database. Error message should result.
    def test_add_book_invalid_input(self):
        # Invalid input data for a new book (Quantity is negative)
        invalid_book_data = ["1424567130123", "Book 1", "Author 1", "Publisher 1", "2023", "-5"]

        # Check if the bookstore raises a ValueError when adding the book
        try:
            self.bookstore.addBook(invalid_book_data)

        except ValueError as e:
            self.assertEqual(str(e), "Invalid quantity. Quantity must be a non-negative integer.")
            print("\nWarning Message Correctly Printed: Invalid quantity. Quantity must be a non-negative integer.\n")

        else:
            self.fail("Expected ValueError was not raised.")

    
    # Assumption: At least 1 book with the specific ISBN already exists in the database
    # Expected Output: All books with the inputted ISBN should be removed from the database
    def test_remove_book_valid_input(self):
        # Add a book to the database first to ensure there is a book to remove
        valid_book_data = ["1234562390124", "Book 4", "Author 4", "Publisher 4", "1924", "3"]
        self.bookstore.addBook(valid_book_data)

        # Add book 3 again to create multiple entries of book 3 in database and to ensure removal of all entries with that ISBN
        valid_book_data = ["8172392748271", "Book 3", "Author 3", "Publisher 3", "1999", "3"]        
        self.bookstore.addBook(valid_book_data)

        # Check if the book is removed successfully without any errors (Remove ALL books by given ISBN)
        isbn_to_remove = "8172392748271"
        self.bookstore.removeBook(isbn_to_remove)


    # Assumption: The user entered an invalid ISBN format
    # Expected Output: An error message should be printed
    def test_remove_book_invalid_input(self):
        # Invalid input data for ISBN (non-integer value)
        invalid_isbn = "81723_invalid_isbn"

        # Check if the bookstore raises a ValueError when trying to remove the book
        try:
            self.bookstore.removeBook(invalid_isbn)

        except ValueError as e:
            self.assertEqual(str(e), "Invalid ISBN format. Please enter a valid integer.")
            print("\nWarning Message Correctly Printed: Invalid ISBN format. Please enter a valid integer.\n")

        else:
            self.fail("Expected ValueError was not raised.")

if __name__ == '__main__':
    unittest.main()
