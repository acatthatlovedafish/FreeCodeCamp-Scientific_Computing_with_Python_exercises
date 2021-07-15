# Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and 
# only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different 
# languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

import string

file = open(input("Enter a file name: "))
text = file.read()
count = dict()
for line in text:
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.replace(" ", "")
    line = line.strip()
    line = line.lower()
    for letter in line:
        count[letter] = count.get(letter, 0) + 1

lst = []
for key, val in count.items():
    lst.append((val, key))

print("The number of letters in the text you selected: ")
for key, val in sorted(lst, reverse = True):
    print(val, key)
