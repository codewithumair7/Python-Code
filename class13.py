# String Methods in Python 
# Strings are immuteable

a = " Muhammad umair !!!!!!"
print(len(a))

# 1.The upper() method converts a string to upper case.
print(a.upper())
# 2.The lower() method converts a string to lower case.
print(a.lower())
# 3.The strip() method removes any white spaces before and after the string.
print(a.strip())
# 4.the rstrip() removes any trailing characters. Example:
print(a.rstrip("!"))
# 5.The replace() method replaces all occurences of a string with another string. Example:
print(a.replace("ai","a"))
# 6.The split() method splits the given string at the specified instance and returns the separated strings as list items.
print(a.split(" "))
# 7.The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.
print(a.capitalize())