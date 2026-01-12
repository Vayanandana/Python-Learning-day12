#String indexing in Python allows you to access individual characters using their position within square brackets ( [ ] ). Strings are zero-indexed.
#1️ Basic indexing (starts at 0)
word = "python"
print(word[0])
print(word[1])
print(word[2])

s = "Python"

print(s[0])  # P
print(s[3])  # h
print(s[5])  # n


#2️ Negative indexing (from the end)
s = "Python"

print(s[-1])  # n
print(s[-2])  # o
print(s[-6])  # P
