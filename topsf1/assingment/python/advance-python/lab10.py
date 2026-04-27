import re

text = "Hello Python"

x = re.search("Python", text)
if x:
    print("Found")

x = re.match("Hello", text)
if x:
    print("Matched")