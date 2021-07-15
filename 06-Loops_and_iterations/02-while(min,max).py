# Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

new_lst = []
count = 0
tot = 0.0

# while statement
while True:
    user = input("Enter a number: ")
    if user == 'done':
        break

# Error handling
    try:
        user2 = float(user)
    except:
        print("Invalid input")
        continue

    new_lst.append(user)
    count += 1
    tot += user2
    
# The last line prints the count, the sum, the smallest number and the largest number
print("Total count is: ",  count, "\nThe sum is: ", tot, "\nThe smallest number is: ", min(new_lst), "\nThe largest number is: ", max(new_lst))
