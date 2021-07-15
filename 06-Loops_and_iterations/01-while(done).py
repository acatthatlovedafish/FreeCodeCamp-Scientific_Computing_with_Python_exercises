# Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. 
# If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

count = 0
tot = 0.0

# while statement
while True:
    user = input("Enter a number: ")
    if user == 'done':
        break

# Error handling
    try:
        user = float(user)
    except:
        print("Invalid input")
        continue

    count += 1
    tot += user
# The last line prints the count, the sum, and the average
print("The total count is: " , count, "\nThe sum is: " , tot, "\nThe average is: " , tot / count)
