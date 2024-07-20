# Challenge 6 - Loops
'''
Write the program to ask the user to enter a number.
The script should countdown from that number to zero.
print the values till zero.
'''

num = int(input("Enter the number: "))

# For Loop
for i in range(num, -1, -1):
  print(i)

# While Loop
while num >= 0:
  print(num)
  num = num - 1
