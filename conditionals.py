# Challenge 4 - Conditionals
'''
Write python program to ask for user age.
If the user is 18 or older, print message - "You are eligible to vote."
If the user is younger than 18, print message - "You are not eligible to vote."
'''

age = int(input('Enter your age: '))

if age >= 18:
  print('You are eligible to vote.')
else:
  print('You are not eligible to vote')
