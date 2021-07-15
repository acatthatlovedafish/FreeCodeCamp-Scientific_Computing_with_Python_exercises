# Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line.
# Count the number of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. 
# Then sort the list in reverse order and print out the person who has the most commits.

file = open(input("Enter a file name: "))
count = dict()
for line in file:
    words = line.split()
    
    # guardian in a compound statement
    if len(words) < 3 or words[0] != "From":
        continue
    else:
        words = words[1]
    count[words] = count.get(words, 0) + 1

#lst = []
#for key, val in count.items():
#    lst.append((val, key))

#for key, val in sorted(lst, reverse = True):
#    print(val, key)


# this line of code does almost the exact same thing as the upper one 

print(sorted([(v, k) for k, v in count.items()], reverse = True))
