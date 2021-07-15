# Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters “done”. 
# Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

new_lst = []

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
    
# The last line prints the largest and the smallest number
print("Maximum:", max(new_lst), "\nMinimum:", min(new_lst))
