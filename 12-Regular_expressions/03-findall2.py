# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file 
# and compute the sum of the numbers.

import re

file = open("regex_sum_1073488.txt")
lst = []
for line in file:
    num = re.findall("[0-9]+", line)
    for n in num:
        n = int(n)
        lst.append(n)

print("Sum:", sum(lst))
