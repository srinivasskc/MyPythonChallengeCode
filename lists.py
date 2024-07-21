# Challenge 8 - Lists

# Lists allow us to store multiple items in a single variable
'''
Write a program to store 5 different fruits.
Then asks user for the favourite  fruit.
If the fruit is in the list, print "I like this fruit too"
If the fruit is not in the list, print "I havent tried this fruit yet. I will give it a go!"
'''

favourite_fruits = ['Apple', 'Banana', 'Mango', 'PineApple', 'Sapota']
# Asking user for the favourite fruit
user_fav_fruit = input('What is your favourite fruit? ')
# Checking if the user's favourite fruit is in the list

if user_fav_fruit in favourite_fruits:
  print(f'I like this fruit too - {user_fav_fruit}')
# why we use: f'
#  F-strings allow you to embed expressions and variables directly into strings.

else:
  print(f'I havent tried this {user_fav_fruit} yet. I will give it a go!')
