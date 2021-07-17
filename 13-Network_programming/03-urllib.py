# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, (2) displaying up to 3000 characters, 
# and (3) counting the overall number of characters in the document. 
# Don’t worry about the headers for this exercise, simply show the first 3000 characters of the document contents.

import urllib.request

url = input("Enter an URL: ")
fhand = urllib.request.urlopen(url)
count = 0

for line in fhand:
    words = line.decode().strip()
    if count >= 3000:
        break
    count += len(words)
    print(words)
print("\nNumber of characters in the text:", count)
