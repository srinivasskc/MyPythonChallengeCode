# Challenge 10 - Functions
'''
Write a program to create a function that takes list of numbers as arguments,
and returns the sum of all numbers in the list.
Then script should ask user to input 5 numbers, one at a time, and pass them as a list to the function.
call the function with the list as arguments.
Print the result.
'''


# defining the function will start with def
def sum_numbers(numbers):
  return sum(numbers)


user_numbers = []

for i in range(5):
  number = int(input(f'Enter number #{i+1}:'))
  user_numbers.append(number)

result = sum_numbers(user_numbers)
print("Sum of the numbers is: ", result)
