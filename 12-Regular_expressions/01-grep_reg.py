# Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. 
# Ask the user to enter a regular expression and count the number of lines that matched the regular expression.

import re

count = 0
reg = input("Enter a regular expression: ")
file = open("mbox.txt")
for line in file:
    if re.search(reg, line):
        count += 1
print("mbox.txt had", count, "lines that matched", reg)
