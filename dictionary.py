# Challenge 11 - Dictionaries
'''
Write a program to create a dictionary that stores information about the book.
The dictiionary should have the following keys:
Title, Author, Year of Publication, Genre, Pages.
Values for the keys should be taken from user input.
also add a key called 'is_favorite' with boolean value that indicates the book is fav or not.
'''

# Creating a dictionary for the book.
book = {
    'title': 'Growth Driven Testing',
    'author': 'Pradeep Soundararajan and Dhanasekar Subramaniam',
    'year_of_publication': 2023,
    'genre': 'Software Engineering',
    'pages': 254
}

# adding new key and value to the dictionary
book['is_favorite'] = False

print(book)
