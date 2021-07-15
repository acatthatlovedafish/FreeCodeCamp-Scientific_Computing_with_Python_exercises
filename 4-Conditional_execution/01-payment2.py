# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
hours = float(input("Enter hours: "))
money = float(input("Enter rate: "))

if hours > 40:
    payment = ((hours - 40) * 1.5 * money) + (40 * money)
else:
    payment = money * hours

print("Your total payment: " + str(round(payment, 2)))
