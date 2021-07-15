# Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case.
# You can download the file from www.py4e.com/code3/mbox-short.txt

open = open(input('Enter a file name: '))
for line in open:
    clean = line.rstrip()
    print(clean.upper())
