# Strings Slicing and Operations on Strings in Python
# ===================================================

# Length of a String
# We can find the length of a string using len() function.

name = "Muhammad umair"
print(name[0:12]) # this will print sequence of characters from 0 to 12 of name
print(len(name))


fruit = "mango"
print("mango is",len(fruit),"character word.")

# slicing
print(fruit[0:4]) # print from 0 to 3
print(fruit[:4]) # automaticallt add 0 on left side
print(fruit[:])  # will print all string
