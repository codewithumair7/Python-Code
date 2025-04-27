# Strings in python
# ===================
# In python, anything that you enclose between single or double quotation marks is considered a string.
# A string is essentially a sequence or array of textual data.
# Strings are used when working with Unicode characters.


name = "Umair"
age = "22"
Education ="Bachelor"

print("Name is " +name+"  "+age+"  "+Education)

print('''I am a boy
My name is Umair
I am in bachelor''')

# Accessing Characters of a String
# =================================
# In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0.
# Square brackets can be used to access elements of the string.
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

# Looping through the string
# We can loop through strings using a for loop like this:

for character in name:
    print(character)