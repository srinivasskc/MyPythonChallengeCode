# Challenge 9 - Input Lists
'''
Write a program to declare empty lists.
Then ask user to enter 3 different movies and adds them to the list.
Display the list of movies from the list.
'''

favourite_movies = []

for i in range(3):
  movie = input(f'Enter your favourite movie #{i+1}:')

  favourite_movies.append(movie)

print(f'Your favourite movies are: {favourite_movies}')

print(
    f'Your favourite movies are: {favourite_movies[0]}, {favourite_movies[1]}, {favourite_movies[2]}'
)
