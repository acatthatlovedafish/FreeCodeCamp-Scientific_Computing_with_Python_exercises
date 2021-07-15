# Exercise 4: Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, 
# look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

file = open(input("Enter a file name: "))
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

maxcount = None
maxword = None
for word, count in count.items():
    if maxcount is None or count > maxcount:
        maxword = word
        maxcount = count
print("From the file", file, "the email address with the most messages is:", maxword, "with", maxcount, "emails.")
