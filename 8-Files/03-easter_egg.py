# Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program. 
# Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name “na na boo boo”. 
# The program should behave normally for all other files which exist and don’t exist.

file = input("Enter a file name: ")
count = 0
total = 0

try:
    open(file)
except:
    if file == "na na boo boo":
        print("NA NA BOO BOO - Hurray, you've found an Easter Egg!")
    else:
        print("File cannot be opened:", file)
    quit()

for line in open(file):
    line = line.rstrip()
    place = line.find(" ")
    if line.startswith("X-DSPAM-Confidence:"):
        numberstr = line[place:]
        numberfloat = float(numberstr)
        count += 1
        total += numberfloat

print('The average spam confidence:', total/count)
