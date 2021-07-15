# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

# Defining computepay program
def computepay(hours, money):
    if hours > 40:
        payment = ((hours - 40) * 1.5 * money) + (40 * money)
    else:
        payment = money * hours
    return str(round(payment, 2))

# Handling errors, + inputs
try:
    h = float(input("Enter hours: "))
    m = float(input("Enter rate: "))
except:
    print("Error, please enter numeric input")
    quit()

print("Your total payment: " + computepay(h, m))
