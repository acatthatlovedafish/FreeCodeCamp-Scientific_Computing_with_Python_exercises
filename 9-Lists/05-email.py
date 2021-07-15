# Exercise 5: Minimalist Email Client.
# MBOX (mail box) is a popular file format to store and share a collection of emails. This was used by early email servers and desktop apps. 
# Without getting into too many details, MBOX is a text file, which stores emails consecutively. Emails are separated by a special line which starts with From (notice the space). 
# Importantly, lines starting with From: (notice the colon) describes the email itself and does not act as a separator. 
# Imagine you wrote a minimalist email app, that lists the email of the senders in the user’s Inbox and counts the number of emails.
# Write a program to read through the mail box data and when you find line that starts with “From”, you will split the line into words using the split function. 
# We are interested in who sent the message, which is the second word on the From line.
# You will parse the From line and print out the second word for each From line, then you will also count the number of From (not From:) lines and print out a count at the end.

#file = open("mbox-short.txt")
#count = 0
#for line in file:
#    if not line.startswith('From'):
#        continue
#    if line.startswith('From:'):
#        continue
#    else:
#        line = line.split()
#        line = line[1]
#        print(line)
#    count += 1
# print("There were", count, "lines in the file with From as the first word.")

# These two solutions produce the same results.

file = open("mbox-short.txt")
count = 0
for line in file:
	words = line.split()
  
	# guardian in a compound statement
	if len(words) < 3 or words[0] != "From":
		continue
	print(words[1])
	count += 1
  
print("There were", count, "lines in the file with From as the first word.")
