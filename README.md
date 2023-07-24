# Online-Bookstore

Simple online bookstore inventory management system that allows the user to add books to the inventory, remove books from the inventory, and search for books by various parameters. Developed in Python.

#### Features:
1) Add Books: The system should allow the user to add a book to the inventory. Each book should have the following attributes: ISBN, title, author, publisher, year of publication, and quantity in stock.
2) Remove Books: The system should allow the user to remove a book from the inventory using the ISBN.
3) Search Books: The system should allow the user to search for a book by ISBN, title, or author.
4) List Books: The system should allow the user to list all the books in the inventory.
5) Persistence: The system should persist data across sessions. You can use a simple file-based storage system, or a database system if you prefer.
6) User Interface: The system should have a simple text-based user interface.
7) Error Handling: The system should handle errors gracefully and not crash when given invalid input.

## Files

* main.py: The main script for the online bookstore which handles interactions between the user and the bookstore. 
* bookstore.py: Defines the methods for the bookstore class, including how to add, remove, search, and list books.
* test.py: Test file that can be run to check the validity of the source code using a few unit test cases.

## Installation

Please download all the files to a folder. Within this folder, the 'src' folder and 'test' folders will exist. The 'src' folder will contain the bookstore.py and main.py files. The 'test' folder will contain the test.py file.

## Run Unit Test

To run test cases, open the terminal window. Change directories so that you are inside the folder containing the 'test.py' file. 

Run the unit test file using the following command: **$ python -m unittest discover test**

A separate 'data' folder will be created, containing the database.csv file, which will serve as the database for the online bookstore inventory management system. 

## Run Without Unit Test Cases

To run the file without test cases, change the directory into the 'src' folder where the main.py file is. From the terminal window, run the following command: **$ python3 main.py**

Follow the instructions as prompted after running the command.

Once again, a separate 'data' folder will be created, containing the database.csv file, which will serve as the database for the online bookstore inventory management system. 

## Some Design Decisions

* Use of a CSV File: Allows for a simple way to store data and manipulate it. Also enables efficiency in retrieving certain fields of data due to its format (table).
* Created the Bookstore Class: Allows for the code to be organized and easy to change in the case of any needed modification.
* Dataframe Usage: Used the Pandas library to easily query, read, and write to the CSV table as needed.
* Error Handling: Try & Except blocks were used in order to handle errors and repeatedly ask the user for valid input(s) and print respective error messages.
* File Organization: Files are organized into their own directories for source code, test code, and the database. This makes it easy to separate essential files from one another based on their purpose.

