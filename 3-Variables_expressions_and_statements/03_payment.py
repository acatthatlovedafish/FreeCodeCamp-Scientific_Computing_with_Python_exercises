# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
hours = input("Enter the hours: ")
money = input("Enter the rate: ")
payment =  int(hours) * float(money)
print("Your total payment: ", round(payment, 2))
