# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.
celsius = input("Enter Celsius temperature: ")
to_fahrenheit = (int(celsius) * 9/5) + 32
print(celsius + "°C in Fahrenheit is: " + str(to_fahrenheit) + "°F.")
