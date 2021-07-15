# Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. 
# Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.
# Test your file on the mbox.txt and mbox-short.txt files.

open = open(input('Enter a file name: '))
count = 0
total = 0
for line in open:
    line = line.rstrip()
    place = line.find(" ")
    if line.startswith("X-DSPAM-Confidence:"):
        numberstr = line[place:]
        numberfloat = float(numberstr)
        count += 1
        total += numberfloat
print('The average spam confidence:', total/count)
