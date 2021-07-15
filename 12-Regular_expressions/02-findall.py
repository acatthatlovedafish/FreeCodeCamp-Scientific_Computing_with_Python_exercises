# Exercise 2: Write a program to look for lines of the form:
# New Revision: 39772
# Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average as an integer.

import re

file = open("mbox.txt")
lst = []
for line in file:
    num = re.findall("^New Revision: ([0-9]+)", line)
    if len(num) != 1:
        continue
    for n in num:
        n = float(n)
    lst.append(n)

print("Average:", sum(lst)/len(lst))
