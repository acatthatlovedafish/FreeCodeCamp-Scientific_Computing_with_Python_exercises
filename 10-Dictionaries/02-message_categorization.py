# Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, 
# then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

#file = open("mbox-short.txt")
#count = dict()
#for line in file:
#    if not line.startswith('From'):
#        continue
#    if line.startswith('From:'):
#        continue
#    else:
#        line = line.split()
#        line = line[2]
#    count[line] = count.get(line, 0) + 1
#print(count)

# These two solutions produce the same results

file = open("mbox-short.txt")
count = dict()
for line in file:
    words = line.split()
    
    # guardian in a compound statement
    if len(words) < 3 or words[0] != "From":
        continue
    line = words[2]
    count[line] = count.get(line, 0) + 1
print(count)
