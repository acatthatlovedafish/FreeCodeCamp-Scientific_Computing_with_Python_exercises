# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. 
# The following shows two executions of the program:
try:
    hours = float(input("Enter hours: "))
    money = float(input("Enter rate: "))
except:
    print("Error, please enter numeric input")
    quit()

if hours > 40:
    payment = ((hours - 40) * 1.5 * money) + (40 * money)
else:
    payment = money * hours

print("Your total payment: " + str(round(payment, 2)))
