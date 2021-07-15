# Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and 
# then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, 
# sorted by hour as shown below.

file = open(input("Enter a file name: "))
count = dict()
for line in file:
    words = line.split()
    
    # guardian in a compound statement
    if len(words) < 6 or words[0] != "From":
        continue
    else:
        words = words[5]
        words = words.split(":")
        words = words[0]
    count[words] = count.get(words, 0) + 1

lst = []
for key, val in count.items():
    lst.append((key, val))

for key, val in sorted(lst):
    print("Hour:", key, "No. of emails:", val)

# this line of code does almost the exact same thing as the upper one 

#print(sorted([(k, v) for k, v in count.items()]))
