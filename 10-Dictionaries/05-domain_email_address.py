# Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). 
# At the end of the program, print out the contents of your dictionary.

#file = open(input("Enter a file name: "))
#count = dict()
#for line in file:
#    if not line.startswith('From'):
#        continue
#    if line.startswith('From:'):
#        continue
#    else:
#        line = line.split()
#        line = line[1]
#        line = line.split("@")
#        line = line[1]
#    count[line] = count.get(line, 0) + 1

#print(count)

# These solutions produce the same results

file = open(input("Enter a file name: "))
count = dict()
for line in file:
    words = line.split()
    # guardian in a compound statement
    if len(words) < 3 or words[0] != "From":
        continue
    else:
        words = words[1]
        words = words.split("@")
        words = words[1]
    count[words] = count.get(words, 0) + 1

print(count)
