# Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, 
# and print the dictionary.

file = open("mbox-short.txt")
count = dict()
for line in file:
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    else:
        line = line.split()
        line = line[1]
    count[line] = count.get(line, 0) + 1
print(count)

# These two solutions produce the same results

#file = open("mbox-short.txt")
#count = dict()
#for line in file:
#    words = line.split()
#    # guardian in a compound statement
#    if len(words) < 3 or words[0] != "From":
#        continue
#    line = words[1]
#    count[line] = count.get(line, 0) + 1
#print(count)
