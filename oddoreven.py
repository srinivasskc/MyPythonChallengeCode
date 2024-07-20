# Challenge 5 - Even or Odd
'''
Write python program to ask for to enter a number from the user.
If the number is divisible by 2, print message - "Number is even."
If the number is not divisible by 2, print message - "Number is odd."
'''

num = int(input("Enter the number: "))
answer = num % 2
if answer == 0:
  print("Number is even.")
else:
  print("Number is odd.")
