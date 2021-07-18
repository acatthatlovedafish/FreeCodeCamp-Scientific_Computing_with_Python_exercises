# Exercise 4: Change the urllinks.py program to extract and count paragraph (p) tags from the retrieved HTML document and display 
# the count of the paragraphs as the output of your program. Do not display the paragraph text, only count them. 
# Test your program on several small web pages as well as some larger web pages.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as bs
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter an URL: ")
html = urllib.request.urlopen(url, context = ctx).read()
soup = bs(html, "html.parser")

# Count all of the paragraph (p) tags
count = 0
tags = soup("p")
for tag in tags:
    count += 1
print(count)
