=========================================================
--------------------------DAY 3--------------------------
=========================================================

# Data Structures

    1. Sequences
    2. Sets
    3. Dictionaries

---------------------------------------------------------

# Lists

    - Ordered
    - Mutable
    - Duplicates are allowed
    - Mixed data types

### Methods

    - append, pop, remove
    - sort
    - List slicing

### List comprehensions & Nested List Comprehensions

---------------------------------------------------------

## Practice Programs

1. Demonstrate list methods
2. Display neg values from a numbers list
3. Second largest from a list
4. Count even and odds in a list
5. Delete an element from a list without using built-in methods
6. Count frequency of each element in a list
7. Filter unique elements from a list
8. Count the number of duplicate values in a list
9. You are building a simple E-commerce application in python. The system should maintain a list of products available in the cart. Write a python program to perform the following operations using lists:
   - Add a product to the cart
   - Remove a product from the cart
   - Search for a product in the cart
   - Display all products in the cart
   - Count number of products in the cart

---------------------------------------------------------

# Tuples

    - immutable

---------------------------------------------------------

## Practice Programs
1) A school stores student records as tuples in the format (roll_no, name, marks)
    Write a python program to:
    - Store the data of 5 students in a list of tuples
    - Print the name of the student who scored the highest marks
    - Print all students who scored more than 75 marks

---------------------------------------------------------
# Strings

---------------------------------------------------------
### Practice Programs
1) Find length of a string without using len method
2) Count alphabet, digits and special characters in a string
3) Count vowels and consonants in a string
4) Count number of words in a string
5) Count freq of a character in a string
6) Write a program for the following
    input: aaabbca
    output: a4b2c1
7) Find the highest frequency character in a string
8) Find the lowest frequency character in a string

---------------------------------------------------------
# Sets
    - No duplicates
    - Unordered
    - Mutable
    - Heterogeneous
    - Unindexed

## Set Operations
    - union (|) (.union())
    - intersection (&) (.intersection())
    - difference (-) (.difference())
    - symmetric difference (^) (.symmetric_difference()) : except those that are common in both
## Methods
    - add(), update()
    - remove(), discard(), pop(), clear()
    - Membership: in, not in
    - len, max, min, sum, sorted

---------------------------------------------------------
### Practice Programs
1) A 3-day tech workshop collected attendee registrations separately for each day. You are given three lists(day1, day2, day3) of email addresses - lists may contain duplicates (people registering multiple times) and email case may vary(Upper/Lower).
    Write a python program that:
        - Cleans each day's list (normalizes case, removes duplicates)
        - Prints the total number of unique attendees across all days.
        - Prints the list of attendees who attended all three days
        - Prints the list of attendees who attended exactly one day
        - Prints pairwise overlap counts(day1 & day2, day2 & 3, 3 & 1)
        - Produces a final report with counts and sorted lists for each of the above outputs

---------------------------------------------------------
# Dictionaries
    - key, value pairs
    - keys: mutable type
## Methods
    - values(), keys(), items()

---------------------------------------------------------
### Practice Programs
1) You are building a Library Management System in Python. The system should store books in a dictionary where, key is bookid and value is boot title. 
    Write a Python program to perform the following operations using Dictionaries:
        - Add a book to the library (Book Id, Title)
        - Remove a book using Book ID
        - Search for a book by Book ID and display the title
        - Update the title of a book (eg. correction in title)
        - Display all books in the library
        - Count the total number of books in the library
        - Check if a book title exists in the library (reverse look up)
