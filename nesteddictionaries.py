# Challenge 12 - Nested Dictionaries
# Dictionary inside of Dictionary
'''
Create a function "add_book".
The function should take three arguments:
existing library dictionary, dictionary representing new book, 
name of the author of new book
The function should add the new book to the correct author in the library dictionary.
If the author does not exist in library yet, the function should add them.
'''

library = {}


def add_book(library, book, author):
  if author in library:
    library[author].append(book)
  else:
    library[author] = [book]


# Adding a book:
book = {
    "title": "Growth Driven Testing : Moolya way of testing",
    "year_published": 2023,
    "genre": 'Software Engineering'
}, {
    "title": "Buddha in Testing : Finding Peace in Chaos",
    "year_published": 2020,
    "genre": 'Software Testing'
}

add_book(library, book, 'Pradeep Soundararajan')

print(library)
